import sys
import os
import colorama
from colorama import Fore, Back, Style
import textwrap
import random
import shutil
import time
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter
import cv2
import re

colorama.init(autoreset=True)

class Question:
    def __init__(self, question, image_question, hints, correct_answers, incorrect_answers, other_answers, image_answer):
        self.question = question
        self.image_question = image_question
        self.hints = hints
        self.correct_answers = correct_answers
        self.incorrect_answers = incorrect_answers
        self.other_answers = other_answers
        self.image_answer = image_answer
        self.miss = 0
        random.shuffle(self.hints)
        
    def write(self, filename):
        
        if filename == '':
            return
        
        question = self.question
        
        if self.hints:
            question += f"$hint\n" + "\n".join(self.hints)
            
        question += "\n$answer"
        
        if self.correct_answers:
            question += f"\n$correct\n" + "\n".join(self.correct_answers)
            
        if self.incorrect_answers:
            question += f"\n$wrong\n" + "\n".join(self.incorrect_answers)
            
        if self.other_answers:
            question += f"\n$other\n" + "\n".join(self.other_answers)
            
        if self.image_answer:
            question += f"\n$image\n" + self.image_answer
            
        question = re.sub(r'\n+', '\n', question)
        question += "\n\n"    
            
        with open(filename, "a", encoding="utf-8") as f:
            f.write(question)

    def print_divider(self, title, symbol="-", style=Fore.YELLOW + Back.BLUE + Style.BRIGHT):
        length = shutil.get_terminal_size().columns
        print(style + symbol * length)
        wrapped_title = textwrap.fill(title, width=length-4, subsequent_indent=' ' * ((length - len(title)) // 2))
        print(style + f"{symbol} {wrapped_title} {symbol}".center(length))
        print(style + symbol * length)

    def print_styled_text(self, text, style, indent=4):
        wrap_length = shutil.get_terminal_size().columns - indent
        lines = text.split('\n')
        for line in lines:
            wrapped_text = textwrap.fill(line, width=wrap_length, initial_indent=' ' * indent, subsequent_indent=' ' * indent)
            print(style + wrapped_text)

    def print_section(self, title, answers, color):
        self.print_divider(title, symbol="-", style=color + Back.BLACK + Style.BRIGHT)
        for answer in answers:
            if answer.strip():
                self.print_styled_text("- " + answer, color + Style.NORMAL)
        print()

    def print_question(self, i, l, streak, max_streak):
        i+=1
        self.print_divider(f"Question {i}/{l}, {l-i} Left, Current Streak: {streak}, Max Streak: {max_streak} ", symbol="=", style=Fore.BLACK + Back.BLACK + Style.BRIGHT)
        print()
        self.print_styled_text(self.question, Fore.RESET + Style.BRIGHT + Style.BRIGHT)
        print()
        if self.hints:
            for hint in self.hints:
                if hint:
                    self.print_styled_text("    - " + hint, Fore.LIGHTWHITE_EX + Style.DIM)
            print()
        if self.image_question:
            self.show_image_question()
            
    def show_image_answer(self):
        img = cv2.imread(self.image_answer.strip(), cv2.IMREAD_ANYCOLOR)
        cv2.namedWindow("Answer", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Answer", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("Answer", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def show_image_question(self):
        img = cv2.imread(self.image_question.strip(), cv2.IMREAD_ANYCOLOR)
        cv2.namedWindow("Question", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Question", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("Question", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def print_answers(self):
        if self.correct_answers:
            self.print_section("Correct Answers", self.correct_answers, Fore.GREEN)
        if self.incorrect_answers:
            self.print_section("Incorrect Answers", self.incorrect_answers, Fore.RED)
        if self.other_answers:
            self.print_section("Answer", self.other_answers, Fore.WHITE)
        if self.image_answer:
            self.show_image_answer()

class QuestionParser:
    def __init__(self, text):
        self.text = text
        self.questions = []

    def parse(self):
        question_blocks = self.text.split('\n\n')
        for block in question_blocks:
            
            if "$answer" not in block:
                continue
            
            hints = []
            correct_answers = []
            wrong_answers = []
            other_answers = []
            image_question = None
            image_answer = None
            
            question, answer = block.split("$answer\n")   
            
            if "$hint" in question:
                question, hint = question.split("$hint\n")
                hints = hint.split("\n")
            if "$image" in question:
                question, image_question = question.split("$image\n")
                
            question = "\n".join(question.split("\n"))
                
            if "$correct" in answer:
                correct = answer.split("$correct\n")[1].split("\n$")[0]
                correct_answers = correct.split("\n") if correct else []
            if "$wrong" in answer:
                wrong = answer.split("$wrong\n")[1].split("\n$")[0]
                wrong_answers = wrong.split("\n") if wrong else []
            if "$other" in answer:
                other = answer.split("$other\n")[1].split("\n$")[0]
                other_answers = other.split("\n") if other else []
            if "$image" in answer:
                image_answer = answer.split("$image\n")[1].split("\n$")[0]
            
            self.questions.append(Question(question, image_question, hints, correct_answers, wrong_answers, other_answers, image_answer))

    def get_questions(self):
        return self.questions

class QuizApp:
    def __init__(self, filepath, t=10, s=True, missed_file="missed.txt"):
        self.running = True
        self.answer_printed = False
        self.filepath = filepath
        self.questions = self.get_questions(filepath)
        self.n = 0
        self.t = t
        self.streak = 0
        self.max_streak = 0
        self.missed_file = missed_file
        if s:
            random.shuffle(self.questions)
        
    def print_divider(self, title, symbol="-", middle_symbol="-", middle_symbol_length=0, style=Fore.YELLOW + Back.BLUE + Style.BRIGHT):
        length = shutil.get_terminal_size().columns
        print(style + symbol * length)
        adjusted_length = length - 4 - len(title)
        wrapped_title = textwrap.fill(title, width=length-4, subsequent_indent=' ' * (adjusted_length // 2))
        print(style + f"{middle_symbol} {wrapped_title} {middle_symbol}".center(length + middle_symbol_length))
        print(style + symbol * length)

    def get_questions(self, filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            text_input = f.read()
        parser = QuestionParser(text_input)
        parser.parse()
        return parser.get_questions()

    def get_key_press(self):
        if os.name == 'nt':
            import msvcrt
            return msvcrt.getch().decode()
        else:
            import tty, termios, sys
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
                if ch == '\x1b':  # ESC key
                    return 'esc'
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch


    def next_question(self):
        if self.n < len(self.questions):
            self.n += 1
            self.answer_printed = False

    def wrong_answer(self):
        if not self.answer_printed:
            return
        
        incorrect_answers = [
            "Swing and a miss. 🏓",
            "Next one's yours! 💖",
            "Ah, almost! 🤏",
            "Seemed right to me 🧐",
            "Who's counting anyways? 🤓",
            "Missed! 🚀",
            "Whoopsie daisy! 🌼",
            "Swing and a miss! ⚾",
            "That was a toughie. 🤷",
            "Next time definitely! 😉",
            "Missed! Keep swinging. 🏌️‍♂️",
            "I still believe in you. 🌟",
            "Let's try another. 🎲",
            "Whoops! 🫣",
            "Almost! Keep going! 👣",
            "That one was tough! 🤨",
            "Shell we try again? 🐚",
            "Oh no... anyway... 👉"
        ]
        
        self.streak = 0
        
        self.print_divider(random.choice(incorrect_answers), style=Fore.RED + Back.BLACK + Style.BRIGHT, middle_symbol_length=-1)
        time.sleep(1)
        
        question = self.questions[self.n]
        question.miss += 1
        
        self.questions.insert(min(self.n + self.t, len(self.questions)), question)
        
        question.write(self.missed_file)
        
        for _ in range(question.miss - 1):
            self.questions.insert(random.randint(self.n + 1, len(self.questions)), question)
        
        self.next_question()

    def correct_answer(self):
        if not self.answer_printed:
            return
        
        correct_answers = [
            "🎉 You're on fire!",
            "Spot on! 🌟",
            "🏆 You're crushing it!",
            "Right you are! 🧠",
            "Nailed it! ⚒️",
            "Yes! 💡",
            "Aced it! ✅",
            "Absolutely right! 📚",
            "Slow down Einstein! 🤯",
            "Perfect! 🌈",
            "You're on fire. 🔥",
            "You're a genius. 🧠",
            "Yes! Keep rolling. 🎳",
            "You're unstoppable. 🚄",
            "Crushing it. 🥊",
            "Aced it! 🌟",
            "You're a rock star. 🎸",
            "Perfect!🏆",
            "Absolutely! 😎",
        ]
        
        self.streak += 1
        if self.streak > self.max_streak:
            self.max_streak = self.streak
        
        self.print_divider(random.choice(correct_answers), style=Fore.GREEN + Back.BLACK + Style.BRIGHT, middle_symbol_length=-1)
        time.sleep(1)
        
        self.next_question()

    def previous_answer(self):
        if self.n > 0:
            self.n -= 1
            self.answer_printed = False
            
    def print_controlls(self):
        print(Fore.LIGHTWHITE_EX + Style.DIM + "Press any key to show answer, 'a' to repeat, 'd' to proceed, 'w' to return, 'q' to quit.\n")

    def print_prompt(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_controlls()
        
        end_of_quiz = [
            "Quiz completed! 🎉 You're a star! 🌟",
            "All done! 🏁 Your brain deserves a trophy. 🏆",
            "That's all, folks! 🐷 Time to celebrate! 🎊",
            "End of the road! 🛣️ You've done splendidly! 💐",
            "No more questions! 🚫 You've conquered this quiz! 🏔️",
            "Quiz over! 📚 Time for a well-deserved break! ☕",
            "You've reached the end! 🏠 What a journey, huh? 🌍",
            "All out of questions! 📖 You're officially a quiz whiz! 🧙‍♂️",
            "Finished! 🏆 Take a bow; you've earned it! 🎻",
            "That's a wrap! 🎬 You've aced this challenge! 🥇",
        ]
        
        if self.n >= len(self.questions):
            self.print_divider(f"{random.choice(end_of_quiz)}, Your max streak was {self.max_streak}", style=Fore.CYAN + Back.BLACK + Style.BRIGHT, middle_symbol_length=-2)
            restart = input("🔁 Wanna do that all over again? (Yes/no) ")
            if restart.strip().lower() in ['yes', 'y', '']:
                self.n = 0
                print("All right! 👌")
                print(f"🎮 Running quiz with {'🔀 shuffled' if shuffle else '📚 ordered'} questions, 🔄 every {steps} questions for repeats, from file 📁 {filename}")
                for i in range(5, 0, -1):
                    print(f"\r🚀 And we're beginninng in {i}... 🚀", end="", flush=True)
                    time.sleep(1)
                self.print_prompt()
            else:
                print("👋 See you in the next quiz!")
                sys.exit()
        
        else:
            self.questions[self.n].print_question(self.n, len(self.questions), self.streak, self.max_streak)
            if not self.answer_printed and not self.questions[self.n].image_question:
                self.get_key_press()
            self.questions[self.n].print_answers()
            self.answer_printed = True

    def run(self):
        while self.running:
            self.print_prompt()
            key = self.get_key_press()
            if key == 'esc':
                break
            elif key == 'a':
                self.wrong_answer()
            elif key == 'd':
                self.correct_answer()
            elif key == 'w':
                self.previous_answer()
            
            
def get_filename_with_path_hinting(text, test=True):
    completer = PathCompleter()
    filename = prompt(text, completer=completer)
    while test:
        try:
            with open(filename, "r", encoding="utf-8") as f:
                f.read()
            break
        except:
            filename = prompt(f"I don't see any {filename} 👀 Let's give it another try ", completer=completer)
    return filename

if __name__ == "__main__":
    
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("🌟 Welcome to the Ultimate Quiz App! Let's get your quiz journey started. 🚀")
        print("But first, I need some juicy details to spice things up... 🌶️")
        
        filename = get_filename_with_path_hinting("📄 What's the name of the question file? ", test=True)

        shuffle_ans = input("🎲 Do you love surprises? Should I shuffle the questions? ")
        
        missed_file = get_filename_with_path_hinting("📄 Where should we save answers you miss? ", test=False)
        if missed_file == '':
            print(f"👌 Alright! We won't save them for now.")
        else: 
            print(f"👌 Alright! We'll keep them in {missed_file}")
        
        steps_ans = input("💭 How often should we revisit the ones you miss? ")

        shuffle = shuffle_ans.strip().lower() in ['yes', 'y', '']
        try:
            assert steps_ans
            steps = int(steps_ans.strip())
        except Exception:
            print("🤔 That doesn't look like a number. I'll just assume you're cool with revisiting every 10 questions.")
            steps = 10

        print(f"🎮 Running quiz with {'🔀 shuffled' if shuffle else '📚 ordered'} questions, 🔄 every {steps} questions for repeats, from file 📁 {filename}")
        for i in range(5, 0, -1):
            print(f"\r🚀 And we're beginninng in {i}... 🚀", end="", flush=True)
            time.sleep(1)

        app = QuizApp(filename, t=steps, s=shuffle, missed_file=missed_file)
        app.run()
    except KeyboardInterrupt:
        pass


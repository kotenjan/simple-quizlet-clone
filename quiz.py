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
from PIL import Image
import numpy as np
import tkinter
import json
import hashlib

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
        
    def generate_id(self):
        """
        Generates a unique ID based on the object's attributes.
        """
        # Create a dictionary of all relevant attributes
        data = {
            'question': self.question,
            'image_question': self.image_question,
            'hints': self.hints,
            'correct_answers': self.correct_answers,
            'incorrect_answers': self.incorrect_answers,
            'other_answers': self.other_answers,
            'image_answer': self.image_answer
        }
        
        # Serialize the dictionary into a JSON string with sorted keys
        json_string = json.dumps(data, sort_keys=True)
        
        # Generate a SHA-256 hash of the JSON string
        unique_id = hashlib.sha256(json_string.encode()).hexdigest()
        
        return unique_id
        
    def write(self, filename):
        
        if filename == '':
            return
        
        question = self.question
        
        if self.hints:
            question += f"\n$hint\n" + "\n".join(self.hints)
            
        if self.image_question:
            question += f"\n$image\n" + self.image_question
            
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
            
        try:
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()
        except:
            content = ""
            
        if question not in content:
            with open(filename, "a", encoding="utf-8") as f:
                f.write(question)

    def print_divider(self, title, symbol="-", style=Fore.YELLOW + Style.BRIGHT):
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
        self.print_divider(title, symbol="-", style=color + Style.BRIGHT)
        for answer in answers:
            if answer.strip():
                self.print_styled_text("- " + answer, color + Style.NORMAL)
        print()

    def print_question(self, i, l, streak, max_streak):
        self.print_divider(f"Question {i}/{l}, {l-i} Left, Current Streak: {streak}, Max Streak: {max_streak} ", symbol="=", style=Fore.BLACK + Style.BRIGHT)
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

    def add_black_background_to_16_9(self, image):
        image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        original_width, original_height = image.size

        screen_width = 1920
        screen_height = 1080

        target_aspect_ratio = screen_width / screen_height
        current_aspect_ratio = original_width / original_height

        # New width based on the target aspect ratio, keeping the original height
        new_width = max(original_width, screen_width)
        new_height = max(original_height, screen_height)
        
        if current_aspect_ratio < target_aspect_ratio:
            new_width = max(int(target_aspect_ratio * original_height), screen_width)
        elif current_aspect_ratio > target_aspect_ratio:
            new_height = max(int(original_width / target_aspect_ratio), screen_height)

        new_image = Image.new('RGB', (new_width, new_height), (61, 61, 61))
        # Calculating the position to center the original image
        left = (new_width - original_width) // 2
        top = (new_height - original_height) // 2
        new_image.paste(image, (left, top))
    
        return cv2.cvtColor(np.array(new_image), cv2.COLOR_RGB2BGR)
            
    def show_image_answer(self):
        img = cv2.imread(self.image_answer.strip(), cv2.IMREAD_ANYCOLOR)

        img = self.add_black_background_to_16_9(img)

        cv2.namedWindow("Answer", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Answer", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("Answer", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def show_image_question(self):
        img = cv2.imread(self.image_question.strip(), cv2.IMREAD_ANYCOLOR)

        img = self.add_black_background_to_16_9(img)

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
    def __init__(self, filepath, phrase_dir='phrases', t=5, s=True, stats_file=None):
        self.running = True
        self.answer_printed = False
        self.filepath = filepath
        self.questions = self.get_questions(filepath)
        self.n = 0
        self.t = t
        self.streak = 0
        self.max_streak = 0
        self.stats_file = stats_file
        self.phrase_dir = phrase_dir

        # Load phrases from files
        self.incorrect_answers = self.load_phrases('incorrect_answers.txt')
        self.correct_answers = self.load_phrases('correct_answers.txt')
        self.end_of_quiz = self.load_phrases('end_of_quiz.txt')
        
        self.stats = self.load_stats()
        
        if s:
            random.shuffle(self.questions)
            
        self.questions = sorted(
            self.questions,
            key=lambda question: 0 if question.generate_id() not in self.stats else max(1, self.stats[question.generate_id()][0] - self.stats[question.generate_id()][1])
        )

    def load_phrases(self, filename):
        path = os.path.join(self.phrase_dir, filename)
        if not os.path.exists(path):
            print(f"Phrase file {path} not found. Please ensure it exists.")
            sys.exit(1)
        with open(path, 'r', encoding='utf-8') as f:
            phrases = [line.strip() for line in f if line.strip()]
        return phrases

    def print_divider(self, title, symbol="-", middle_symbol="-", middle_symbol_length=0, style=Fore.YELLOW + Style.BRIGHT):
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
        if self.n < len(self.questions) - 1:
            self.n += 1
            self.answer_printed = False
        else:
            self.n += 1  # To trigger end of quiz
        self.save_stats()

    def wrong_answer(self):
        if not self.answer_printed:
            return
        
        message = random.choice(self.incorrect_answers)
        self.streak = 0
        
        self.print_divider(message, style=Fore.RED + Style.BRIGHT, middle_symbol_length=-1)
        time.sleep(1)
        
        question = self.questions[self.n]
        
        if question.generate_id() in self.stats:
            self.stats[question.generate_id()][1] = self.stats[question.generate_id()][1] + 1
        else:
            self.stats[question.generate_id()] = [0, 1]
            
        question.miss += 1
        
        insert_position = min(self.n + self.t, len(self.questions))
        self.questions.insert(insert_position, question)
        
        for _ in range(question.miss - 1):
            self.questions.insert(random.randint(self.n + 1, len(self.questions)), question)
        
        self.next_question()

    def correct_answer(self):
        if not self.answer_printed:
            return
        
        message = random.choice(self.correct_answers)
        
        question = self.questions[self.n]
        
        if question.generate_id() in self.stats:
            self.stats[question.generate_id()][0] = self.stats[question.generate_id()][0] + 1
        else:
            self.stats[question.generate_id()] = [1, 0]
        
        self.streak += 1
        if self.streak > self.max_streak:
            self.max_streak = self.streak
        
        self.print_divider(message, style=Fore.GREEN + Style.BRIGHT, middle_symbol_length=-1)
        time.sleep(1)
        
        self.next_question()

    def previous_answer(self):
        if self.n > 0:
            self.n -= 1
            self.answer_printed = False

    def print_controlls(self):
        print(Fore.LIGHTWHITE_EX + Style.DIM + "Press any key to show answer, 'a' to mark incorrect, 'd' to mark correct, 'w' to go back, 'q' to quit.\n")

    def print_prompt(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_controlls()
        
        end_of_quiz_messages = self.end_of_quiz
        
        if self.n >= len(self.questions):
            message = random.choice(end_of_quiz_messages)
            self.print_divider(f"{message}, Your max streak was {self.max_streak}", style=Fore.CYAN + Style.BRIGHT, middle_symbol_length=-2)
            restart = input("🔁 Wanna do that all over again? (Yes/no) ")
            if restart.strip().lower() in ['yes', 'y', '']:
                self.n = 0
                self.streak = 0
                print("All right! 👌")
                print(f"🎮 Running quiz with 🔀 shuffled questions, 🔄 every {self.t} questions for repeats, from file 📁 {self.filepath}")
                for i in range(5, 0, -1):
                    print(f"\r🚀 And we're beginning in {i}... 🚀", end="", flush=True)
                    time.sleep(1)
                self.print_prompt()
            else:
                print("👋 See you in the next quiz!")
                sys.exit()
        
        else:
            current_question = self.questions[self.n]
            current_question.print_question(self.n + 1, len(self.questions), self.streak, self.max_streak)
            if not self.answer_printed and not getattr(current_question, 'image_question', False):
                key = self.get_key_press()
                if key == 'q':
                    self.running = False
                    sys.exit()
                elif key == 'esc':
                    self.running = False
                    sys.exit()
                # Handle other keys if necessary
            if not self.answer_printed:
                self.questions[self.n].print_answers()
                self.answer_printed = True

    def run(self):
        while self.running:
            self.print_prompt()
            key = self.get_key_press()
            if key == 'esc' or key.lower() == 'q':
                print("👋 Exiting the quiz. Goodbye!")
                break
            elif key.lower() == 'a':
                self.wrong_answer()
            elif key.lower() == 'd':
                self.correct_answer()
            elif key.lower() == 'w':
                self.previous_answer()
                
    def load_stats(self):
        if os.path.exists(self.stats_file):
            with open(self.stats_file, 'r', encoding='utf-8') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    print(f"Error decoding JSON from {self.stats_file}. Initializing empty stats.")
                    return {}
        else:
            return {}
            
    def save_stats(self):
        with open(self.stats_file, 'w', encoding='utf-8') as f:
            json.dump(self.stats, f, indent=4)
            
            
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
        
        stats_file = filename.split(".txt")[0] + "_stats.json"
        
        steps_ans = input("💭 How often should we revisit the ones you miss? ")

        shuffle = shuffle_ans.strip().lower() in ['yes', 'y', '']
        try:
            assert steps_ans
            steps = int(steps_ans.strip())
        except Exception:
            steps = 5

        print(f"🎮 Running quiz with {'🔀 shuffled' if shuffle else '📚 ordered'} questions, 🔄 every {steps} questions for repeats, from file 📁 {filename}")
        for i in range(3, 0, -1):
            print(f"\r🚀 And we're beginninng in {i}... 🚀", end="", flush=True)
            time.sleep(1)

        app = QuizApp(filename, t=steps, s=shuffle, stats_file=stats_file)
        app.run()
    except KeyboardInterrupt:
        pass


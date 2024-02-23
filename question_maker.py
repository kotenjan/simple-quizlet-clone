import os
import time
import re
import colorama
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter
import cv2

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
            question += f"\n$other\n" + self.other_answers
            
        if self.image_answer:
            question += f"\n$image\n" + self.image_answer
            
        question = re.sub(r'\n+', '\n', question)
        question += "\n\n"    
            
        with open(filename, 'a', encoding='utf-8', errors='ignore') as f:
            f.write(question)

class QuizCreator:
    def __init__(self, filename, question_img=False, question_hint=False, default_answer=False, correct_answer=False, answer_img=False, img_path=None):
        self.filename = filename
        self.question_img = question_img
        self.question_hint = question_hint
        self.default_answer = default_answer
        self.correct_answer = correct_answer
        self.answer_img = answer_img
        self.img_path = img_path
        self.img_index = 0
        self.questions = []
            
    def select_image(self):

        images = sorted([img for img in os.listdir(self.img_path) if img.endswith('.png')])

        def show_image(index):
            # Read and show the current image
            img_path = os.path.join(self.img_path, images[index])
            img = cv2.imread(img_path)
            cv2.imshow("Image Browser", img)

        cv2.namedWindow("Image Browser", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Image Browser", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        show_image(self.img_index)

        img_path = None
        
        while True:
            key = cv2.waitKey(0) & 0xFF
            if key == ord('q') or key == 27:  # Quit on 'q' or ESC
                break
            elif key == 13:  # Enter key
                img_path = os.path.join(self.img_path, images[self.img_index])
                self.img_index = (self.img_index + 1) % len(images)
                break
            elif key == 81 or key == 2424832:  # Left arrow
                self.img_index = (self.img_index - 1) % len(images)
                show_image(self.img_index)
            elif key == 83 or key == 2555904:  # Right arrow
                self.img_index = (self.img_index + 1) % len(images)
                show_image(self.img_index)

        cv2.destroyAllWindows()
        
        return img_path
    
    def multiline_input(self, prompt, line_start):
        print(prompt + " (Enter on a new line when finished) \n")
        lines = []
        while True:
            line = input(line_start)
            if line == "":
                print("\033[A                             \033[A")
                break
            lines.append(line)
        return lines

            
    def add_question(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        question = Question(None, None, None, None, None, None, None)

        print("🌟 Let's craft a new question! \n")
        question.question = "\n".join(self.multiline_input("✏️  Spin the question wheel!", line_start="    "))

        if self.question_hint:
            print("💡 Need a hint? Drop some breadcrumbs here: ")
            question.hints = self.multiline_input("Enter hints", line_start="  - ")
            
        if self.question_img:
            print("\n📸 Snap! Add a picture to your question (leave blank for a mystery): ")
            question.image_question = self.select_image()
            print("\n    " + str(question.image_question) + " 🖼️")
            
        if self.default_answer:
            question.other_answers = "\n".join(self.multiline_input("\nEnter answer", line_start="    "))

        if self.correct_answer:
            question.correct_answers = self.multiline_input("\nEnter correct answers", line_start="  - ")

        if self.correct_answer:
            question.incorrect_answers = self.multiline_input("\nEnter incorrect answers", line_start="  - ")
        
        if self.answer_img:
            print("\n🖼️ Got a pic that gives it away? Share the answer image path (or keep the suspense): ")
            question.image_answer = self.select_image()
            print("\n    " + str(question.image_answer) + " 📷")

        return question

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

    def run(self):
        while True:
            question = self.add_question()
            key_pressed = self.get_key_press()
            if key_pressed == 'esc':
                break     
            if key_pressed == 'r':
                continue
            question.write(self.filename)       
            
def get_filename_with_hinting(text, verify=True):
    completer = PathCompleter()
    
    filename = ""
    
    while filename == "":
        filename = prompt(text, completer=completer)
        if filename == "":
            print(f"⚠️ You did not specify any name. Let's try that again ")
    
    if verify:
        if os.path.exists(filename):
            print(f"⚠️ There's already a {filename}. I'll append the questions to it ")
        
    return filename

def get_image_path_with_hinting(text, verify=True):
    
    while True:
        completer = PathCompleter()
        filename = prompt(text, completer=completer)
        if verify:
            if os.path.exists(filename):
                if not any(file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')) for file in os.listdir(filename)):
                    answer = input(f"I don't see any images in {filename}. 👀 Should we try again? (Yes/no)")
                    if answer.strip().lower() in ['yes', 'y', '']:
                        continue
            else:
                answer = input(f"The directory '{filename}' does not exist. 👀 Should we try again? (Yes/no) ")
                if answer.strip().lower() in ['yes', 'y', '']:
                    continue
        return filename
            

if __name__ == "__main__":
    
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("🌟 Welcome to the Ultimate Quiz Creator! Let's craft some engaging quizzes. 🚀")
        print("Before we dive in, I need a bit more info to tailor the experience... 🛠️")

        filename = get_filename_with_hinting("📁 Tell me, where do you wish to store your questions? ")
        
        print("📌 Note: For questions and answers with images, ensure you have the images ready. ")
        question_img = input("🖼️ Do the questions include images? (Yes/no) ")
        question_img = question_img.strip().lower() in ['yes', 'y', '']
        question_hint = input("💡 Do the questions include hints? (Yes/no) ")
        question_hint = question_hint.strip().lower() in ['yes', 'y', '']
        default_answer = input("🔮 Do you want to set a default answer for the questions? (Yes/no) ")
        default_answer = default_answer.strip().lower() in ['yes', 'y', '']
        correct_answer = input("✅/❌ Will you specify correct answers for questions? (Yes/no) ")
        correct_answer = correct_answer.strip().lower() in ['yes', 'y', '']
        answer_img = input("🖼️ Do the answers include images? (Yes/no) ")
        answer_img = answer_img.strip().lower() in ['yes', 'y', '']
        img_path = None
        if answer_img or question_img:
            img_path = get_image_path_with_hinting("📁 Tell me, where should I look for images? ", verify=True)

        print(f"✨ Creating a quiz with {'images in questions' if question_img else 'no images in questions'}, {'hints' if question_hint else 'no hints'}, {'a default answer' if default_answer else 'no default answer'}, {'correct and incorrect answers explicitly marked' if correct_answer else 'not marking correct or incorrect answers explicitly'}, and {'images in answers' if answer_img else 'no images in answers'}, all stored in 🗂️ {filename}.")
        for i in range(3, 0, -1):
            print(f"\r🎉 Let the crafting begin in {i}... 🎉", end="", flush=True)
            time.sleep(1)

        try:
            app = QuizCreator(filename, question_img=question_img, question_hint=question_hint, default_answer=default_answer, correct_answer=correct_answer, answer_img=answer_img, img_path=img_path)
            app.run()
        except KeyboardInterrupt:
            pass

    except KeyboardInterrupt:
        pass



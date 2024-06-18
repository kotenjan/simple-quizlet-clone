import os
import time
import re
import colorama
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter
import cv2
from time import sleep
import sys

colorama.init(autoreset=True)

class Question:
    def __init__(self, image_question, image_answer):
        self.image_question = image_question
        self.image_answer = image_answer
        self.miss = 0
        
    def write(self, filename):
        
        if filename == '':
            return
        
        question = ""
        
        if self.image_question:
            question += f"\n$image\n" + self.image_question
        
        question += "\n$answer"
            
        if self.image_answer:
            question += f"\n$image\n" + self.image_answer
            
        question = re.sub(r'\n+', '\n', question)
        question += "\n\n"    
            
        with open(filename, 'a', encoding='utf-8', errors='ignore') as f:
            f.write(question)

class QuizCreator:
    def __init__(self, filename, img_path=None):
        self.filename = filename
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
            
    def add_question(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        question = Question(None, None)

        print("🌟 Let's craft a new question! \n")

        print("\n📸 Snap! Add a picture to your question: ")
        question.image_question = self.select_image()
        print("\n    " + str(question.image_question) + " 🖼️")
        
        print("\n🖼️ Share the answer image path: ")
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
                print("\nNot saving that one ❌")
                sleep(1)
                continue
            print("\nMoving onto another ⏭️")
            question.write(self.filename)       
            sleep(0.2)
            
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
                    answer = input(f"I don't see any images in {filename}. 👀 Should we try again? (Yes/no) ")
                    if answer.strip().lower() in ['yes', 'y', '']:
                        continue
            else:
                answer = input(f"The directory '{filename}' does not exist. 👀 Should we try again? (Yes/no) ")
                if answer.strip().lower() in ['yes', 'y', '']:
                    continue
        return filename
            

if __name__ == "__main__":
    
    try:
        
        filename = sys.argv[1]
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("🌟 Welcome to the Ultimate Quiz Creator! Let's craft some engaging quizzes. 🚀")
        print("Before we dive in, I need a bit more info to tailor the experience... 🛠️")

        if not os.path.isdir(os.path.dirname(filename)):
            filename = get_filename_with_hinting("📁 Couldn't find the questions directory🥺 Tell me, where do you wish to store your questions? ")
        
        print("📌 Note: Ensure you have the images ready. ")
        
        img_path = os.path.join(os.path.dirname(sys.argv[1]), "i_" + re.search(r'_(\d+)', os.path.basename(sys.argv[1])).group(1))
        
        if not os.path.isdir(img_path):
            img_path = get_image_path_with_hinting("📁 Couldn't find the images directory🥺 Tell me, where should I look for images? ", verify=True)

        print(f"✨ Creating a quiz, storing in 🗂️ {filename}.")
        for i in range(3, 0, -1):
            print(f"\r🎉 Let the crafting begin in {i}... 🎉", end="", flush=True)
            time.sleep(1)

        try:
            app = QuizCreator(filename, img_path=img_path)
            app.run()
        except KeyboardInterrupt:
            pass

    except KeyboardInterrupt:
        pass



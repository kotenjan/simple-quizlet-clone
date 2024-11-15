import os
import time
import re
import colorama
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter
import cv2
from time import sleep
import sys

class Question:
    def __init__(self, image_question, image_answer):
        self.image_question = image_question
        self.image_answer = image_answer
        
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
        self.images = sorted([img for img in os.listdir(self.img_path) if img.endswith('.png')])
        self.questions = []
            
    def select_image(self):

        img_path = os.path.join(self.img_path, self.images[self.img_index])
        
        self.img_index = self.img_index + 1
        
        return img_path
            
    def add_question(self):

        question = Question(None, None)

        question.image_question = self.select_image()
        
        question.image_answer = self.select_image()

        return question

    def run(self):
        while len(self.images) > self.img_index:
            question = self.add_question()
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
        
        if not os.path.isdir(os.path.dirname(filename)):
            filename = get_filename_with_hinting("📁 Couldn't find the questions directory🥺 Tell me, where do you wish to store your questions? ")
        
        img_path = os.path.join(os.path.dirname(sys.argv[1]), "i_" + re.search(r'_(\d+)', os.path.basename(sys.argv[1])).group(1))
        
        if not os.path.isdir(img_path):
            img_path = get_image_path_with_hinting("📁 Couldn't find the images directory🥺 Tell me, where should I look for images? ", verify=True)

        try:
            app = QuizCreator(filename, img_path=img_path)
            app.run()
        except KeyboardInterrupt:
            pass

    except KeyboardInterrupt:
        pass



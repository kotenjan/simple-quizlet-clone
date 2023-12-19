import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sys
import textwrap
import random
import argparse

class QuestionApp(tk.Tk):
    def __init__(self, directory, steps, shuffle):
        super().__init__()
        self.title(f"Question App [{directory}*]")
        self.geometry("1600x900")
        self.configure(bg='#2E2E2E')
        self.questions_answers = []
        self.steps = steps
        self.shuffle = shuffle
        self.directory = directory
        self._load_questions(f"{directory}q.txt")
        self.current_index = 0
        self.img_label = None
        self.showing_answer = False
        self._setup_ui()
        self.show_question()
        
    def quit(self, event=None):
        super().quit()

    def _load_questions(self, question_file):
        with open(question_file, 'r') as file:
            content = file.read()
            qa_pairs = content.split('\n\n')

            for pair in qa_pairs:
                if pair.strip():  # Check if the pair is not empty
                    last_semicolon_index = pair.rfind(';')
                    q = pair[:last_semicolon_index].strip()
                    a = pair[last_semicolon_index + 1:].strip()
                    self.questions_answers.append((q, a))

        if self.shuffle:
            random.shuffle(self.questions_answers)


    def show_question(self):
        max_line_length = 80
        if self.current_index < len(self.questions_answers):
            question = self.questions_answers[self.current_index][0]
            
            if '\n' in question:
                wrapped_text = "\n".join([self.split_text(line, max_line_length) for line in question.split('\n')])
            else:
                wrapped_text = self.split_text(question, max_line_length)

            question_var.set(f"{self.current_index + 1}/{len(self.questions_answers)} {wrapped_text}")
            result_var.set('')
            if self.img_label:
                self.img_label.pack_forget()
            self.showing_answer = False
        else:
            question_var.set('No more questions!')
            result_var.set("")


    def split_text(self, text, max_line_length):
        return "\n".join(textwrap.wrap(text, max_line_length))

    def display_answer(self):
        answer = self.questions_answers[self.current_index][1]
        max_width = 1000  
        max_height = 800  
        max_line_length = 100  # You might adjust this value

        if answer.lower().endswith(".png"):
            if self.img_label:
                self.img_label.pack_forget()
            
            with Image.open(f"{self.directory}{answer}") as img:
                if img.width > max_width or img.height > max_height:
                    scale = min(max_width/img.width, max_height/img.height)
                    new_width = int(img.width * scale)
                    new_height = int(img.height * scale)
                    img = img.resize((new_width, new_height))
                photo = ImageTk.PhotoImage(img)
            
            self.img_label = ttk.Label(self, image=photo)
            self.img_label.photo = photo  
            self.img_label.pack(pady=20)
        else:
            wrapped_text = "\n".join([self.split_text(line, max_line_length) for line in answer.split('\n')])
            result_var.set(wrapped_text)
            if self.img_label:
                self.img_label.pack_forget()

        self.showing_answer = True

    def on_enter_pressed(self, event=None):
        if self.showing_answer:
            self.ok_clicked()
        else:
            self.display_answer()
            
    def on_backspace_pressed(self, event=None):
        if self.showing_answer:
            self.try_again_clicked()
        else:
            self.display_answer()

    def ok_clicked(self):
        # Hide labels
        self.question_label.pack_forget()
        self.result_label.pack_forget()
        if self.img_label:
            self.img_label.pack_forget()

        self.configure(bg='green')
        self.after(200, self._post_ok_click)

    def _post_ok_click(self):
        self.configure(bg='#2E2E2E')
        # Show labels
        self.question_label.pack(pady=30)
        self.result_label.pack(pady=20)

        self.current_index += 1
        self.show_question()

    def try_again_clicked(self):
        # Hide labels
        self.question_label.pack_forget()
        self.result_label.pack_forget()
        if self.img_label:
            self.img_label.pack_forget()

        self.configure(bg='red')
        self.after(200, self._post_try_again_click)

    def _post_try_again_click(self):
        self.configure(bg='#2E2E2E')
        # Show labels
        self.question_label.pack(pady=30)
        self.result_label.pack(pady=20)

        if self.current_index + self.steps < len(self.questions_answers):
            self.questions_answers.insert(self.current_index + self.steps, self.questions_answers[self.current_index])
        elif self.current_index < len(self.questions_answers):
            self.questions_answers.append(self.questions_answers[self.current_index])
        
        self.current_index += 1
        self.show_question()
        
    def prev_question(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.show_question()

    def on_left_arrow_pressed(self, event=None):
        if not self.showing_answer:
            self.prev_question()

    def _setup_ui(self):
        style = ttk.Style(self)
        style.configure('TButton', font=('Arial', 18, 'bold'), padding=10, background='#505050', foreground='white')
        style.configure('TLabel', foreground="white", background="#2E2E2E", font=("Arial", 24))
        style.configure('Question.TLabel', foreground="white", background="#2E2E2E", font=("Arial", 28))
        style.configure('Answer.TLabel', foreground="white", background="#2E2E2E", font=("Arial", 18))

        style.map('TButton', background=[('active', '#707070'), ('disabled', '#404040')], foreground=[('disabled', '#A0A0A0')])

        global question_var, result_var, ok_btn, try_again_btn
        
        question_var = tk.StringVar(self)
        result_var = tk.StringVar(self)
        
        self.question_label = ttk.Label(self, textvariable=question_var, style='Question.TLabel')
        self.question_label.pack(pady=30)

        self.result_label = ttk.Label(self, textvariable=result_var, style='Answer.TLabel')
        self.result_label.pack(pady=20)

        self.bind('<Return>', self.on_enter_pressed)
        self.bind('<BackSpace>', self.on_backspace_pressed)
        self.bind('<Escape>', self.quit)
        self.bind('<Left>', self.on_left_arrow_pressed)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple quiz app")
    parser.add_argument("filename", help="The filename of the question file")
    parser.add_argument("-s", "--shuffle", help="Shuffle questions", action="store_true")
    parser.add_argument("-t", "--steps", type=int, help="Number of steps/questions", default=5)

    args = parser.parse_args()
    path = args.filename if args.filename.endswith("/") else args.filename + "/"
    
    app = QuestionApp(path, steps=args.steps, shuffle=args.shuffle)
    app.mainloop()

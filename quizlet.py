import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

questions_answers = []

with open('questions.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        q, a = line.strip().split(';')
        questions_answers.append((q, a))

current_index = 0
img_label = None
showing_answer = False

def show_question():
    global current_index, img_label, showing_answer
    if current_index < len(questions_answers):
        question_var.set(questions_answers[current_index][0])
        result_var.set('')
        if img_label:
            img_label.pack_forget()
        showing_answer = False
    else:
        question_var.set('No more questions!')
        ok_btn.config(state=tk.DISABLED)
        try_again_btn.config(state=tk.DISABLED)
        result_var.set("")

def display_answer():
    global img_label, showing_answer
    answer = questions_answers[current_index][1]
    max_width = 1000  
    max_height = 800  

    if answer.lower().endswith(".png"):
        if img_label:
            img_label.pack_forget()
        
        with Image.open(answer) as img:
            if img.width > max_width or img.height > max_height:
                scale = min(max_width/img.width, max_height/img.height)
                new_width = int(img.width * scale)
                new_height = int(img.height * scale)
                img = img.resize((new_width, new_height))
            photo = ImageTk.PhotoImage(img)
        
        img_label = ttk.Label(root, image=photo)
        img_label.photo = photo  
        img_label.pack(pady=20)
    else:
        result_var.set(answer)
        if img_label:
            img_label.pack_forget()

    showing_answer = True

def on_enter_pressed(event=None):
    global current_index, showing_answer
    if showing_answer:
        ok_clicked()
    else:
        display_answer()

def ok_clicked():
    global current_index
    current_index += 1
    show_question()

def try_again_clicked():
    global current_index
    if current_index + 10 < len(questions_answers):
        questions_answers.insert(current_index + 10, questions_answers[current_index])
    else:
        questions_answers.append(questions_answers[current_index])
    ok_clicked()

root = tk.Tk()
root.title("Question App")
root.geometry("1600x900")
root.configure(bg='#2E2E2E')

style = ttk.Style(root)
style.configure('TButton', font=('Arial', 18, 'bold'), padding=10, background='#505050', foreground='white')
style.configure('TLabel', foreground="white", background="#2E2E2E", font=("Arial", 24))  # Increase font size here
# Configure styles
style.configure('Question.TLabel', foreground="white", background="#2E2E2E", font=("Arial", 28))  # Larger font for questions
style.configure('Answer.TLabel', foreground="white", background="#2E2E2E", font=("Arial", 18))  # Smaller font for answers

# Applying styles
style.map('TButton', background=[('active', '#707070'), ('disabled', '#404040')], foreground=[('disabled', '#A0A0A0')])

question_var = tk.StringVar(root)
ttk.Label(root, textvariable=question_var, style='Question.TLabel').pack(pady=30)

result_var = tk.StringVar(root)
ttk.Label(root, textvariable=result_var, style='Answer.TLabel').pack(pady=20)

button_frame = tk.Frame(root, bg='#2E2E2E')
button_frame.pack(side=tk.BOTTOM, pady=20)

ok_btn = ttk.Button(button_frame, text="OK", command=ok_clicked, state=tk.NORMAL)
ok_btn.pack(side=tk.LEFT, padx=50)

try_again_btn = ttk.Button(button_frame, text="Try Again", command=try_again_clicked, state=tk.NORMAL)
try_again_btn.pack(side=tk.RIGHT, padx=50)

root.bind('<Return>', on_enter_pressed)

show_question()

root.mainloop()

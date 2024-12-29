from flask import Flask, render_template, request, redirect, url_for, session, jsonify, send_from_directory
import os
import json
import threading
import random
import webbrowser
import signal
import sys
import requests

app = Flask(__name__)
app.secret_key = 'secret_key'
DATA_DIR = './DATA'

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    if 'quiz_questions' not in session:
        return redirect(url_for('index'))
    return render_template('quiz.html')

@app.route('/start_quiz', methods=['POST'])
def start_quiz():
    quiz_file = os.path.join("DATA", request.form.getlist('files')[0], "quiz.json")
    session["shuffle"] = request.form.get('shuffle_questions') == 'true'
    session["reset_progress"] = request.form.get('reset_progress') == 'true'
    session["repeat_after"] = int(request.form.get('repeat_interval', 1))
    session["quiz_path"] = quiz_file
    with open(quiz_file, 'r', encoding="utf-8") as f:
        quiz_data = json.load(f)

    if session["reset_progress"]:
        for i in range(len(quiz_data)):
            quiz_data[i]["correct"] = 0
            quiz_data[i]["incorrect"] = 0

    if session["shuffle"]:

        random.shuffle(quiz_data)

        quiz_data = sorted(
            quiz_data,
            key=lambda question: 0 if question["correct"] == 0 and question["incorrect"] == 0 else max(1, question["correct"] - question["incorrect"])
        )

    session['quiz_questions'] = quiz_data
    session['question_index'] = 0
    return redirect(url_for('quiz'))

@app.route('/quiz/get_card')
def get_card():
    
    if 'quiz_questions' not in session:
        return jsonify({'error': 'Quiz is NOT Loaded.'}), 400
    
    index = session.get('question_index', 0)

    quiz_questions = session['quiz_questions']
    if index >= len(quiz_questions):
        return jsonify({'error': 'You have reached the end of the quiz. Congrats! 🥳'}), 400
    
    index = session.get('question_index', 0)
    quiz_questions = session['quiz_questions']
    card = quiz_questions[index]
    return jsonify({'question': card["question"], "answer": card["answer"], "question_n": index+1, "questions_total": len(quiz_questions), "questions_left": len(quiz_questions) - (index+1)})

@app.route('/quiz/mark', methods=['POST'])
def mark():

    def save_quiz(quiz):
        elements = set()
        questions_to_save = []

        for element in quiz[::-1]: # last copy of element has correct/incorrect with current state
            if element["question"] not in elements: # keep only first instance of element
                elements.add(element["question"])
                questions_to_save.append(element)

        with open(session["quiz_path"], "w", encoding="utf-8") as f:
            json.dump(questions_to_save[::-1], f) # reverse back to get original order

    data = request.get_json()
    action = data.get('action')
    if 'quiz_questions' not in session:
        return jsonify({'error': 'Quiz is NOT Loaded.'}), 400
    
    index = session.get('question_index', 0)
    
    quiz_questions = session['quiz_questions']
    
    if index >= len(quiz_questions):
        return jsonify({'error': 'You have reached the end of the quiz. Congrats! 🥳'}), 400
    
    if action == 'correct':
        quiz_questions[index]['correct'] += 1
        save_quiz(quiz_questions)
        session['question_index'] = min(index + 1, len(quiz_questions) - 1)
    
    elif action == 'incorrect':
        quiz_questions[index]['incorrect'] += 1
        save_quiz(quiz_questions)
        session['question_index'] = min(index + 1, len(quiz_questions) - 1)

        insert_position = min(index + session["repeat_after"], len(quiz_questions))
        quiz_questions.insert(insert_position, quiz_questions[index])

    session['quiz_questions'] = quiz_questions
    
    index = session.get('question_index', 0)
    quiz_questions = session['quiz_questions']
    card = quiz_questions[index]
    return jsonify({'question': card["question"], "answer": card["answer"], "question_n": index+1, "questions_total": len(quiz_questions), "questions_left": len(quiz_questions) - (index+1)})

@app.route('/quiz/move', methods=['POST'])
def move():
    data = request.get_json()
    direction = data.get('direction')
    if 'quiz_questions' not in session:
        return jsonify({'error': 'Quiz is NOT Loaded.'}), 400
    
    index = session.get('question_index', 0)
    
    if direction == 'next':
        session['question_index'] = min(index + 1, len(session['quiz_questions']) - 1)
    
    elif direction == 'prev':
        session['question_index'] = max(index - 1, 0)
    
    quiz_questions = session['quiz_questions']
    
    index = session.get('question_index', 0)
    quiz_questions = session['quiz_questions']
    card = quiz_questions[index]
    return jsonify({'question': card["question"], "answer": card["answer"], "question_n": index+1, "questions_total": len(quiz_questions), "questions_left": len(quiz_questions) - (index+1)})

@app.route('/DATA/<path:filename>')
def data_files(filename):
    return send_from_directory('DATA', filename)

@app.route('/fetch_data', methods=['GET'])
def fetch_data():
    path = request.args.get('path', '.')
    abs_path = os.path.join(DATA_DIR, os.path.normpath(path.lstrip('/')))
    if not abs_path.startswith(DATA_DIR):
        return jsonify([])  # Prevent accessing paths outside of DATA_DIR
    try:
        entries = []
        for entry in os.scandir(abs_path):
            if entry.is_dir():
                # Check if the directory contains "quiz.json"
                if "quiz.json" in os.listdir(entry.path):
                    entries.append({
                        'name': entry.name,
                        'type': 'file'  # Treat directory as a file
                    })
                else:
                    entries.append({
                        'name': entry.name,
                        'type': 'dir'
                    })
            else:
                entries.append({
                    'name': entry.name,
                    'type': 'file'
                })
        return jsonify(entries)
    except Exception as e:
        return jsonify([])

# Route to serve the create.html page
@app.route('/create_quiz', methods=['GET'])
def create_quiz_page():
    return render_template('create.html')

# Route to handle quiz creation
@app.route('/create_quiz', methods=['POST'])
def create_quiz():

    def group_into_pairs(elements):
        result = []
        for i in range(0, len(elements), 2):
            if i + 1 < len(elements):
                pair = {
                    "question": os.path.join(quiz_images_folder, elements[i].filename),
                    "answer": os.path.join(quiz_images_folder, elements[i + 1].filename),
                    "correct": 0,
                    "incorrect": 0
                }
                result.append(pair)
        return result
    
    quiz_name = request.form.get('quiz_name')
    files = request.files.getlist('files[]')

    if not quiz_name or not files:
        return jsonify({"error": "Quiz name and files are required."}), 400

    try:
        quiz_images_folder = os.path.join("DATA", quiz_name, "images")
        quiz_path = os.path.join("DATA", quiz_name, "quiz.json")

        os.makedirs(quiz_images_folder, exist_ok=True)

        for file in files:
            file.save(os.path.join(quiz_images_folder, file.filename))
        
        quiz = group_into_pairs(files)

        print(quiz)

        with open(quiz_path, "w", encoding="utf-8") as f:
            json.dump(quiz, f)

        return jsonify({"message": f"Quiz created successfully in {quiz_images_folder}"}), 200

    except Exception as e:
        print(str(e))
        return jsonify({"error": str(e)}), 500

def open_browser():
    webbrowser.open("http://127.0.0.1:5000")

def shutdown_server():
    os._exit(0)

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

def handle_exit(signal, frame):
    requests.post('http://127.0.0.1:5000/shutdown')
    sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, handle_exit)
    signal.signal(signal.SIGTERM, handle_exit)
    threading.Timer(1, open_browser).start()
    app.run()

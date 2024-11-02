import random
import sys

def load_and_shuffle_questions(input_path, output_path):
    
    with open(input_path, 'r', encoding='utf-8') as file:
        data = file.read()
    
    # Split data into individual questions
    questions = data.split("###")[1:]
    processed_questions = []

    for question_index, question in enumerate(questions):
        question_parts = [x for x in question.split("\n\n") if x != ""]
        
        if len(question_parts) != 3:
            print(len(question_parts))
            for x in question_parts:
                print()
                print(x)

        _, question_text, options = question_parts
        options = [x[5:] for x in options.split("\n") if x != ""]

        # Identify correct answer and remove '*'
        for i, option in enumerate(options):
            if '*' in option[-1]:
                correct_answer_text = option[:-1]
                options[i] = correct_answer_text

        # Shuffle options
        shuffled_options = options[:]
        random.shuffle(shuffled_options)

        # Format and store the processed question
        formatted_question = f"Otázka {question_index + 1}\n\n{question_text}\n\n" + "\n".join(" - " + opt for i, opt in enumerate(shuffled_options)) + "\n\nSprávná Odpověď:\n" + correct_answer_text
        processed_questions.append(formatted_question)

    # Join all questions into final output format
    output = "\n\n".join(processed_questions)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(output)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        load_and_shuffle_questions(input_file, output_file)

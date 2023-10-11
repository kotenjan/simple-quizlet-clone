# QuestionApp

## Description
A simple quiz app built using Tkinter in Python.

## Input Requirements

### Question File
1. Place a text file named `q.txt` in a directory.
2. Each line in the file should contain a question and an answer separated by a semicolon (`;`).

### Command-Line Arguments
- `filename`: The directory containing `q.txt`.
- `-s` or `--shuffle`: Optional flag to shuffle questions.
- `-t` or `--steps`: Optional, sets the number of steps/questions. Default is 5. If user flags question as incorrect it will be repeated in -t steps.

## Controls
- `Enter`: Show answer or move to next question.
- `Backspace`: Show answer or mark question for review.
- `Escape`: Quit the app.

## Example Usage
```python your_script_name.py your_directory -s -t 10```

# PNG to q.txt Generator

## Description
A Python script to generate a `q.txt` file from `.png` image files in a specified directory.

## Input Requirement

### Command-Line Argument
- `directory_path`: Path to the directory containing `.png` files.

## Example Usage
`python your_script.py /path/to/directory`

## Output
A file named `q.txt` will be generated in the specified directory. This file will contain the image names and corresponding `.png` filenames, separated by a semicolon (`;`).

# simple-quizlet-clone
### image_2_question.py - creates a textfile q.txt for the quizlet.py where question textfield is the file name. The app will show the image instead of answer text.
### quizlet.py - Enter for correct answers. Backspace for incorrect answers. If user flags answer as incorrect, it will be repeated after <steps=5> questions.

Input for this app:

A text file (q.txt) in a directory. Each line contains a question and answer separated by a semicolon.
Command-line arguments:
filename: The directory containing q.txt.
-s or --shuffle: Optional flag to shuffle questions.
-t or --steps: Optional, number of steps/questions. Default is 5.

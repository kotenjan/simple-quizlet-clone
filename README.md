# Ultimate Quiz Project

![Quiz Project Banner](https://your-image-url.com/banner.png)

Welcome to the **Ultimate Quiz Project**! This project provides a comprehensive solution for creating, managing, and running image-based quizzes. Whether you're an educator, content creator, or just someone who loves quizzes, this project offers tools to enhance your quiz experience.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [1. Image Merger](#1-image-merger)
  - [2. Quiz Creator](#2-quiz-creator)
  - [3. Quiz App](#3-quiz-app)
- [Configuration](#configuration)
- [Dependencies](#dependencies)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Image Merging**: Seamlessly merge the last two PNG images in a directory either horizontally or vertically.
- **Quiz Creation**: Easily create quizzes by pairing question and answer images.
- **Interactive Quiz Application**: Run interactive quizzes with support for images, hints, correct/incorrect answers tracking, and statistics.
- **User-Friendly Interface**: Utilize command-line prompts with autocomplete for a smooth user experience.
- **Statistics Tracking**: Keep track of your performance and revisit missed questions based on your preferences.
- **Customization**: Configure various aspects like shuffle options, repeat intervals, and more to tailor the quiz to your needs.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/ultimate-quiz-project.git
   cd ultimate-quiz-project
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

The project consists of three main components:

1. **Image Merger**
2. **Quiz Creator**
3. **Quiz App**

### 1. Image Merger

Merge the last two PNG images in a specified directory either horizontally or vertically.

**Usage:**

```bash
python image_merger.py [orientation]
```

**Arguments:**

- `orientation` (optional): Choose `v` for vertical merge or `h` for horizontal merge. Default is `v`.

**Example:**

```bash
python image_merger.py h
```

This command merges the last two PNG images in the default directory horizontally.

**Default Directory:**

```python
dir_path = "/mnt/c/Users/koten/Pictures/Screenshots"
```

You can modify the `dir_path` in the script to point to your desired directory.

### 2. Quiz Creator

Create a quiz by pairing question and answer images. The Quiz Creator will generate a formatted question file based on your image pairs.

**Usage:**

```bash
python quiz_creator.py <output_filename>
```

**Example:**

```bash
python quiz_creator.py my_quiz.txt
```

This command creates a quiz file named `my_quiz.txt` by pairing images from the default image directory.

**Default Image Directory:**

The script looks for images in a directory derived from the output filename. For example, if your output file is `my_quiz.txt`, it looks for images in `i_<number>`, where `<number>` is extracted from the filename.

You can specify a different image directory by modifying the script or using prompt inputs when running.

### 3. Quiz App

Run the interactive quiz based on the questions you've created. The Quiz App supports images, hints, answer tracking, and statistics.

**Usage:**

```bash
python quiz_app.py
```

Upon running, the app will prompt you for:

- **Question File**: The name of the question file (e.g., `my_quiz.txt`).
- **Shuffle Options**: Whether to shuffle the questions.
- **Repeat Interval**: How often to revisit missed questions.

**Interactive Controls:**

- **Any Key**: Show the answer.
- **'a'**: Mark the answer as incorrect.
- **'d'**: Mark the answer as correct.
- **'w'**: Go back to the previous question.
- **'q'**: Quit the quiz.

**Example:**

```bash
python quiz_app.py
```

Follow the on-screen prompts to start your quiz session.

## Configuration

You can customize various aspects of the project:

- **Directories**: Modify the `dir_path` in `image_merger.py` and `quiz_creator.py` to point to your desired directories for images and questions.
- **Statistics File**: The Quiz App generates a statistics file (`*_stats.json`) to track your performance.
- **Phrase Files**: Customize response phrases by editing files in the `phrases` directory, such as `incorrect_answers.txt`, `correct_answers.txt`, and `end_of_quiz.txt`.

## Dependencies

Ensure you have the following dependencies installed. They are listed in `requirements.txt` and can be installed via `pip`.

- Python 3.6+
- [Pillow](https://python-pillow.org/) (`PIL`)
- [OpenCV](https://opencv.org/) (`cv2`)
- [NumPy](https://numpy.org/)
- [Colorama](https://pypi.org/project/colorama/)
- [Prompt Toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) (usually included with Python)

**Install Dependencies:**

```bash
pip install -r requirements.txt
```

**`requirements.txt`:**

```plaintext
Pillow
opencv-python
numpy
colorama
prompt-toolkit
```

## Examples

### Merging Images Horizontally

```bash
python image_merger.py h
```

This command will merge the last two PNG images in the specified directory horizontally and display the merged image. If you press 'q' or 'ESC', the merging process will be aborted.

### Creating a Quiz

```bash
python quiz_creator.py geography_quiz.txt
```

This command will create a `geography_quiz.txt` file by pairing question and answer images from the designated image directory.

### Running the Quiz App

```bash
python quiz_app.py
```

Follow the interactive prompts to select your quiz file, shuffle preferences, and repeat intervals. Engage with the quiz using the keyboard controls to navigate through questions, mark answers, and track your performance.

## Contributing

We welcome contributions! Whether it's improving documentation, adding new features, or fixing bugs, your help is appreciated.

1. **Fork the Repository**
2. **Create a Feature Branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m "Add your feature"
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

Please ensure your code follows the project's coding standards and includes appropriate documentation.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this project as per the terms of the license.

---

*Happy Quizzing! 🎉*

For any questions or support, please open an issue on the [GitHub repository](https://github.com/yourusername/ultimate-quiz-project/issues).
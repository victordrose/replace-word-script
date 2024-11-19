# Text Replacement Script

This project is a Python-based script that processes files in a directory, detects text content, and replaces specific words with generic alternatives based on a predefined dictionary. It is designed for portability and ease of use.

## Features

- Processes multiple file formats (e.g., `.txt`, `.java`, `.yaml`, etc.) in a folder.
- Skips empty or non-text files automatically.
- Performs case-insensitive word replacements.
- Dynamically detects the project folder and input files for easy portability.
- Creates the input folder if it doesn't exist.

## How to Use

1. **Clone the Repository**:
   ```
   git clone https://github.com/victordrose/replace-word-script
   cd replace-word-script
    ```

2. **Run the Script**:

    ```
    py gptsafe.py
    ```

3. **Check the Output**:

    The script will modify the files in place, replacing the specified words.

## Configuration
Update the word_replacements dictionary in the script to define custom words and their replacements:

    word_replacements = {
        "password": "REDACTED",
        "secret": "REDACTED",
        "username": "USER",
        "email": "EMAIL",
    }

## Requirements
    Python 3.6 or higher.

## Project Structure

    project-folder/
    │
    ├── inputs/                # Directory for input files
    ├── script_name.py         # Main Python script
    └── README.md              # Project documentation
## Example
For an input file named input.txt with the content:

        username: admin
        password: 12345 
        email: admin@example.com

After running the script, the content will be:

        username: USER
        password: REDACTED
        email: EMAIL

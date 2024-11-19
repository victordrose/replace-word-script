import os
import re

# Determine the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the relative folder containing the files
folder_path = os.path.join(script_dir, "input") 

# Dictionary of words to replace and their generic replacements
word_replacements = {
    "password": "REDACTED",
    "secret": "REDACTED",
    "username": "USER",
    "email": "EMAIL",
    # Add more words as needed
}

def replace_words_in_file(input_path, replacements):
    """
    Reads a file, performs word replacements, and saves the result back to the same file.
    """
    try:
        # Read the content of the file
        with open(input_path, "r", encoding="utf-8") as file:
            content = file.read()

        # Perform replacements
        for word, replacement in replacements.items():
            content = re.sub(rf"\b{word}\b", replacement, content, flags=re.IGNORECASE)

        # Write the modified content back to the file
        with open(input_path, "w", encoding="utf-8") as file:
            file.write(content)

        print(f"Replacements completed in: {input_path}")
    except Exception as e:
        print(f"An error occurred while processing {input_path}: {e}")

def process_files_in_folder(folder_path, replacements):
    """
    Processes all files in the given folder. Only processes files with text content.
    """
    for filename in os.listdir(folder_path):
        # Build the full file path
        file_path = os.path.join(folder_path, filename)

        # Skip directories, only process files
        if os.path.isfile(file_path):
            try:
                # Check if the file contains text
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()

                # If content exists, process the file
                if content.strip():  # Ensure it's not an empty file
                    print(f"Processing file: {filename}")
                    replace_words_in_file(file_path, replacements)
                else:
                    print(f"Skipping empty file: {filename}")

            except UnicodeDecodeError:
                print(f"Skipping non-text file: {filename}")
            except Exception as e:
                print(f"Error reading file {filename}: {e}")

if __name__ == "__main__":
    if os.path.exists(folder_path):
        process_files_in_folder(folder_path, word_replacements)
    else:
        print(f"The folder {folder_path} does not exist.")

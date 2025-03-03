"""
Process a text file to count occurrences of the word "Romeo" and save the result.
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = "data"
processed_folder_name: str = "data_processed"

#####################################
# Define Functions
#####################################

def count_word_occurrences(file_path: pathlib.Path, word: str) -> int:
    """Count the occurrences of a specific word in a text file (case-insensitive)."""
    try:
        with file_path.open('r') as file:
            content: str = file.read()
            return content.lower().count(word.lower())
    except Exception as e:
        logger.error(f"Error reading text file: {e}")
        return 0

def process_text_file():
    """Read a text file, count occurrences of 'Harry', and save the result."""


    input_file = pathlib.Path(fetched_folder_name, "C:\Projects\datafun-03-project\data\harry_potter.txt")
    output_file = pathlib.Path("C:\Projects\datafun-03-project\data_processed", "Harry.txt")


    word_to_count: str = "Harry"
    word_count: int = count_word_occurrences(input_file, word_to_count)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open('w') as file:
        file.write(f"Occurrences of '{word_to_count}': {word_count}\n")
    logger.info(f"Processed text file: {input_file}, Word count saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting text processing...")
    process_text_file()
    logger.info("Text processing complete.")
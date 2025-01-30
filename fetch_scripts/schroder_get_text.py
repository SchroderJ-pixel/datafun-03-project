import pathlib
import requests
from utils_logger import logger

# Declare the folder to be outside fetch_scripts
fetched_folder_name = pathlib.Path(__file__).resolve().parent.parent.joinpath("data")  # Moves the data folder outside

def fetch_text_file(folder_name: str, filename: str, url: str) -> None:
    """
    Fetch text data from the given URL and write it to a file.

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        url (str): URL of the text file to fetch.

    Returns:
        None
    """
    if not url:
        logger.error("The URL provided is empty. Please provide a valid URL.")
        return

    try:
        logger.info(f"Fetching text data from {url}...")
        response = requests.get(url)
        response.raise_for_status()  # Check for any errors
        write_text_file(folder_name, filename, response.text)
        logger.info(f"SUCCESS: Text file fetched and saved as {filename}")
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request error occurred: {req_err}")

def write_text_file(folder_name: str, filename: str, string_data: str) -> None:
    """
    Write text data to a file with UTF-8 encoding.

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        string_data (str): Text content as a string.

    Returns:
        None
    """
    file_path = folder_name.joinpath(filename)
    try:
        logger.info(f"Writing text data to {file_path}...")
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('w', encoding='utf-8') as file:  # Use utf-8 encoding
            file.write(string_data)
        logger.info(f"SUCCESS: Text data written to {file_path}")
    except IOError as io_err:
        logger.error(f"Error writing text data to {file_path}: {io_err}")

def main():
    """
    Main function to demonstrate fetching text data.
    """
    text_url = "https://github.com/amephraim/nlp/raw/master/texts/J.%20K.%20Rowling%20-%20Harry%20Potter%201%20-%20Sorcerer's%20Stone.txt"
    logger.info("Starting text fetch demonstration...")
    fetch_text_file(fetched_folder_name, "harry_potter.txt", text_url)

if __name__ == '__main__':
    main()

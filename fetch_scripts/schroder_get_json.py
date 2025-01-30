import pathlib
import requests
import json  # This should be at the top
from utils_logger import logger

# Declare the folder to be outside fetch_scripts
fetched_folder_name = pathlib.Path(__file__).resolve().parent.parent.joinpath("data")  # Moves the data folder outside

def fetch_json_file(folder_name: str, filename: str, url: str) -> None:
    """
    Fetch JSON data from the given URL and write it to a file.

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        url (str): URL of the JSON file to fetch.

    Returns:
        None
    """
    if not url:
        logger.error("The URL provided is empty. Please provide a valid URL.")
        return

    try:
        logger.info(f"Fetching JSON data from {url}...")
        response = requests.get(url)
        response.raise_for_status()  # Check for any errors
        write_json_file(folder_name, filename, response.json())  # Use .json() to parse the content
        logger.info(f"SUCCESS: JSON file fetched and saved as {filename}")
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request error occurred: {req_err}")

def write_json_file(folder_name: str, filename: str, json_data: dict) -> None:
    """
    Write JSON data to a file.

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        json_data (dict): JSON content to write.

    Returns:
        None
    """
    file_path = folder_name.joinpath(filename)
    try:
        logger.info(f"Writing JSON data to {file_path}...")
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('w', encoding='utf-8') as file:  # Use utf-8 encoding
            json.dump(json_data, file, ensure_ascii=False, indent=4)
        logger.info(f"SUCCESS: JSON data written to {file_path}")
    except IOError as io_err:
        logger.error(f"Error writing JSON data to {file_path}: {io_err}")

def main():
    """
    Main function to demonstrate fetching JSON data.
    """
    json_url = "https://github.com/olitreadwell/pokemon-classic-json/raw/main/pokedex.json"
    logger.info("Starting JSON fetch demonstration...")
    fetch_json_file(fetched_folder_name, "pokedex.json", json_url)

if __name__ == '__main__':
    main()


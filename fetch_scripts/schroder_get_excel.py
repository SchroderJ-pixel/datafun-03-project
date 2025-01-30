import pathlib
import requests
from utils_logger import logger

# Declare the folder to be outside fetch_scripts
fetched_folder_name = pathlib.Path(__file__).resolve().parent.parent.joinpath("data")  # Moves the data folder outside

def fetch_excel_file(folder_name: str, filename: str, url: str) -> None:
    """
    Fetch Excel data from the given URL and write it to a file.

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        url (str): URL of the Excel file to fetch.

    Returns:
        None
    """
    if not url:
        logger.error("The URL provided is empty. Please provide a valid URL.")
        return

    try:
        logger.info(f"Fetching Excel data from {url}...")
        response = requests.get(url)
        response.raise_for_status()  # Check for any errors
        write_excel_file(folder_name, filename, response.content)
        logger.info(f"SUCCESS: Excel file fetched and saved as {filename}")
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request error occurred: {req_err}")

def write_excel_file(folder_name: str, filename: str, file_data: bytes) -> None:
    """
    Write Excel data to a file.

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        file_data (bytes): The binary content of the Excel file.

    Returns:
        None
    """
    file_path = folder_name.joinpath(filename)
    try:
        logger.info(f"Writing Excel data to {file_path}...")
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('wb') as file:  # Write in binary mode
            file.write(file_data)
        logger.info(f"SUCCESS: Excel data written to {file_path}")
    except IOError as io_err:
        logger.error(f"Error writing Excel data to {file_path}: {io_err}")

def main():
    """
    Main function to demonstrate fetching Excel data.
    """
    excel_url = "https://github.com/shadsluiter/ExcelExamples/raw/master/Cell%20Phone%20Plans%20compared.xlsx"
    logger.info("Starting Excel fetch demonstration...")
    fetch_excel_file(fetched_folder_name, "cell_phone_plans.xlsx", excel_url)

if __name__ == '__main__':
    main()

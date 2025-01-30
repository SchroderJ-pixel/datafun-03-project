import pathlib
import csv
import statistics
from utils_logger import logger

# Folder names
processed_folder_name: str = "data_processed"

def analyze_seals(file_path: pathlib.Path) -> dict:
    """Analyze the number of seals to calculate min, max, mean, and stdev."""
    try:
        seals_list = []
        with file_path.open('r') as file:
            dict_reader = csv.DictReader(file)
            for row in dict_reader:
                try:
                    seals = int(row["number_of_seals"])  # Extract number_of_seals and convert to int
                    seals_list.append(seals)
                except ValueError as e:
                    logger.warning(f"Skipping invalid row: {row} ({e})")

        if seals_list:
            stats = {
                "min": min(seals_list),
                "max": max(seals_list),
                "mean": statistics.mean(seals_list),
                "stdev": statistics.stdev(seals_list) if len(seals_list) > 1 else 0,
            }
            return stats
        else:
            logger.warning("No valid data in seals_list")
            return {}

    except Exception as e:
        logger.error(f"Error processing CSV file: {e}")
        return {}

def process_csv_file():
    """Read a CSV file, analyze seals, and save the results."""
    input_file = pathlib.Path("C:\\Projects\\datafun-03-project\\data\\arcticseals.csv")  # Corrected path
    output_file = pathlib.Path(processed_folder_name, "arcticseals_statistics.txt")
    
    stats = analyze_seals(input_file)

    if stats:
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with output_file.open('w') as file:
            file.write("Seal Count Statistics:\n")
            file.write(f"Minimum: {stats['min']}\n")
            file.write(f"Maximum: {stats['max']}\n")
            file.write(f"Mean: {stats['mean']}\n")
            file.write(f"Standard Deviation: {stats['stdev']}\n")

        logger.info(f"Processed CSV file: {input_file}, Statistics saved to: {output_file}")
    else:
        logger.error("No valid statistics to save.")

if __name__ == "__main__":
    logger.info("Starting CSV processing...")
    process_csv_file()
    logger.info("CSV processing complete.")

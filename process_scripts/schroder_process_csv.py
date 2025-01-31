
#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import csv
import statistics

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

def analyze_seal_data(file_path: pathlib.Path) -> dict:
    """Analyze Arctic seal data, specifically focusing on the 'number_of_seals' and 'species_confidence' columns."""
    try:
        # Initialize lists to store data
        seal_counts = []
        species_confidence = []
        with file_path.open('r') as file:
            dict_reader = csv.DictReader(file)  # Use DictReader for easy column access
            for row in dict_reader:
                try:
                    # Extract and convert the number of seals to an integer
                    seals = int(row["number_of_seals"])
                    seal_counts.append(seals)
                    
                    # Extract species confidence, assuming it's a float or can be converted
                    confidence = float(row["species_confidence"])
                    species_confidence.append(confidence)
                except ValueError as e:
                    logger.warning(f"Skipping invalid row: {row} ({e})")
        
        # Calculate statistics
        seal_stats = {
            "total_seals": sum(seal_counts),
            "avg_seal_count": statistics.mean(seal_counts) if seal_counts else 0,
            "avg_species_confidence": statistics.mean(species_confidence) if species_confidence else 0,
            "min_species_confidence": min(species_confidence) if species_confidence else 0,
            "max_species_confidence": max(species_confidence) if species_confidence else 0,
        }
        return seal_stats
        
    except Exception as e:
        logger.error(f"Error processing CSV file: {e}")
        return {}

def process_csv_file():
    """Read a CSV file, analyze Arctic seal data, and save the results."""
    input_file = pathlib.Path(fetched_folder_name, "articseals.csv")
    output_file = pathlib.Path(processed_folder_name, "seal_data_analysis.txt")
    
    # Perform the analysis
    seal_stats = analyze_seal_data(input_file)
    
    # Ensure the output directory exists
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Save the analysis results to a file
    with output_file.open('w') as file:
        file.write(f"Total number of seals: {seal_stats['total_seals']}\n")
        file.write(f"Average number of seals per entry: {seal_stats['avg_seal_count']}\n")
        file.write(f"Average species confidence: {seal_stats['avg_species_confidence']}\n")
        file.write(f"Minimum species confidence: {seal_stats['min_species_confidence']}\n")
        file.write(f"Maximum species confidence: {seal_stats['max_species_confidence']}\n")
    
    logger.info(f"Processed CSV file: {input_file}, Seal data analysis saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting Arctic seal data processing...")
    process_csv_file()
    logger.info("Arctic seal data processing complete.")
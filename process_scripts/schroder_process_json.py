#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import json

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

def count_pokemon_types(file_path: pathlib.Path) -> dict:
    """Count occurrences of each Pokémon type in the JSON file."""
    try:
        with file_path.open('r') as file:
            # Load JSON data into a Python dictionary
            data = json.load(file)
            
            # Initialize dictionary to store type counts
            type_counts = {}
            
            # Iterate through the Pokémon data
            for pokemon in data.get("pokemon", []):
                types = pokemon.get("type", [])
                for t in types:
                    type_counts[t] = type_counts.get(t, 0) + 1
                    
            return type_counts
    except Exception as e:
        logger.error(f"Error reading or processing JSON file: {e}")
        return {}

def process_json_file():
    """Read a JSON file, count Pokémon types, and save the result."""
    input_file = pathlib.Path(fetched_folder_name, "C:\Projects\datafun-03-project\data\pokedex.json")
    output_file = pathlib.Path("C:\Projects\datafun-03-project\data_processed", "pokemon_type_counts.txt")

    # Get type counts
    type_counts = count_pokemon_types(input_file)
    
    # Ensure the output folder exists
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Save results to a text file
    with output_file.open('w') as file:
        file.write("Pokémon Type Counts:\n")
        for type_, count in type_counts.items():
            file.write(f"{type_}: {count}\n")
    
    logger.info(f"Processed JSON file: {input_file}, Type counts saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")


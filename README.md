# datafun-03-project
Module 3 - Working with Data

## Setup Instructions

1. Clone the repository from GitHub:
   ```bash
   git clone https://github.com/SchroderJ-pixel/datafun-03-project

2. Set Terminal to project folder
    ```bash
    cd C:\Projects\datafun-03-project

Creat virtual environment py -m venv .venv
    py -m venv .venv

Activate virtual environment .venv\Scripts\activate
    .venv\Scripts\activate  # For Windows

Select virtual environment for Python interpreter Ctrl + Shift + P Python: Select Interpreter .venv

Update pip py -m pip install --upgrade pip setuptools wheel

Install dependencies py -m pip install -r requirements.txt

********

Save the example project to computer, then copy and paste the example_get files, example_process, and util_logger

********
Step 3:
This script (schroder_get_csv.py) fetches the ArcticSeals CSV file from GitHub and saves it to the data folder. The script performs the following actions:

    Fetches the CSV file from the specified GitHub URL.
    Saves the file as articseals.csv in the data folder, which is located outside the fetch_scripts directory.

This script (schroder_get_excel.py) fetches an Excel file containing cell phone plans from GitHub and saves it to the data folder. The script performs the following actions:

    Fetches the Excel file from the specified GitHub URL.
    Saves the file as cell_phone_plans.xlsx in the data folder, which is located outside the fetch_scripts directory.

This script (`schroder_get_json.py`) fetches the Pokémon Classic Pokedex JSON file from GitHub and saves it to the data folder. The script performs the following actions:

    Fetches the JSON file from the specified GitHub URL.
    Saves the file as `pokedex.json` in the data folder, which is located outside the fetch_scripts directory.


This script (`schroder_get_text.py`) fetches the Harry Potter text file from GitHub and saves it to the data folder. The script performs the following actions:

    Fetches the text file from the specified GitHub URL.
    Saves the file as `harry_potter.txt` in the data folder, which is located outside the fetch_scripts directory.
*******
Step 4:

Arctic Seals Data Processing
I processed the articseals.csv file to calculate the total number of seals and the average seals per entry.

Movie Cleaopatra Data Processing 
I processed the IMDB-Movie-Database.xlsx to find all the movies named Cleopatra.

Pokemon Type Data Processing:
I processed the podedex.json to count how many pokemon of each type are in Gen 1.

Harry Potter Data Processing:
I processed the harry_potter.txt to count how many times the word "Harry" is said in the text. 

Step 5: 
Update README.md







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
This script (schroder_get_csv.py) fetches the ArcticSeals CSV file from GitHub and saves it to the data folder. The script performs the following actions:

    Fetches the CSV file from the specified GitHub URL.
    Saves the file as articseals.csv in the data folder, which is located outside the fetch_scripts directory.

This script (schroder_get_excel.py) fetches an Excel file containing cell phone plans from GitHub and saves it to the data folder. The script performs the following actions:

    Fetches the Excel file from the specified GitHub URL.
    Saves the file as cell_phone_plans.xlsx in the data folder, which is located outside the fetch_scripts directory.





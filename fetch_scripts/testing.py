import requests

url = "https://www.google.com"  # Testing connection to Google

try:
    response = requests.get(url)
    print(f"Connection successful! Status Code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error connecting to {url}: {e}")

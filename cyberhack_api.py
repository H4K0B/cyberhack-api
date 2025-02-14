import os
import requests
import argparse

parser = argparse.ArgumentParser(description='Search for a domain or a emaiil using the CyberHack API.')
parser.add_argument('search_query', type=str, help='The domain or search term to query.')
args = parser.parse_args()

api_key = os.getenv('CYBERHACK_API_KEY')

if api_key is None:
    raise ValueError("API key not found. Please set the CYBERHACK_API_KEY environment variable.")

base_url = "https://api.cyberhack.io"
endpoint = "/search"

headers = {
    'X-API-KEY': api_key,
    'Content-Type': 'application/json'
}

params = {'q': args.search_query}

response = requests.get(base_url + endpoint, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)

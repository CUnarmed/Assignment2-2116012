import requests
import webbrowser

def get_random_advice(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()

        advice_data = response.json()
        return advice_data
    expect requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    expect requests.exceptions.ConnectionError as errc:
        print(f"Error Connection: {errc}")
    expect requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    expect requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

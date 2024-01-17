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

def display_advice(advice_data):
    if "slip" in advice_data and "advice" in advice_data["slip"]:
        print("\nRandom Advice:")
        print(advice_data["slip"]["advice"])
    else:
        print("unable to fetch random advice.")

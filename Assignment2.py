import requests
import webbrowser


def get_random_advice(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Check for errors in the response

        advice_data = response.json()
        return advice_data
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")


def display_advice(advice_data):
    if "slip" in advice_data and "advice" in advice_data["slip"]:
        print("\nRandom Advice:")
        print(advice_data["slip"]["advice"])
    else:
        print("unable to fetch random advice.")


def main():
    advice_api_url = "https://api.adviceslip.com/advice"


    advice_data = get_random_advice(advice_api_url)
    if advice_data:
        display_advice(advice_data)

if __name__ == "__main__":
    main()

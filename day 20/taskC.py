import requests

try:
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    data = response.json()
    print(f"Setup: {data["setup"]}")
    print(f"Punchline: {data["punchline"]}")

except requests.exceptions.RequestException as err:
    print(err)
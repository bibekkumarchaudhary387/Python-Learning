import requests

try:
    response = requests.get("https://api.kanye.rest/", timeout=5) # wait max 5 seconds
    response.raise_for_status() # Automatically raises an error if code is 404 or 500
    data = response.json()
    print(data["quote"])
except requests.exceptions.RequestException as e:
    print(f"Network Error: {e}")
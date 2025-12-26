# Task A: The Boredom Killer There is an API that suggests things to do when you are bored.
# URL: https://www.boredapi.com/api/activity (Note: If this URL is down, try https://official-joke-api.appspot.com/random_joke)
# Goal: Create a script that fetches an activity and prints it. Wrap it in a try/except block.

import requests as api

try:
    output = api.get("https://www.boredapi.com/api/activity ")
    print(output.status_code)
    data = output.json()
    print(data["id"])

except api.exceptions.RequestException as e:
    print(f"You get {e}")
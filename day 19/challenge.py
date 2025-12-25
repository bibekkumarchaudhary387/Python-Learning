# Daily Challenge: "The Kanye West Quote Machine"
# Scenario: You want some instant wisdom. We will build a script that fetches a random quote from Kanye West every time you run it.
# API URL: https://api.kanye.rest/

# Instructions:
# Import requests.
# Use requests.get() to call the URL.
# Check if status_code is 200 (Success).
# Convert the response to JSON: quote_data = response.json().

# Hint: Print the whole quote_data first to see the "key" name (it's likely called "quote").

# Print the quote nicely: "Kanye says: [quote]"

import requests as quotes

url = "https://api.kanye.rest/"

response = quotes.get(url)
print(response.status_code)

data = response.json() 
print(data["quote"])
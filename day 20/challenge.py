import requests as api

try:
    response = api.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response.raise_for_status() # Good practice to catch 404/500 errors
    
    data = response.json()
    
    # Navigating the layers
    rate = data["bpi"]["USD"]["rate"] 
    
    print(f"The current price of Bitcoin is: ${rate} USD")

except api.exceptions.RequestException as err:
    print(f"Connection Error: {err}")
except KeyError:
    print("Error: Could not find the price in the data.")
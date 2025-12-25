import requests as space

#url of the api
url = "http://api.open-notify.org/astros.json"

# reuqest to the server for data
responce = space.get(url)

# check the status 
# 200 if server response data
# 400 if data not found (error)
print(responce.status_code)

# responces data from api
data = responce.json() #convert json data into python dictianary
print(data["number"])
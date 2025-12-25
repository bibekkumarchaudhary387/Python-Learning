import requests as api

#1. url of api
url = "https://jsonplaceholder.typicode.com/posts/1"

#2. The request (asking for data)
response = api.get(url)

#3. The status (did server accept the redquest)
# 200  = ok (success)
# 400 = not found (error )
print(f"Status code is {response.status_code}")

# 4. The data (data responce from server)
data = response.json() #convert json string to python dictianary
print(data["body"])
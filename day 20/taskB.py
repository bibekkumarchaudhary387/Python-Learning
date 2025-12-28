import requests as api
import json as file

try:
    response = api.get("https://jsonplaceholder.typicode.com/users")
    output = response.json()
    users_filtered = []
    count = 0

    for x in output:
        users_filtered.append ({
            "id": x["id"],
            "name": x["name"],
            "email": x["email"],
            "city": x["address"]["city"]
        })
    

    with open("users_filtered.json", "w") as files:
        file.dump(users_filtered, files, indent=5)
        print(f"{len(users_filtered)} users successfully processed")

except api.exceptions.RequestException as err:
    print(err)
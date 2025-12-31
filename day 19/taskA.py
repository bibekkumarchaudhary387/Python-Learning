import requests as api
import json 

try:
    response = api.get("https://fakestoreapi.com/products")

    code_status = response.status_code
    filltered_record = []

    if code_status == 200:
        data = response.json()
        for x in data:
            if x["price"] >100 and x["rating"]["rate"] >= 4 :
                filltered_record.append ({
                    "id": x["id"],
                    "title": x["title"],
                    "price": x["price"],
                    "category": x["category"],
                    "rating": x["rating"]["rate"]
                })
        with open ("filltered_record_day19.json", "w") as file:
            json.dump(filltered_record, file, indent=4)
            print("Succeful")

except api.exceptions.ConnectionError:
    print("Connection not founded")

except api.exceptions.Timeout:
    print("Request time out")

except ValueError:
    print("Invalid json")

except Exception as err:
    print(f"unecpected error {err}")
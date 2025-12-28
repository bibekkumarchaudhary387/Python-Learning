import requests
import json

filtered_comments = []
try:
    url = requests.get("https://jsonplaceholder.typicode.com/comments")
    data = url.json()
    
    for x in data:
        lenght_of_body = len(x["body"])
        if x["email"].endswith(".net") and lenght_of_body > 100:
            filtered_comments.append ({
                "postId": x["postId"],
                "id": x["id"],
                "email": x["email"],
                "body": x["body"]
            })
        
    with open("filtered_comments.json", "w")  as file:
        json.dump(filtered_comments, file, indent=4)
    
    print(len(filtered_comments))
    print(filtered_comments[0]["email"])

except requests.exceptions.RequestException as err:
    print(err)
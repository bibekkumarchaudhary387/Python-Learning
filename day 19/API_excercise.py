import requests as api 
import json as file

url = "https://jsonplaceholder.typicode.com/posts"
filtered_post = []
responce = api.get(url)

data = responce.json()

for x in data:
    lenght = len(x['title'])
    if x['userId'] == 1 and lenght > 20:
        filtered_post.append({
            "id": x["id"],
            "title": x["title"],
            "body": x["body"]
        })

with open("filtered_post.json", "w") as files:
    file.dump(filtered_post, files, indent=4)

print("Total filtered posts:", len(filtered_post))
print("JSON file 'filtered_posts.json' created successfully.")
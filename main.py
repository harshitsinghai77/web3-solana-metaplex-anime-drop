import requests
import json


def get_image(i):
    doc = requests.get("https://api.waifu.pics/sfw/waifu")
    doc = doc.json()
    url = doc["url"]
    if url:
        response = requests.get(url)
        with open(f"./assets/{i}.png", "wb") as f:
            f.write(response.content)
        json_content = {
            "name": "Shadow Anime",
            "symbol": "SAnime",
            "image": f"{i}.png",
            "properties": {
                "files": [{"uri": f"{i}.png", "type": "image/png"}],
                "creators": [
                    {
                        "address": "8VPYec3biQg34yXcnB7NaZMCQ9ExxeAP9XhXqiRgk7NK",
                        "share": 100,
                    }
                ],
            },
        }
        with open(f"./assets/{i}.json", "w") as json_file:
            json_file.write(json.dumps(json_content))


for i in range(10):
    get_image(i)

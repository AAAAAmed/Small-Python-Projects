import requests
import json

while True:
    # Collect json data from chess.com
    username = input("\nEnter your Chess.com username: ")
    url = "https://api.chess.com/pub/player/{}".format(username)
    jsonData = requests.get(url)

    # Convert json to python dictionary
    pythonData = json.loads(jsonData.text)

    # Print link to avatar image
    print("\n", pythonData["avatar"])
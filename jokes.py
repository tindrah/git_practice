import requests

# api-endpoint
URL = "https://sv443.net/jokeapi/v2/joke/Any"

# sending get request and saving the response as response object
r = requests.get(url = URL)

# extracting data in json format
data = r.json()

if data['type'] == 'single':
    print("Joke: " + data['joke'])
else:
    print("Setup: " + data['setup'])
    print("Delivery: " + data['delivery'])

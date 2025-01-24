
import requests

# Joke API endpoint
url = "https://official-joke-api.appspot.com/random_joke"

# Send get request to fetch a joke
response = requests.get(url) 

# Check if the request was successful
if response.status_code == 200:
    jokeData = response.json()
    print(f"Joke = {jokeData['setup']} - {jokeData['punchline']}")
else:
    print("Error: Failed to retrieve joke")

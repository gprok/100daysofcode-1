import requests

r = requests.get(url='https://api.chucknorris.io/jokes/random')
response = r.json()
print("Random joke: ", response['value'])

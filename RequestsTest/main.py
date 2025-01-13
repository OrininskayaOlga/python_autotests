import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8d4800b860727ab32b0123d58f70e731'
HEADER = {'Content-Type': 'application/json', 'trainer_token':TOKEN}


body_create = {
    "name": "Chester",
    "photo_id": 5
}

body_change = {
    "pokemon_id": "191967",
    "name": "Alice",
    "photo_id": 5
}

body_add_pokeball = {
    "pokemon_id": "191967"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)
message = response_create.json() ['message']
print (message)

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)
message = response_change.json() ['message']
print(message)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)
message = response_add_pokeball.json() ['message']
print(message)
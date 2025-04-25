import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5cb86f3f5e0c3639dfd4bb87e55fc83c'
HEADER = {'Content-Type': 'application/json', 'trainer_token':TOKEN}
body_create = {
    "name": "generate",
    "photo_id": -1
}
body_change = {
    "pokemon_id": "301306",
    "name": "New",
    "photo_id": 3
}
body_inpokeball = {
    "pokemon_id": "301306"
}
'''response_create = requests.post(url = f'{URL}/pokemons', headers =HEADER, json = body_create)
print(response_create.text)'''
'''response_change = requests.put(url = f'{URL}/pokemons', headers =HEADER, json= body_change)
print(response_change.text)'''
response_inpokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers =HEADER, json= body_inpokeball)
print(response_inpokeball.text)
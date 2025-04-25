import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5cb86f3f5e0c3639dfd4bb87e55fc83c'
HEADER = {'Content-Type': 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '34468'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def tests_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID}) 
    assert response_get.json()["data"][0]['id'] == '34468'
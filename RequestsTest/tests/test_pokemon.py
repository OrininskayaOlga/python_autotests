import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8d4800b860727ab32b0123d58f70e731'
HEADER = {'Content-Type': 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = 14742

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_trainer_name():
    response_get_name = requests.get(url = f'{URL}/me', headers = HEADER)
    assert response_get_name.json()["data"] [0] ["trainer_name"] == "Helga Fleur"

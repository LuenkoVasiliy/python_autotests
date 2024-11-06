import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5c1b1356d8db08d44c525991017b7018'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN }
TRAINER_ID = 8048


def test_id_name_pokemon():
    response_get = requests.get(url = f'{URL}/pokemons', params= {'trainer_id': TRAINER_ID}) 
    assert response_get.json ()["data"][0]["name"] == 'Барабуля'

    

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200


def test_id_trainer():
    response_get_name = requests.get(url = f'{URL}/trainers', params= {'trainer_id': TRAINER_ID}) 
    assert response_get_name.json()["data"][0]['trainer_name'] == 'Василек'


   
@pytest.mark.parametrize ('key, value', [('name', 'Барабуля'),('id', '124997')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID}) 
    assert response_parametrize.json()["data"][0][key] == value



@pytest.mark.parametrize ('key, value', [('trainer_name', 'Василек'),('trainer_id', '8048')])
def test_parametrize_name(key, value):
    response_get_name_parametrize = requests.get(url=f'{URL}/trainers',params= {'trainer_id': TRAINER_ID})
    assert response_get_name_parametrize.json()["data"][0]['trainer_name'] == 'Василек'


import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5c1b1356d8db08d44c525991017b7018'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN }


body_registration = {
    "trainer_token": TOKEN,
    "email": "lavata@yandeks.ru",
    "password": "Iloveqa1111111111"
}
body_confirmation = {
    "trainer_token": TOKEN
}

body_create_pokemons = {
    "name": "Барабуля",
    "photo_id": 1
}

body_rename_pokemon = {
    "pokemon_id": "124399",
    "name": "ШУТ",
    "photo_id": 3
}

body_inpokeball= {
    "pokemon_id": "124400"
}

respons = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration) 
print(respons.text)

response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation) 
print(response_confirmation.text)

response_create_pokemons = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemons) 
print(response_create_pokemons.text)

response_rename_pokemon = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_rename_pokemon) 
print(response_rename_pokemon.text)

response_inpokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_inpokeball) 
print(response_inpokeball.text)
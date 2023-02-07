import requests
from entity import Pokemon


class PokemonRepo:

    url: str

    def __init__(self):

        self.url = "https://pokeapi.co/api/v2"

    def get_pokemon_by_id(self, id: str) -> Pokemon:

        url = f"{self.url}/pokemon/{id}/"

        res = requests.get(url)

        if (res.status_code == 404):
            return None
        else:
            json_body = res.json()
            return Pokemon(
                id=json_body['id'],
                name=json_body['name'].capitalize(),
                height=json_body['height'],
                hp=json_body['stats'][0]['base_stat'],
                attack=json_body['stats'][1]['base_stat'],
                defense=json_body['stats'][2]['base_stat'],
                speed=json_body['stats'][5]['base_stat'],
                weight=json_body['weight'],
                xp=json_body['base_experience'],
            )

from typing import List
from .pokemon import Pokemon

class Game:

    is_ended: bool
    leader: int
    deck_1: List[Pokemon]
    deck_2: List[Pokemon]

    def __init__(self, deck_1: List[Pokemon], deck_2: List[Pokemon]):

        self.is_ended = False
        self.leader = 0
        self.deck_1 = deck_1
        self.deck_2 = deck_2

        self._check_cards()

    def _check_cards(self):

        if (len(self.deck_1) != len(self.deck_2)):
            raise ValueError("Deck 1 and deck 2 does not have the same number of cards")

        deck_2_pokemon_id_list = [x.id for x in self.deck_2]
        for deck_1_pokemon in self.deck_1:
            if (deck_1_pokemon.id in deck_2_pokemon_id_list):
                raise ValueError(f"Duplicate pokemon found: {deck_1_pokemon.name}")

    def compare(self, stat: str, deck_1_pokemon_index: int, deck_2_pokemon_index: int) -> int:

        deck_1_stat = getattr(self.deck_1[deck_1_pokemon_index], stat)
        deck_2_stat = getattr(self.deck_2[deck_2_pokemon_index], stat)

        return_value = 0

        if (deck_1_stat > deck_2_stat):
            self.deck_2.pop(deck_2_pokemon_index)
            return_value = 1
        elif (deck_1_stat < deck_2_stat):
            self.deck_1.pop(deck_1_pokemon_index)
            return_value = -1

        self._check_is_ended()
        self._check_leader()
        return return_value

    def _check_is_ended(self):
        self.is_ended = len(self.deck_1) == 0 or len(self.deck_2) == 0

    def _check_leader(self):

        if len(self.deck_1) > len(self.deck_2):
            self.leader = 1

        elif len(self.deck_1) < len(self.deck_2):
            self.leader = -1

        else:
            self.leader = 0

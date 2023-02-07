import random
from typing import List
from entity import Pokemon, Game
from repository import PokemonRepo
from ui import TerminalUI

ui = TerminalUI()
pokemon_repo = PokemonRepo()

TOTAL_NUMBER_OF_POKEMON = 1000
BATTLE_MODES = [
    "attack",
    "defense",
    "hp",
    "height",
    "xp",
    "speed",
    "weight",
]

def main():

    # What you do here
    intro()

    number_of_pokemon_per_player = ask_number_of_pokemons()

    pokemon_ids = list(range(1, TOTAL_NUMBER_OF_POKEMON + 1))
    deck_1 = generate_deck(pokemon_ids, number_of_pokemon_per_player)
    deck_2 = generate_deck(pokemon_ids, number_of_pokemon_per_player)

    game = Game(deck_1=deck_1, deck_2=deck_2)

    round = 1

    while not game.is_ended:

        show_round(round)
        battle_mode = BATTLE_MODES[ask_battle_mode()]

        p1_pokemon_idx = ask_pokemon_to_select(deck_1, 1, battle_mode)
        p2_pokemon_idx = ask_pokemon_to_select(deck_2, 2, battle_mode)

        battle_res = game.compare(
            stat=battle_mode,
            deck_1_pokemon_index=p1_pokemon_idx,
            deck_2_pokemon_index=p2_pokemon_idx,
        )

        if (battle_res == 1):
            ui.display_single("Player 1 wins this round.")
        elif (battle_res == -1):
            ui.display_single("Player 2 wins this round.")
        else:
            ui.display_single("No winner.")

        show_game_summary(game)
        round += 1

    ui.display_multiple([
        "",
        "==========================",
        f"Player {1 if game.leader == 1 else 2} is the winner!",
        "==========================",
        "",
    ])

def intro():
    """Introduction to the application
    """
    ui.display_multiple([
        "",
        "==========================",
        "Welcome to Pokémon Top Trumps!",
        "==========================",
        "",
        'The rules are as follows:\n'
        '\n'
        'Before you begin, you will decide how many cards do you want to play in this game.\n'
        'For each round, you and your opponent will then each take turns to choose which stats you want to compete with.\n'
        'You will then choose which Pokémon to battle with. The higher stat wins the round.\n'
        'The defeated player from each round will lose that Pokémon from their deck.\n'
        'Whoever has the most cards left in their deck wins!\n'
    ])

def generate_deck(pokemon_pool: List[str], number_of_pokemon: int) -> List[Pokemon]:

    deck: List[Pokemon] = []
    for i in range(number_of_pokemon):
        idx = random.randint(0, len(pokemon_pool) - 1)
        pokemon_id = pokemon_pool.pop(idx)
        pokemon = pokemon_repo.get_pokemon_by_id(pokemon_id)
        if not pokemon:
            raise Exception(f"Pokemon with ID {pokemon_id} is missing")

        deck.append(pokemon)

    return deck

def ask_number_of_pokemons() -> int:
    return ui.ask_integer(
        "Please input the number of pokemons per player",
        min=1,
        max=int(TOTAL_NUMBER_OF_POKEMON / 2),
    )

def ask_battle_mode() -> str:
    return ui.ask_choices(BATTLE_MODES)

def ask_pokemon_to_select(deck: List[Pokemon], player: int, battle_mode: str) -> int:
    ui.display_multiple([
        "",
        "==========================",
        f"Player {player} turn",
        "==========================",
        "",
    ])
    return ui.ask_choices([
        f"{d.name}. {battle_mode}: {getattr(d, battle_mode)}."
        for d in deck
    ])

def show_game_summary(game: Game):
    ui.display_multiple([
        "",
        "==========================",
        "Match summary",
        f"Player 1 cards: {len(game.deck_1)}",
        f"Player 2 cards: {len(game.deck_2)}",
        "==========================",
        "",
    ])

def show_round(round: int):
    ui.display_multiple([
        "",
        "==========================",
        f"Round {round}",
        "==========================",
        "",
    ])

if __name__ == "__main__":
    main()

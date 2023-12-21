from behave import *
from pages import pokemon as pokemon_driver
import time

@given('I have opened the wikidex website')
def step_impl(context):
    pokemon_driver.browse_to_wikidex()

@when('I search for the Pokemon {pokemon}')
def step_impl(context, pokemon):
    pokemon_driver.search_for_pokemon(pokemon)

@then('I can assert that the last {attack_type}-type move that learns by leveling-up is {move}')
def step_impl(context, attack_type, move):
    assert pokemon_driver.get_last_move_by_type(attack_type) == move

@then('I can assert that its location in the game {game} is {location}')
def step_impl(context, game, location):
    assert pokemon_driver.get_location_by_generation(game) == location    

@then('I can assert that the egg moves that it can learn with {egg_pokemon} are {moves}')
def step_impl(context, egg_pokemon, moves):
    moves = moves.split(', ')
    time.sleep(0.1)
    assert set(pokemon_driver.get_egg_moves_by_parent(egg_pokemon)) == set(moves)
    

@then('I can assert that its levels of evolution are {levels}')
def step_impl(context, levels):
    levels = levels.split(', ')
    assert set(pokemon_driver.get_evolutions()) == set(levels)
    

@then('I can assert that its debilities are {debilities}')
def step_impl(context, debilities):
    debilities = debilities.split(', ')
    debilities = [debility.lower() for debility in debilities]
    time.sleep(0.1)
    assert set(pokemon_driver.get_debilities()) == set(debilities)




from behave import *
from pages import pokemon as pokemon_driver

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


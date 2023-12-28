from behave import *
from pages import pokemon as pokemon_driver
import re

@given('I have started a new test')
def step_impl(context):
    pokemon_driver.driver.reset()

@then('I can close the driver, once the test is done')
def step_impl(context):
    pokemon_driver.driver.close_driver()

@given('I have opened the wikidex website')
def step_impl(context):
    pokemon_driver.browse_to_wikidex()

@when('I search for the Pokemon {pokemon}')
def step_impl(context, pokemon):
    pokemon_driver.search_for_pokemon(pokemon)

@when('I navigate to Pokemon GO and click on the events from {year}')
def step_impl(context, year):
    pokemon_driver.hover_to_pokemon_go()
    pokemon_driver.go_to_list_events()
    pokemon_driver.get_event_by_year(year)

@then('I can assert that the event {event} started on {date}')
def step_impl(context, event, date):
    year = re.match("\\d+ de \\w+ del (\\d+)", date).group(1)
    
    not_formatted_date = pokemon_driver.get_event_start_date(event, year)
    possible_start_date = not_formatted_date.replace('Desde: ', '').strip()
    assert possible_start_date == date
    pokemon_driver.driver.close_driver()


@then('I can assert that the last {attack_type}-type move that learns by leveling-up in the game {game} is {move}')
def step_impl(context, attack_type, game, move):
    assert pokemon_driver.get_last_move_by_type_and_game(game, attack_type) == move
    pokemon_driver.driver.close_driver()

@then('I can assert that its location in the game {game} is {location}')
def step_impl(context, game, location):
    assert pokemon_driver.get_location_by_generation(game) == location    
    pokemon_driver.driver.close_driver()

@then('I can assert that the egg moves that it can learn with {egg_pokemon} are {moves}')
def step_impl(context, egg_pokemon, moves):
    moves = moves.split(', ')
    assert set(pokemon_driver.get_egg_moves_by_parent(egg_pokemon)) == set(moves)
    pokemon_driver.driver.close_driver()


@then('I can assert that its levels of evolution are {levels}')
def step_impl(context, levels):
    levels = levels.split(', ')
    assert set(pokemon_driver.get_evolutions()) == set(levels)
    pokemon_driver.driver.close_driver()

@then('I can assert that its debilities are {debilities}')
def step_impl(context, debilities):
    debilities = debilities.split(', ')
    debilities = [debility.lower() for debility in debilities]
    assert set(pokemon_driver.get_debilities()) == set(debilities)
    pokemon_driver.driver.close_driver()




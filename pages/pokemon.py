from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('')
search_bar = "//input[@type='search']"
search_button = "//input[@type='submit'][@value='Ir']"
last_move = "//table[contains(@class, 'movnivel')]//tr[.//a[contains(@title, 'TYPE_ATTACK')]][last()]//td[count(//table[contains(@class, 'movnivel')]//th[contains(@class, 'movimiento')]/preceding-sibling::th)+1]"
location_by_generation = "//span[@id='Localización']/following::a[contains(text(), 'GENERATION')][1]/following::a[@title='Pokémon salvaje'][1]/following::a[1]"
egg_move_list = "//table[contains(@class, 'movhuevo')]//tr[.//a[contains(@title, 'EGG_POKEMON')]]//td[count(//table[contains(@class, 'movhuevo')]//th[contains(@class, 'movimiento')]/preceding-sibling::th)+1]"

def browse_to_wikidex():
    driver.get("https://www.wikidex.net/")
    
def search_for_pokemon(pokemon):
    driver.find_element(By.XPATH, search_bar).send_keys(pokemon)
    driver.find_element(By.XPATH, search_bar).send_keys(Keys.RETURN)
    
def get_last_move_by_type(type):
    move = last_move.replace('TYPE_ATTACK', type)
    return driver.find_element(By.XPATH, move).text

def get_location_by_generation(generation):
    location = location_by_generation.replace('GENERATION', generation)
    return driver.find_element(By.XPATH, location).text

def get_egg_moves_by_parent(pokemon):
    moves = egg_move_list.replace('EGG_POKEMON', pokemon)
    return [move.text for move in driver.find_elements(By.XPATH, moves)]
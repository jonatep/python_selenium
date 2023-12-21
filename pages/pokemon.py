import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('')

search_bar = "//input[@type='search']"
search_button = "//input[@type='submit'][@value='Ir']"
last_move = "//table[contains(@class, 'movnivel')]//tr[.//a[contains(@title, 'TYPE_ATTACK')]][last()]//td[count(//table[contains(@class, 'movnivel')]//th[contains(@class, 'movimiento')]/preceding-sibling::th)+1]"
location_by_generation = "//span[@id='Localización']/following::a[contains(text(), 'GENERATION')][1]/following::a[@title='Pokémon salvaje'][1]/following::a[1]"
egg_move_list = "//table[contains(@class, 'movhuevo')]//tr[.//a[contains(@title, 'EGG_POKEMON')]]//td[count(//table[contains(@class, 'movhuevo')]//th[contains(@class, 'movimiento')]/preceding-sibling::th)+1]"
evolucion_list = "//span[@id='Evolución']/following::table[@class='evolucion']//td[@class='flecha']"
weak_types_list = "//span[@id='Debilidades_y_resistencias']/following::table[contains(@class, 'tabpokemon')]//tr[.//td[contains(text(), 'ébil')]]//td[count(//span[@id='Debilidades_y_resistencias']/following::table[contains(@class, 'tabpokemon')]//tr[.//th[contains(text(), 'Tipos')]/preceding-sibling::th])+2]//a"
pokemon_dropdown= "//li[@id='n-Pokémon']"
videogames_dropdown = "//li[@id='n-Pokémon']/ul//a[text()='Videojuegos']"
violet_link = "//li[@id='n-Pokémon']/ul//a[text()='Videojuegos']/following::a[text()='Escarlata y Púrpura']"
pokemon_go_link = "//li[@id='n-Pokémon']/ul//a[text()='Videojuegos']/following::a[text()='Pokémon GO']"
events_list = "//span[@id='Eventos_especiales']/following::a[contains(@title, 'Lista de eventos')]"
event_by_year = "//div[@id='mw-content-text']//a[contains(@title, YEAR)]"

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

def get_evolutions():
    return [nivel.text.replace('\n', ' ').strip() for nivel in driver.find_elements(By.XPATH, evolucion_list)]

def get_debilities():
    return [type.get_attribute('title').replace('Tipo ', '').strip() for type in driver.find_elements(By.XPATH, weak_types_list)]

def hover_to_pokemon_go():
    
    driver.execute_script("window.scrollTo(0, 100)")
    actions = ActionChains(driver)
    pokemon_dropdown_element = driver.find_element(By.XPATH, pokemon_dropdown)
    actions.move_to_element(pokemon_dropdown_element)
    actions.perform()
    
    videogames_dropdown_element = driver.find_element(By.XPATH, videogames_dropdown)
    actions.move_to_element(videogames_dropdown_element)
    actions.perform()
    
    violet_link_element = driver.find_element(By.XPATH, violet_link)
    actions.move_to_element(violet_link_element)
    actions.perform()
    
    pokemon_go_link_element = driver.find_element(By.XPATH, pokemon_go_link)
    actions = ActionChains(driver).move_to_element(pokemon_go_link_element)
    actions.perform()
      
    pokemon_go_link_element.click()

def go_to_list_events():
    events_list_element = driver.find_element(By.XPATH, events_list)
    scroll = ActionChains(driver).move_to_element(events_list_element)
    scroll.perform()
    events_list_element.click()

def get_event_by_year(year):
    event = event_by_year.replace('YEAR', year)
    event_element = driver.find_element(By.XPATH, event)
    event_element.click()


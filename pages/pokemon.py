import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome('')
wait = WebDriverWait(driver, timeout=2)

search_bar = "//input[@type='search']"
search_button = "//input[@type='submit'][@value='Ir']"
last_move = "//article[contains(@id, 'GENERATION')]/table[contains(@class, 'movnivel')]//tr[.//a[contains(@title, 'TYPE_ATTACK')]][last()]//td[count(//article[contains(@id, 'GENERATION')]/table[contains(@class, 'movnivel')]//th[contains(@class, 'movimiento')]/preceding-sibling::th)+1]"
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
button_cookies = "//button[@name='disablecookiewarning']"
event_start_date = "//span[contains(@id, 'EVENT_START')][1]/following::table[1]//td[./b[contains(text(), 'Desde')] and contains(text(), 'YEAR_EVENT')]"
arrow_generations = "//table[contains(@class, 'movnivel')]/preceding::div[@class='tabber__header__next'][1]"
button_generation_moves = "//table[contains(@class, 'movnivel')]/preceding::nav[@class='tabber__tabs'][1]//a[contains(@id, 'GENERATION')]"

def browse_to_wikidex():
    driver.get("https://www.wikidex.net/")
    click_cookies()

def search_for_pokemon(pokemon):
    driver.find_element(By.XPATH, search_bar).send_keys(pokemon)
    driver.find_element(By.XPATH, search_bar).send_keys(Keys.RETURN)

def click_arrow_next_moves():
    driver.find_element(By.XPATH, arrow_generations).click()

def select_generation_attack(game):
    try:
        button_desired_generation = button_generation_moves.replace('GENERATION', game.replace(' ', '_'))
        wait.until(lambda d : driver.find_element(By.XPATH, button_desired_generation).is_displayed())
        driver.find_element(By.XPATH, button_desired_generation).click()
    except:
        click_arrow_next_moves()
        time.sleep(.3)
        select_generation_attack(game)

def get_last_move_by_type_and_game(game, type):
    select_generation_attack(game)
    move = last_move.replace('TYPE_ATTACK', type).replace('GENERATION', game.replace(' ', '_'))
    wait.until(lambda d : driver.find_element(By.XPATH, move).is_displayed())
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

def perform_hover(element_xpath, actions):
    element = driver.find_element(By.XPATH, element_xpath)
    actions.move_to_element(element)
    actions.perform()

def click_cookies():
    try:
        button_cookies_element = driver.find_element(By.XPATH, button_cookies)
        button_cookies_element.click()
    except:
        print('The cookies button has already been pressed')
        
def hover_to_pokemon_go():    
    actions = ActionChains(driver)
    perform_hover(pokemon_dropdown, actions)
    perform_hover(videogames_dropdown, actions)
    perform_hover(violet_link, actions)
    perform_hover(pokemon_go_link, actions)
    
    pokemon_go_link_element = driver.find_element(By.XPATH, pokemon_go_link)
    pokemon_go_link_element.click()

def go_to_list_events():
    events_list_element = driver.find_element(By.XPATH, events_list)
    events_list_element.click()

def get_event_by_year(year):
    event = event_by_year.replace('YEAR', year)
    event_element = driver.find_element(By.XPATH, event)
    event_element.click()
    
def get_event_start_date(event, year):
    event_table = event_start_date.replace('EVENT_START', event.replace(' ', '_'))
    event_table = event_table.replace('YEAR_EVENT', year)
    event_start_date_element = driver.find_element(By.XPATH, event_table)
    return event_start_date_element.text

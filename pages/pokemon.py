from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from . import common

driver = webdriver.Chrome('')
wait = WebDriverWait(driver, timeout=2.5)

SEARCH_BAR = "//input[@type='search']"
LAST_MOVE = "//article[contains(@id, 'GENERATION')]\
                /table[contains(@class, 'movnivel')]\
                    //tr[.//a[contains(@title, 'TYPE_ATTACK')]][last()]\
                        //td[count(//article[contains(@id, 'GENERATION')]\
                            /table[contains(@class, 'movnivel')]\
                                //th[contains(@class, 'movimiento')]\
                                    /preceding-sibling::th)+1]"
LOCATION_BY_GENERATION = "//span[@id='Localización']\
                            /following::a[contains(text(), 'GENERATION')][1]\
                                /following::a[@title='Pokémon salvaje'][1]\
                                    /following::a[1]"
EGG_MOVE_LIST = "//table[contains(@class, 'movhuevo')]\
                    //tr[.//a[contains(@title, 'EGG_POKEMON')]]\
                        //td[count(//table[contains(@class, 'movhuevo')]\
                            //th[contains(@class, 'movimiento')]\
                                /preceding-sibling::th)+1]"
EGG_MOVE_TABLE = "//table[contains(@class, 'movhuevo')]"
EVOLUTION_LIST = "//span[@id='Evolución']\
                    /following::table[@class='evolucion']\
                        //td[@class='flecha']"
WEAK_TYPES_LIST = "//span[@id='Debilidades_y_resistencias']\
                    /following::table[contains(@class, 'tabpokemon')]\
                        //tr[.//td[contains(text(), 'ébil')]]\
                            //td[count(//span[@id='Debilidades_y_resistencias']\
                                /following::table[contains(@class, 'tabpokemon')]\
                                    //tr[.//th[contains(text(), 'Tipos')]\
                                        /preceding-sibling::th])+2]//a"
WEAK_TYPE_TABLE = "//span[@id='Debilidades_y_resistencias']\
                        /following::table[contains(@class, 'tabpokemon')]"
POKEMON_DROPDOWN= "//li[@id='n-Pokémon']"
VIDEOGAMES_DROPDOWN = "//li[@id='n-Pokémon']\
                        /ul//a[text()='Videojuegos']"
VIOLET_LINK = "//li[@id='n-Pokémon']\
                /ul\
                    //a[text()='Videojuegos']\
                        /following::a[text()='Escarlata y Púrpura']"
POKEMON_GO_LINK = "//li[@id='n-Pokémon']\
                    /ul\
                        //a[text()='Videojuegos']\
                            /following::a[text()='Pokémon GO']"
EVENTS_LIST = "//span[@id='Eventos_especiales']\
                    /following::a[contains(@title, 'Lista de eventos')]"
EVENT_BY_YEAR = "//div[@id='mw-content-text']\
                    //a[contains(@title, YEAR)]"
BUTTON_COOKIES = "//button[@name='disablecookiewarning']"
EVENT_START_DATE = "//span[contains(@id, 'EVENT_START')][1]\
                        /following::table[1]\
                            //td[./b[contains(text(), 'Desde')] and contains(text(), 'YEAR_EVENT')]"
ARROW_GENERATIONS = "//table[contains(@class, 'movnivel')]\
                        /preceding::div[@class='tabber__header__next'][1]"
BUTTON_GENERATION_MOVES = "//table[contains(@class, 'movnivel')]\
                            /preceding::nav[@class='tabber__tabs'][1]\
                                //a[contains(@id, 'GENERATION')]"

def browse_to_wikidex():
    driver.get("https://www.wikidex.net/")
    click_cookies()

def search_for_pokemon(pokemon):
    driver.find_element(By.XPATH, SEARCH_BAR).send_keys(pokemon)
    driver.find_element(By.XPATH, SEARCH_BAR).send_keys(Keys.RETURN)

def click_arrow_next_moves():
    driver.find_element(By.XPATH, ARROW_GENERATIONS).click()

def select_generation_attack(game):
    try:
        button_desired_generation = BUTTON_GENERATION_MOVES\
            .replace('GENERATION', game.replace(' ', '_'))

        wait.until(lambda d : driver.find_element(
                By.XPATH, button_desired_generation
            ).is_displayed())
        
        driver.find_element(By.XPATH, button_desired_generation).click()
    except:
        click_arrow_next_moves()
        driver.implicitly_wait(.1)
        select_generation_attack(game)

def get_last_move_by_type_and_game(game, type_attack):
    select_generation_attack(game)
    move = LAST_MOVE.replace('TYPE_ATTACK', type_attack)\
        .replace('GENERATION', game.replace(' ', '_'))
        
    wait.until(lambda d : driver.find_element(
            By.XPATH, move
        ).is_displayed())
    
    return driver.find_element(By.XPATH, move).text

def get_location_by_generation(generation):
    location = LOCATION_BY_GENERATION.replace('GENERATION', generation)
    return driver.find_element(By.XPATH, location).text

def get_egg_moves_by_parent(pokemon):
    moves = EGG_MOVE_LIST.replace('EGG_POKEMON', pokemon)
    wait.until(lambda d : driver.find_element(By.XPATH, EGG_MOVE_TABLE).is_displayed())
    return [move.text for move in driver.find_elements(By.XPATH, moves)]

def get_evolutions():
    return [nivel.text.replace('\n', ' ').strip()\
        for nivel in driver.find_elements(
            By.XPATH, EVOLUTION_LIST
            )]

def get_debilities():
    wait.until(lambda d : driver.find_element(By.XPATH, WEAK_TYPE_TABLE).is_displayed())
    return [type.get_attribute('title').replace('Tipo ', '').strip()\
        for type in driver.find_elements(
            By.XPATH, WEAK_TYPES_LIST
            )]

def perform_hover(element_xpath, actions):
    element = driver.find_element(By.XPATH, element_xpath)
    actions.move_to_element(element)
    actions.perform()

def click_cookies():
    try:
        button_cookies_element = driver.find_element(By.XPATH, BUTTON_COOKIES)
        button_cookies_element.click()
    except:
        print('The cookies button has already been pressed')
    
def hover_to_pokemon_go():    
    actions = ActionChains(driver)
    common.perform_hover_by_xpath(POKEMON_DROPDOWN, actions, driver)
    common.perform_hover_by_xpath(VIDEOGAMES_DROPDOWN, actions, driver)
    common.perform_hover_by_xpath(VIOLET_LINK, actions, driver)
    common.perform_hover_by_xpath(POKEMON_GO_LINK, actions, driver)
    
    pokemon_go_link_element = driver.find_element(By.XPATH, POKEMON_GO_LINK)
    pokemon_go_link_element.click()

def go_to_list_events():
    try:
        events_list_element = driver.find_element(By.XPATH, EVENTS_LIST)
        events_list_element.click()
    except ElementClickInterceptedException:
        click_cookies()
        
def get_event_by_year(year):
    event = EVENT_BY_YEAR.replace('YEAR', year)
    event_element = driver.find_element(By.XPATH, event)
    event_element.click()
    
def get_event_start_date(event, year):
    event_table = EVENT_START_DATE.replace('EVENT_START', event.replace(' ', '_'))
    event_table = event_table.replace('YEAR_EVENT', year)
    event_start_date_element = driver.find_element(By.XPATH, event_table)
    return event_start_date_element.text

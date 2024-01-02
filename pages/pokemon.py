from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from pages.common import Common

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

driver = Common()

def browse_to_wikidex():
    driver.go_to_url("https://www.wikidex.net/")
    click_cookies()

def search_for_pokemon(pokemon):
    driver.send_keys_by_xpath(SEARCH_BAR, pokemon)
    driver.send_keys_by_xpath(SEARCH_BAR, Keys.RETURN)

def click_arrow_next_moves():
    driver.click_on_element_by_xpath(ARROW_GENERATIONS)

def select_generation_attack(game):
    try:
        button_desired_generation = BUTTON_GENERATION_MOVES\
            .replace('GENERATION', game.replace(' ', '_'))

        driver.wait_until_web_element_is_displayed_by_xpath(button_desired_generation)
        driver.click_on_element_by_xpath(button_desired_generation)

    except:
        click_arrow_next_moves()
        driver.implicit_wait(.1)
        select_generation_attack(game)

def get_last_move_by_type_and_game(game, type_attack):
    select_generation_attack(game)
    move = LAST_MOVE.replace('TYPE_ATTACK', type_attack)\
        .replace('GENERATION', game.replace(' ', '_'))

    driver.wait_until_web_element_is_displayed_by_xpath(move)

    return driver.get_text_by_xpath(move)

def get_location_by_generation(generation):
    location = LOCATION_BY_GENERATION.replace('GENERATION', generation)
    return driver.get_text_by_xpath(location)

def get_egg_moves_by_parent(pokemon):
    moves = EGG_MOVE_LIST.replace('EGG_POKEMON', pokemon)
    driver.wait_until_web_element_is_displayed_by_xpath(EGG_MOVE_TABLE)
    return [move.text for move in driver.get_web_elements_by_xpath(moves)]

def get_evolutions():
    return [nivel.text.replace('\n', ' ').strip()\
                for nivel in \
                    driver.get_web_elements_by_xpath(EVOLUTION_LIST)
            ]

def get_debilities():
    driver.wait_until_web_element_is_displayed_by_xpath(WEAK_TYPE_TABLE)
    return [type.get_attribute('title').replace('Tipo ', '').strip()\
                for type in \
                    driver.get_web_elements_by_xpath(WEAK_TYPES_LIST)
            ]

def click_cookies():
    try:
        driver.click_on_element_by_xpath(BUTTON_COOKIES)
    except:
        print('The cookies button has already been pressed')

def hover_to_pokemon_go():
    driver.perform_hover_by_xpath(POKEMON_DROPDOWN)
    driver.perform_hover_by_xpath(VIDEOGAMES_DROPDOWN)
    driver.perform_hover_by_xpath(VIOLET_LINK)
    driver.perform_hover_by_xpath(POKEMON_GO_LINK)

    driver.click_on_element_by_xpath(POKEMON_GO_LINK)

def go_to_list_events():
    try:
        driver.click_on_element_by_xpath(EVENTS_LIST)
    except ElementClickInterceptedException:
        click_cookies()

def get_event_by_year(year):
    event = EVENT_BY_YEAR.replace('YEAR', year)
    driver.click_on_element_by_xpath(event)

def get_event_start_date(event, year):
    event_table = EVENT_START_DATE.replace('EVENT_START', event.replace(' ', '_'))
    event_table = event_table.replace('YEAR_EVENT', year)
    return driver.get_text_by_xpath(event_table)

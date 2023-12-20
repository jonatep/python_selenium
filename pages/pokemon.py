from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('')
search_bar = "//input[@type='search']"
search_button = "//input[@type='submit'][@value='Ir']"
last_normal_type_move = "//table[contains(@class, 'movnivel')]//tr[.//a[contains(@title, 'normal')]][last()]//td[count(//table[contains(@class, 'movnivel')]//th[contains(@class, 'movimiento')]/preceding-sibling::th)+1]"

def browse_to_wikidex():
    driver.get("https://www.wikidex.net/")
    
def search_for_pokemon(pokemon):
    driver.find_element(By.XPATH, search_bar).send_keys(pokemon)
    driver.find_element(By.XPATH, search_button).click()
    
def get_last_normal_type_move():
    return driver.find_element(By.XPATH, last_normal_type_move).text
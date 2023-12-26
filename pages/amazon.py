from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from . import common

driver = webdriver.Chrome('')
wait = WebDriverWait(driver, timeout=2.5)

variations_to_product = "//div[@id='inline-twister-expander-content-color_name']//li[not(contains(@class, 'swatch-prototype'))]//img"
main_image_product = "(//div[contains(@class, 'imgTagWrapper')]/img)[1]"
first_image = "//div[contains(@class, 'imgTagWrapper')]//img"

def browse_to_amazon():
    driver.get('https://www.amazon.com')

def go_to_product(product):
    driver.get(product)

def click_second_and_first_product():
    try:
        first_product = driver.find_element(By.XPATH, variations_to_product.replace('//img', '[1]'))
    except:
        print('Website version not supported')
        driver.close()
        
    second_product = driver.find_element(By.XPATH, variations_to_product.replace('//img', '[2]'))
    second_product.click()
    first_product.click()


def is_image_changing_when_hovering():
    elements = driver.find_elements(By.XPATH, variations_to_product)
    actions = ActionChains(driver)
    res = []
    wait.until(lambda d : driver.find_element(By.XPATH, main_image_product)).is_displayed()
    previous_image = driver.find_element(By.XPATH, first_image).get_attribute('src')
    
    for element in elements:
        common.perform_hover_by_element(element, actions)
        current_image = driver.find_element(By.XPATH, main_image_product).get_attribute('src')
        res.append(previous_image != current_image)
    
    return res.count(False) == 1
        
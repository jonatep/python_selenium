from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from . import common
import re
import math 

driver = webdriver.Chrome('')
wait = WebDriverWait(driver, timeout=2.5)

variations_to_product = "//div[@id='inline-twister-expander-content-color_name']//li[not(contains(@class, 'swatch-prototype'))]//img"
main_image_product = "(//div[contains(@class, 'imgTagWrapper')]/img)[1]"
alternating_image_product = "//li[contains(@class, 'swatch')]//div[contains(@class, 'imgTagWrapper')]/img"
discount_price_whole = "//div[contains(@id, 'corePriceDisplay')]//span[contains(@class, 'a-price-whole')]"
discount_price_fraction = "//div[contains(@id, 'corePriceDisplay')]//span[contains(@class, 'a-price-fraction')]"
original_price = "//div[contains(@id, 'corePriceDisplay')]//span[contains(@class, 'a-text-price')]//span[@aria-hidden]"
discount = "//div[contains(@id, 'corePriceDisplay')]//span[contains(@class, 'savingPriceOverride ')]"
checkbox_coupon = "//label[contains(@for, 'checkbox')]//i[contains(@class, 'checkbox')]"
checkbox_input = "//label[contains(@for, 'checkbox')]//input[contains(@id, 'checkbox')]"

def browse_to_amazon():
    driver.get('https://www.amazon.com')

def go_to_product(product):
    driver.get(product)

def is_image_changing_when_hovering():
    elements = driver.find_elements(By.XPATH, variations_to_product)
    actions = ActionChains(driver)
    res = True
    wait.until(lambda d : driver.find_element(By.XPATH, main_image_product)).is_displayed()
    previous_image = driver.find_element(By.XPATH, main_image_product).get_attribute('src')
    
    for element in elements[1:]:
        common.perform_hover_by_element(element, actions)
        current_image = driver.find_element(By.XPATH, alternating_image_product).get_attribute('src')
        res = res and (previous_image != current_image)
    
    return res

def get_discount(original_price, discounted_price):
    return (1- (discounted_price / original_price)) * 100       

def is_discount_accurate():
    try:
        discount_price_fraction_text = driver.find_element(By.XPATH, discount_price_fraction).text
    except:
        print("This product currently doesn't have a discount")
        return False
    
    original_price_text = driver.find_element(By.XPATH, original_price).text    
    discount_price_whole_text = driver.find_element(By.XPATH, discount_price_whole).text
    discount_percentage_text = driver.find_element(By.XPATH, discount).text
    
    discount_price_text = discount_price_whole_text + "." + discount_price_fraction_text
    original_price_text = re.findall("\\d+.\\d+", original_price_text)[0]
    discount_percentage_text = re.findall("\\d+", discount_percentage_text)[0]
    
    discount_percentage_shown = get_discount(float(original_price_text), float(discount_price_text))
     
    return float(discount_percentage_text) == math.trunc(discount_percentage_shown)

def click_on_coupon_checkbox():
    checkbox_coupon_element = driver.find_element(By.XPATH, checkbox_coupon)
    checkbox_coupon_element.click()
    
def get_current_url():
    return driver.current_url

def go_to_previous_tab():
    driver.back()
    
def is_checkbox_selected():
    checkbox = driver.find_element(By.XPATH, checkbox_input)
    return checkbox.is_selected()
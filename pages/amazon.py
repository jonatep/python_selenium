import re
import math 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from . import common


driver = webdriver.Chrome('')
wait = WebDriverWait(driver, timeout=2.5)

VARIATIONS_TO_PRODUCT = "//div[@id='inline-twister-expander-content-color_name']\
                            //li[not(contains(@class, 'swatch-prototype'))]\
                                //img"
MAIN_IMAGE_PRODUCT = "(//div[contains(@class, 'imgTagWrapper')]/img)[1]"
ALTERNATING_IMAGE_PRODUCT = "//li[contains(@class, 'swatch')]\
                                //div[contains(@class, 'imgTagWrapper')]\
                                    /img"
DISCOUNT_PRICE_WHOLE = "//div[contains(@id, 'corePriceDisplay')]\
                            //span[contains(@class, 'a-price-whole')]"
DISCOUNT_PRICE_FRACTION = "//div[contains(@id, 'corePriceDisplay')]\
                            //span[contains(@class, 'a-price-fraction')]"
ORIGINAL_PRICE = "//div[contains(@id, 'corePriceDisplay')]\
                    //span[contains(@class, 'a-text-price')]\
                        //span[@aria-hidden]"
DISCOUNT = "//div[contains(@id, 'corePriceDisplay')]\
                //span[contains(@class, 'savingPriceOverride ')]"
CHECKBOX_COUPON = "//label[contains(@for, 'checkbox')]\
                    //i[contains(@class, 'checkbox')]"
CHECKBOX_INPUT = "//label[contains(@for, 'checkbox')]\
                    //input[contains(@id, 'checkbox')]"
LANGUAGE_NAV_TOOL = "//div[@id='nav-tools']\
                        //a[contains(@id, 'icp')]"
CHANGE_CURRENCY_LINK = "//div[@id = 'nav-flyout-icp']\
                            //a[contains(@class, 'change')]"
CURRENCY_DROPDOWN = "//p[contains(@id, 'currency-dropdown')]\
                        //span[contains(@id, 'dropdown')]"
SPECIFIC_CURRENCY = "//div[contains(@class, 'wrapper')]\
                        //li[@role='option' and @id='CURRENCY']"
CONFIRM_CURRENCY_BUTTON = "(//span[contains(@id, 'save-button')])[1]\
                                //input"

def browse_to_amazon():
    driver.get('https://www.amazon.com/')

def go_to_product(product):
    driver.get(product)

def is_image_changing_when_hovering():
    elements = driver.find_elements(By.XPATH, VARIATIONS_TO_PRODUCT)
    actions = ActionChains(driver)
    res = True
    wait.until(lambda d : driver.find_element(By.XPATH, MAIN_IMAGE_PRODUCT)).is_displayed()
    previous_image = driver.find_element(By.XPATH, MAIN_IMAGE_PRODUCT).get_attribute('src')
    
    for element in elements[1:]:
        common.perform_hover_by_element(element, actions)
        current_image = driver.find_element(
                By.XPATH, ALTERNATING_IMAGE_PRODUCT
            ).get_attribute('src')
        
        res = res and (previous_image != current_image)
    
    return res

def get_discount(price, discounted_price):
    return (1- (discounted_price / price)) * 100       

def is_discount_accurate():
    try:
        discount_price_fraction_text = driver.find_element(By.XPATH, DISCOUNT_PRICE_FRACTION).text
    except NoSuchElementException:
        print("This product currently doesn't have a discount")
        return False
    
    original_price_text = driver.find_element(By.XPATH, ORIGINAL_PRICE).text    
    discount_price_whole_text = driver.find_element(By.XPATH, DISCOUNT_PRICE_WHOLE).text
    discount_percentage_text = driver.find_element(By.XPATH, DISCOUNT).text
    
    discount_price_text = discount_price_whole_text + "." + discount_price_fraction_text
    original_price_text = re.findall("\\d+.\\d+", original_price_text)[0]
    discount_percentage_text = re.findall("\\d+", discount_percentage_text)[0]
    
    discount_percentage_shown = get_discount(float(original_price_text), float(discount_price_text))
     
    return float(discount_percentage_text) == math.trunc(discount_percentage_shown)

def click_on_coupon_checkbox():
    checkbox_coupon_element = driver.find_element(By.XPATH, CHECKBOX_COUPON)
    checkbox_coupon_element.click()
    
def get_current_url():
    return driver.current_url

def go_to_previous_tab():
    driver.back()
    
def is_checkbox_selected():
    checkbox = driver.find_element(By.XPATH, CHECKBOX_INPUT)
    return checkbox.is_selected()

def go_to_currency_change_page():
    actions = ActionChains(driver)
    common.perform_hover_by_xpath(LANGUAGE_NAV_TOOL, actions, driver)
    wait.until(lambda d : driver.find_element(By.XPATH, CHANGE_CURRENCY_LINK)).is_displayed()
    change_currency_link_element = driver.find_element(By.XPATH, CHANGE_CURRENCY_LINK)
    change_currency_link_element.click()

def select_currency_from_dropdown(currency):
    currency_dropdown_element = driver.find_element(By.XPATH, CURRENCY_DROPDOWN)
    currency_dropdown_element.click()
    specific_currency_replaced = SPECIFIC_CURRENCY.replace('CURRENCY', currency)
    specific_currency_element = driver.find_element(By.XPATH, specific_currency_replaced)
    specific_currency_element.click()
    confirm_currency_button_element = driver.find_element(By.XPATH, CONFIRM_CURRENCY_BUTTON)
    confirm_currency_button_element.click()


def get_current_currency():
    wait.until(EC.none_of(EC.url_contains("customer-preferences")))
    preceding_sibling = "/preceding-sibling::span"
    current_currency = CHANGE_CURRENCY_LINK + preceding_sibling
    actions = ActionChains(driver)
    common.perform_hover_by_xpath(LANGUAGE_NAV_TOOL, actions, driver)
    wait.until(lambda d : driver.find_element(By.XPATH, CHANGE_CURRENCY_LINK)).is_displayed()
    current_currency_text = driver.find_element(By.XPATH, current_currency).text
    current_currency_text = re.match(".* *(\\w{3}) - .+", current_currency_text).group(1)
    return current_currency_text
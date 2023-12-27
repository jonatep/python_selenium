from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('')
wait = WebDriverWait(driver, timeout=2.5)
actions = ActionChains(driver)

def go_to_url(url):
    driver.get(url)

def perform_hover_by_xpath(element_xpath):
    element = driver.find_element(By.XPATH, element_xpath)
    actions.move_to_element(element)
    actions.perform()

def perform_hover_by_element(element):
    actions.move_to_element(element)
    actions.perform()

def get_web_elements_by_xpath(xpath):
    return driver.find_elements(By.XPATH, xpath)

def get_web_element_by_xpath(xpath):
    return driver.find_element(By.XPATH, xpath)

def get_text_by_xpath(xpath):
    return get_web_element_by_xpath(xpath).text

def send_keys_by_xpath(xpath, keys):
    get_web_element_by_xpath(xpath).send_keys(keys)

def click_on_element_by_xpath(xpath):
    get_web_element_by_xpath(xpath).click()

def wait_until_web_element_is_displayed_by_xpath(xpath):
    wait.until(lambda d : get_web_element_by_xpath(xpath)).is_displayed()

def wait_until_url_does_not_contain_string(string):
    wait.until(EC.none_of(EC.url_contains(string)))

def go_to_previous_tab():
    driver.back()

def implicit_wait(seconds):
    driver.implicitly_wait(seconds)

def get_current_url():
    return driver.current_url
from selenium.webdriver.common.by import By

def perform_hover_by_xpath(element_xpath, actions, driver):
    element = driver.find_element(By.XPATH, element_xpath)
    actions.move_to_element(element)
    actions.perform()
    
def perform_hover_by_element(element, actions):
    actions.move_to_element(element)
    actions.perform()
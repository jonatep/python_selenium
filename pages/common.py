import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Common:

    def __init__(self):
        self.reset()

    def reset(self):
        desired_browser = os.environ['DRIVER_BROWSER']
        desired_timeout = float(os.environ['TIMEOUT'])

        if desired_browser == 'chrome':
            self.driver = webdriver.Chrome('')

        elif desired_browser == 'firefox':
            self.driver = webdriver.Firefox('')

        elif desired_browser == 'edge':
            self.driver = webdriver.Edge('')

        elif desired_browser == 'safari':
            self.driver = webdriver.Safari('')

        self.wait = WebDriverWait(self.driver, timeout = desired_timeout)
        self.actions = ActionChains(self.driver)
        
    def close_driver(self):
        self.driver.quit()

    def go_to_url(self, url):
        self.driver.get(url)

    def perform_hover_by_xpath(self, element_xpath):
        element = self.driver.find_element(By.XPATH, element_xpath)
        self.actions.move_to_element(element)
        self.actions.perform()

    def perform_hover_by_element(self, element):
        self.actions.move_to_element(element)
        self.actions.perform()

    def get_web_elements_by_xpath(self, xpath):
        return self.driver.find_elements(By.XPATH, xpath)

    def get_web_element_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def get_text_by_xpath(self, xpath):
        return self.get_web_element_by_xpath(xpath).text

    def send_keys_by_xpath(self, xpath, keys):
        self.get_web_element_by_xpath(xpath).send_keys(keys)

    def click_on_element_by_xpath(self, xpath):
        self.get_web_element_by_xpath(xpath).click()

    def wait_until_web_element_is_displayed_by_xpath(self, xpath):
        self.wait.until(lambda d : self.get_web_element_by_xpath(xpath)).is_displayed()

    def wait_until_url_does_not_contain_string(self, string):
        self.wait.until(EC.none_of(EC.url_contains(string)))

    def go_to_previous_tab(self):
        self.driver.back()

    def implicit_wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    def get_current_url(self):
        return self.driver.current_url
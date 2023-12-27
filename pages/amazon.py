import re
import math
from selenium.common.exceptions import NoSuchElementException
from . import common

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
    common.go_to_url('https://www.amazon.com/')

def go_to_product(product):
    common.go_to_url(product)

def is_image_changing_when_hovering():
    elements = common.get_web_elements_by_xpath(VARIATIONS_TO_PRODUCT)
    res = True
    common.wait_until_web_element_is_displayed_by_xpath(MAIN_IMAGE_PRODUCT)
    previous_image = common.get_web_element_by_xpath(MAIN_IMAGE_PRODUCT).get_attribute('src')

    for element in elements[1:]:
        common.perform_hover_by_element(element)
        current_image = common.get_web_element_by_xpath(
                ALTERNATING_IMAGE_PRODUCT
            ).get_attribute('src')

        res = res and (previous_image != current_image)

    return res

def get_discount(price, discounted_price):
    return (1- (discounted_price / price)) * 100

def is_discount_accurate():
    try:
        discount_price_fraction_text = common.get_text_by_xpath(DISCOUNT_PRICE_FRACTION)
    except NoSuchElementException:
        print("This product currently doesn't have a discount")
        return False

    original_price_text = common.get_text_by_xpath(ORIGINAL_PRICE)
    discount_price_whole_text = common.get_text_by_xpath(DISCOUNT_PRICE_WHOLE)
    discount_percentage_text = common.get_text_by_xpath(DISCOUNT)

    discount_price_text = discount_price_whole_text + "." + discount_price_fraction_text
    original_price_text = re.findall("\\d+.\\d+", original_price_text)[0]
    discount_percentage_text = re.findall("\\d+", discount_percentage_text)[0]

    discount_percentage_shown = get_discount(float(original_price_text), float(discount_price_text))

    return (float(discount_percentage_text) - math.trunc(discount_percentage_shown)) < 2

def click_on_coupon_checkbox():
    checkbox_coupon_element = common.get_web_element_by_xpath(CHECKBOX_COUPON)
    checkbox_coupon_element.click()

def is_checkbox_selected():
    checkbox = common.get_web_element_by_xpath(CHECKBOX_INPUT)
    return checkbox.is_selected()

def go_to_currency_change_page():
    common.perform_hover_by_xpath(LANGUAGE_NAV_TOOL)
    common.wait_until_web_element_is_displayed_by_xpath(CHANGE_CURRENCY_LINK)
    common.click_on_element_by_xpath(CHANGE_CURRENCY_LINK)

def select_currency_from_dropdown(currency):
    common.click_on_element_by_xpath(CURRENCY_DROPDOWN)
    specific_currency_replaced = SPECIFIC_CURRENCY.replace('CURRENCY', currency)
    common.click_on_element_by_xpath(specific_currency_replaced)
    common.click_on_element_by_xpath(CONFIRM_CURRENCY_BUTTON)


def get_current_currency():
    common.wait_until_url_does_not_contain_string("customer-preferences")
    preceding_sibling = "/preceding-sibling::span"
    current_currency = CHANGE_CURRENCY_LINK + preceding_sibling
    common.perform_hover_by_xpath(LANGUAGE_NAV_TOOL)
    common.wait_until_web_element_is_displayed_by_xpath(CHANGE_CURRENCY_LINK)
    current_currency_text = common.get_text_by_xpath(current_currency)
    current_currency_text = re.match(".* *(\\w{3}) - .+", current_currency_text).group(1)
    return current_currency_text

from behave import *
from pages import amazon as amazon_driver

@given('I have opened Amazon')
def step_impl(context):
    amazon_driver.browse_to_amazon()
    
@given('I go to an Amazon {product}')
def step_impl(context, product):
    amazon_driver.go_to_product(product)

@when('I go to the previous tab')
def step_impl(context):
    amazon_driver.driver.go_to_previous_tab()

@when('I select the currency {currency} in the currency dropdown')
def step_impl(context, currency):
    amazon_driver.go_to_currency_change_page()
    amazon_driver.select_currency_from_dropdown(currency)

@then('I can assert that, when hovering over variations of the product, the image changes')
def step_impl(context):
    assert amazon_driver.is_image_changing_when_hovering() == True
    amazon_driver.driver.close_driver()

@then('I can assert that the product shows an accurate discount percent in its price')
def step_impl(context):
    assert amazon_driver.is_discount_accurate() == True
    amazon_driver.driver.close_driver()
@then('If I click on the coupon checkbox, I go to the login page')
def step_impl(context):
    amazon_driver.click_on_coupon_checkbox()
    assert "https://www.amazon.com/ap/signin?" in amazon_driver.driver.get_current_url()
    amazon_driver.driver.close_driver()

# This test will result in a failure, not because of the design of the test itself,
# but because Amazon doesn't take into account this case when selecting checkboxes
@then('I can assert that the coupon checkbox is not selected')
def step_impl(context):
    assert amazon_driver.is_checkbox_selected() == False
    amazon_driver.driver.close_driver()

@then('The products are displayed with the currency {currency}')
def step_impl(context, currency):
    shown_currency = amazon_driver.get_current_currency()
    assert shown_currency == currency
    amazon_driver.driver.close_driver()

    
from behave import *
from pages import amazon as amazon_driver

@given('I have opened Amazon')
def step_impl(context):
    amazon_driver.browse_to_amazon()
    
@when('I go to a {product}')
def step_impl(context, product):
    amazon_driver.go_to_product(product)
    
@then('I can assert that, when hovering over variations of the product, the image changes')
def step_impl(context):
    assert amazon_driver.is_image_changing_when_hovering() == True

@then('I can assert that the product shows an accurate discount percent in its price')
def step_impl(context):
    assert amazon_driver.is_discount_accurate() == True



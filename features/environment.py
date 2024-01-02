import os
from behave import fixture, use_fixture
from selenium import webdriver
from pages.common import Common

AMAZON_TAG = 'amazon'
POKEMON_TAG = 'pokemon'

os.environ['DRIVER_BROWSER'] = 'chrome'
os.environ['TIMEOUT'] = '2.5'

def before_scenario(context, scenario):
    if AMAZON_TAG in context.tags:
        context.execute_steps(u'''
            given I have started a new amazon test
        ''')
    elif POKEMON_TAG in context.tags:
        context.execute_steps(u'''
            given I have started a new pokemon test
        ''')

def after_scenario(context, scenario):
    if AMAZON_TAG in context.tags:
        context.execute_steps(u'''
            then I can close the driver, once the amazon test is done
        ''')  
    elif POKEMON_TAG in context.tags:
        context.execute_steps(u'''
            then I can close the driver, once the pokemon test is done
        ''')  

    

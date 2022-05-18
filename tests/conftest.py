"""
This module contains shared fixtures
"""

#--------------------------------------------------------------------
#Imports
#--------------------------------------------------------------------
import json
import pytest
import selenium.webdriver
from helper_function import *

@pytest.fixture
def config(scope='session'):

    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)
    
    # Assert values are acceptable
    assert config['browser'] in ['Firefox','Chrome','Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config

@pytest.fixture
def browser(config):
    # Generator setup

    # Initialize the WebDriver instance
    if config['browser'] == 'Firefox':
        # Initialize the Firefox instance
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        # Initialize the ChromeDriver instance
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make its calls wait upto 10 seconds for elements to appear
    b.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield b

    # Generator Tear-down: Quit the WebDriver instance for the cleanup
    b.quit()


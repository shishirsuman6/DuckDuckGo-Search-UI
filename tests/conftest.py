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
        # Explicitly saying that this is a headless application
        opts.add_argument('headless')
        # Explicitly bypassing the security level in Docker, 
        # apparently as Docker deamon always runs as a root user, Chrome crushes.
        opts.add_argument('no-sandbox')
        # Explicitly disabling the usage of /dev/shm/ . 
        # The /dev/shm partition is too small in certain VM environments, causing Chrome to fail or crash.
        opts.add_argument('disable-dev-shm-usage')
        #Disabling the images with chrome_prefs["profile.default_content_settings"] = {"images": 2}
        chrome_prefs = {}
        opts.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make its calls wait upto 10 seconds for elements to appear
    b.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield b

    # Generator Tear-down: Quit the WebDriver instance for the cleanup
    b.quit()


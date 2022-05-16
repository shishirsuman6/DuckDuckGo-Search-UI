"""
This module contains shared fixtures
"""

#--------------------------------------------------------------------
#Imports
#--------------------------------------------------------------------
import pytest
import selenium.webdriver
from helper_function import *

@pytest.fixture
def browser():
    # Generator setup

    # Initialize the ChromeDriver instance
    b = selenium.webdriver.Chrome()

    # Make its calls wait upto 10 seconds for elements to appear
    b.implicitly_wait(10)

    # Return the WebDriver instance for the setup
    yield b

    # Generator Tear-down: Quit the WebDriver instance for the cleanup
    b.quit()


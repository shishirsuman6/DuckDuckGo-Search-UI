"""
This module contains DuckDuckGoSearchPage
the page object for the DuckDuckGo search page
"""

from ast import Pass
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoSearchPage:

    # URL
    URL = 'https://duckduckgo.com/'

    # Locators

    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

    # Initializer

    def __init__(self,browser):
        self.browser = browser

    # Interaction Methods
    
    def load(self):
        self.browser.get(self.URL)

    def search(self,phrase):
        # TODO
        # Test Intearaction with Elements
        # 1. Wait for the target element to appear
        # 2. Get an Object representign the target element
        # 3. send commands to the element object
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN )

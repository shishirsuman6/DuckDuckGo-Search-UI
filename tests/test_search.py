"""
These tests cover DuckDuckGo searches.
"""
#--------------------------------------------------------------------
#Imports
#--------------------------------------------------------------------
from ast import Pass
import pytest
from helper_function import *
from pages.results import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

#--------------------------------------------------------------------
# Tests
#--------------------------------------------------------------------

def test_basic_duckduckgo_search(browser):

    # Scenario: Basic DuckDuckGo search
    search_page= DuckDuckGoSearchPage(browser)
    result_page= DuckDuckGoResultPage(browser)
    PHRASE='orange'

    # Given the DuckDuckGo Home page is displayed
    search_page.load()
    
    # When the user searches for "panda"
    search_page.search(PHRASE)
    
    # Then the search result title contains "panda"
    assert PHRASE in result_page.title()
    
    # And the search result query is "panda"
    assert PHRASE == result_page.search_input_value()
    
    # And the search result links pertain to "panda"
    titles = result_page.result_link_titles()
    matches = [t for t in titles if PHRASE.lower() in t.lower() ]
    assert len(matches) > 0
    
    # Remove this once the test is complete
    raise Exception("Incomplete Test")
    
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

@pytest.mark.parametrize('phrase', ['NFL','NBA','MLB'])
def test_basic_duckduckgo_search(browser, phrase):

    # Scenario: Basic DuckDuckGo search
    search_page= DuckDuckGoSearchPage(browser)
    result_page= DuckDuckGoResultPage(browser)
    
    # Given the DuckDuckGo Home page is displayed
    search_page.load()
    
    # When the user searches for phrase
    search_page.search(phrase)
    
    
    
    # And the search result query is phrase
    assert phrase == result_page.search_input_value()
    
    # And the search result links pertain to phrase
    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower() ]
    assert len(matches) > 0

    # Then the search result title contains phrase
    assert phrase in result_page.title()
    
    # Remove this once the test is complete
    # raise Exception("Incomplete Test")
    
# DuckDuckGo-Search-UI
Use Pytest and Selenium to automate testing for DuckDuckGo Search UI features


## Test Case

    Scenario: Basic DuckDuckGo Search
    Given the DuckDuckGo home page is displayed
    When the user searches for "panda"
    Then the search result title contains "panda"
    And the search result query is "panda"
    And the search result links pertain to "panda"



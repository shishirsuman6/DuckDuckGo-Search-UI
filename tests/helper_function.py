"""
The purpose of this test file is to store helper functions for the pytest framework for DuckDuckGo Search Feature
"""
#--------------------------------------------------------------------
#Imports
#--------------------------------------------------------------------
import pytest

# #--------------------------------------------------------------------
# # functions
# #--------------------------------------------------------------------

def pytest_html_report_title(report):
    report.title = "DuckDuckGo Search Feature - Test Results"
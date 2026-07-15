"""
This pytest config file defines shared fixtures used across the API test suite.
It helps avoid duplication and keeps test setup consistent across different test files.
"""

import pytest


@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"
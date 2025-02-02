import pytest
import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from data import TestData


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--window-size=1200,800')
    browser = webdriver.Firefox(options=options)
    browser.get(TestData.base_url)
    yield browser
    browser.quit()

from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(r"C:\Users\DELL\PycharmProjects\nopCommerce\testCases\chromedriver.exe")
    return driver
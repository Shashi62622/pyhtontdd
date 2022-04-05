import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage

class Test_001_Login:
    baseUrl = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Your store. Login12":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("screenshots/test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_titel = self.driver.title
        if act_titel == "Dashboard / nopCommerce administration12":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("screenshot/test_login.png")
            self.driver.close()
            assert False

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from utilities.readProperties1 import ReadConfig
from utilities.customLogger import LogGen
# creating test cases for login and checking titles of the login page and dashboard page
class Test_001_Login:
    baseURL=ReadConfig.getApplicationURL()  # collection data from readProperties configuration file
    username=ReadConfig.getUserEmail()
    password=ReadConfig.getUserPassword()
    logger=LogGen.logegn()\

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homepage(self,setup):
        self.logger.info("**********Test_001_Login started **********")
        self.logger.info("********** Verifying homepage title **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title =self.driver.title
        if act_title=='Your store. Login':
            assert True
            self.logger.info("**********Test_001_Login  test passed **********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_homepage.png")
            self.driver.close()
            self.logger.info("**********Verification of Login Test failed **********")
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("********** Verifying login Page **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setPassword(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("********** Verifying login Page succesfully **********")
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_login.png")
            self.driver.close()
            assert False
            self.logger.info("********** Verification of login Page Failed **********")


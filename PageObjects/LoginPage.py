from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By



class LoginPage:
    textbox_username_id="Email"
    textbox_password_id="Password"
    button_login_xpath="//button[@type='submit']"
    button_logout_xpath="//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clicklogout(self):
        self.driver.find_element(By.XPATH,self.button_logout_xpath).click()
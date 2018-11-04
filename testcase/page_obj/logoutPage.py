#coding = utf-8
from selenium.webdriver.common.by import By
from .base import Page
from .loginPage import login
from time import sleep

class logout(Page):
    bbs_logout_loc = (By.LINK_TEXT,'退出')
    def user_login(self):
        login(self.driver).user_login()
    def logout_click(self):
        self.find_element(*self.bbs_logout_loc).click()
        sleep(3)
    def check_logout(self):
        self.find_element(*login.bbs_login_user_loc)
#coding = 'utf-8'
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class login(Page):
    '''
    用户登录页面
    '''
    url = '/'

    #Location
    bbs_login_user_loc = (By.LINK_TEXT,'登录')
    #bbs_login_button_loc = (By.XPATH,'//button[@name = "loginsubmit"]')
    login_username_loc = (By.XPATH,'//input[@name ="username"]')
    login_password_loc = (By.XPATH,'//input[@name ="password"]')
    login_button_loc = (By.XPATH,'//button[@name = "loginsubmit"]')
    question_select_loc = (By.XPATH,'//select[@name = "questionid"]')
    login_answer_loc = (By.XPATH,'//input[@name = "answer"]')
    remember_check_loc = (By.XPATH,'//imput[@name = "cookietime"]')
    user_login_error_loc = (By.TAG_NAME, 'i')
    user_login_success_loc = (By.XPATH, '/html/body/div[4]/div/div[3]/div[3]/a')

    #登录链接
    def bbs_login(self):
        self.find_element(*self.bbs_login_user_loc).click()
        sleep(30)
        #self.find_element(*self.bbs_login_button_loc)
    #登录用户名
    def login_username(self,username):
        self.find_element(*self.login_username_loc).send_keys(username)
    #登录密码
    def login_password(self,password):
        self.find_element(*self.login_password_loc).send_keys(password)
    #登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    #登陆问题选择
    def select_question(self,value):
        selector = Select(self.find_element(*self.question_select_loc))
        selector.select_by_value(value)

    #回答问题
    def answer_question(self,str):
        self.find_element(*self.login_answer_loc).send_keys(str)

    #记住密码
    def remember_pwd(self):
        self.find_element(*self.remember_check_loc).click()

    # 登录错误提示
    def user_login_error_hint(self):
        return self.find_element(*self.user_login_error_loc).text

    # 登陆成功返回用户名
    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text

    #定义统一登录入口
    def user_login(self,username = 'Jialee',password = 'cjl123456',flag = False,value = '4',str = '吴亚军',flag2 = False):
        '''获取的用户名密码登录'''
        self.open()
        sleep(10)
        self.bbs_login()
        self.login_username(username)
        self.login_password(password)
        if flag == True:
            self.select_question(value)
            self.answer_question(str)
        else:
            pass
        if flag2 == True:
            self.remember_pwd()
        else:
            pass
        self.login_button()
        sleep(3)







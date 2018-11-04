#coding = utf-8
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from .loginPage import login
from time import sleep
import os
class Shenliao(Page):
    '''
    濠河神聊板块
    '''
    #global tiezi_url,toupiao_url
    tiezi_url = 'http: // bbs.0513.org / forum.php?mod = post & action = newthread & fid = 407 & cedit = yes & extra ='
    toupiao_url = 'http: // bbs.0513.org / forum.php?mod = post & action = newthread & special = 1 & fid = 407 & cedit = yes & extra ='
    #Location
    bbs_shenliao_loc = (By.LINK_TEXT,'濠河神聊')
    bbs_fatie_loc = (By.XPATH,'/html/body/div[7]/div[5]/div/div/div[3]/a/img')
    bbs_xintie_loc = (By.XPATH,'/html/body/div[7]/ul/li[1]/a')
    bbs_toupiao_loc = (By.XPATH,'/html/body/div[7]/ul/li[2]/a')
    #发帖、投票公共定位
    bbs_fenlei_loc = (By.ID,'typeid_ctrl')
    bbs_zhuti_loc = (By.ID,'subject')
    bbs_neirong_loc = (By.XPATH,'/html/body')
    bbs_submit_loc = (By.XPATH,'//*[@id="postsubmit"]')
    bbs_tupian_loc = (By.ID,'e_image')
    bbs_common_loc = (By.XPATH,'/html/body/div[7]/div[2]/div[2]/table/tbody/tr[2]/td[2]/div/ul/li[3]/a')
    bbs_liulan_loc = (By.XPATH,'//*[@id="imgattachnew_1"]')
    bbs_upfile_loc = (By.XPATH,'/html/body/div[7]/div[2]/div[2]/table/tbody/tr[2]/td[2]/div/div[2]/div[1]/div[2]/p[1]/button')
    bbs_confirm_loc = (By.XPATH,'/html/body/div[7]/div[2]/div[2]/table/tbody/tr[2]/td[2]/div/div[2]/div[2]/button')
    bbs_shipin_loc = (By.ID,'e_vid')
    bbs_switch_to_tiezi_loc = (By.XPATH,'/html/body/div[7]/form/div/div/ul/li[1]/a')
    bbs_switch_to_toupiao_loc = (By.XPATH,'/html/body/div[7]/form/div/div/ul/li[2]/a')
    #投票板块特殊定位
    #bbs_maxchoices_loc = (By.XPATH,'//input[@id = "maxchoices"]')
    #bbs_xuanxiang_loc = (By.XPATH,'/html/body/div[7]/form/div/div/div[2]/div[4]/div[1]/div[2]/p[%d]/input')
    #选择分类定位
    def get_class_loc(self,index):
        class_xpath = '/html/body/div[2]/div[2]/ul/li[%d]' % index
        fl_class_loc = (By.XPATH,class_xpath)
        return fl_class_loc
    # 获取选项输入框定位
    def get_xx_loc(self, d):
        xx_xpath = '/html/body/div[7]/form/div/div/div[2]/div[4]/div[1]/div[2]/p[%d]/input' % d
        bbs_xx_loc = (By.XPATH,xx_xpath)
        return bbs_xx_loc
    # 获取删除键定位
    def get_del_xpath(self, d):
        del_xpath = '/html/body/div[7]/form/div/div/div[2]/div[4]/div[1]/div[2]/p[%d]/a' % d
        bbs_del_loc = (By.XPATH,del_xpath)
        return bbs_del_loc
    bbs_add_loc = (By.LINK_TEXT,'+增加一项')

    #进入神聊
    def join_shenliao(self):
        self.find_element(*self.bbs_shenliao_loc).click()
        sleep(10)
    def join_fatie(self):
        ele = self.find_element(*self.bbs_fatie_loc)
        ActionChains(self.driver).move_to_element(ele).perform()
        self.find_element(*self.bbs_xintie_loc).click()
    def join_toupiao(self):
        ele = self.find_element(*self.bbs_fatie_loc)
        ActionChains(self.driver).move_to_element(ele).perform()
        self.find_element(*self.bbs_toupiao_loc).click()
    def switch_to_toupiao(self):
        self.find_element(*self.bbs_switch_to_toupiao_loc).click()
        #sleep(3)
        #if self.driver.current_url == self.toupiao_url:
        #    pass
        #else:
        #    raise Exception('Fail to switch to toupiao.')
    def switch_to_tiezi(self):
        self.find_element(*self.bbs_switch_to_tiezi_loc).click()
        #sleep(3)
        #if self.driver.current_url == self.tiezi_url:
        #    pass
        #else:
        #    raise Exception('Fail to switch to tiezi.')
    def select_fenlei(self,index = '1' ):
        self.find_element(*self.bbs_fenlei_loc).click()
        fl_class_loc = self.get_class_loc(index)
        self.find_element(*fl_class_loc).click()
    def input_subject(self,subjects):
        self.find_element(*self.bbs_zhuti_loc).send_keys(subjects)
    def input_body(self,body = ''):
        self.find_element(*self.bbs_neirong_loc).send_keys(body)
    def upload_img(self):
        self.find_element(*self.bbs_tupian_loc).click()
        self.find_element(*self.bbs_common_loc).click()
        self.find_element(*self.bbs_liulan_loc).click()
        os.system(r"C:\Users\jl\PycharmProjects\Testpro\autoit\upload.exe")
        self.find_element(*self.bbs_upfile_loc).click()
        self.find_element(*self.bbs_confirm_loc).click()
    def submit(self):
        self.find_element(*self.bbs_submit_loc).click()
    def open_ft(self,flag = False):
        login(self.driver).user_login()
        self.join_shenliao()
        if flag == False:
            self.join_fatie()
        else:
            self.join_toupiao()
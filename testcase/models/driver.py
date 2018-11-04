#coding = 'utf-8'

from selenium import webdriver
#from selenium.webdriver import remote
#from selenium.webdriver.common import desired_capabilities


def browser():
    driver = webdriver.Firefox()
    return driver
if __name__ == '__main__':
    dr = browser()
    dr.get('http://www.baidu.com')
    dr.quit()
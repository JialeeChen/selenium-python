#coding = 'utf-8'

from selenium import webdriver
import os

#截图函数
def insert_image(driver,file_name):
    base_dir = os.getcwd()
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\','/')
    base = base_dir.split('/testcase')[0]
    file_path = base+'/report/image/'+file_name
    print(file_path)
    driver.get_screenshot_as_file(file_path)

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('http://www.baidu.com')
    insert_image(driver,'baidu.png')
    driver.quit()
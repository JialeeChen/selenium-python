
import os,sys,unittest
from selenium import webdriver
sys.path.append('./models')
from models.myunit import Mytest
class Test_Download(Mytest):
    '''
    下载文件测试
    '''
    #设置浏览器文件
    fp = webdriver.FirefoxProfile()
    #设置为0代表下载到浏览器默认下载路径，设置成2可保存到指定目录
    fp.set_preference("browser.download.folderList",2)
    #设置是否显示下载界面：True显示，False不显示
    fp.set_preference("browser.download.manager.showWhenStarting",False)
    #设置下载地址，使用os.getcwd()设置为当前文件所在目录
    fp.set_preference("browser.download.dir",os.getcwd())
    #设置下载文件的类型
    fp.set_preference("browser.helperApps.neverAsks.saveToDisk","application/octet-stream")
    #打开浏览器时调用设置文件
    def test1(self):
        driver = webdriver.Firefox(firefox_profile=self.fp)
        driver.get("http://pypi.Python.org/pypi/selenium")
        driver.find_element_by_partial_link_text("selenium-2").click()

if __name__ == '__main__':
    unittest.main()


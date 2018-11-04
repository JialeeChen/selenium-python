#coding = 'utf-8'

from time import sleep
from .driver import browser
from .picshot import insert_image
import unittest

class Mytest(unittest.TestCase):
    global case_count,img_count
    case_count = 0
    img_count = 0
    #计算测试用例的个数，用于显示在测试报告中
    def case_id(self):
        global case_count
        case_count += 1
        if case_count <= 9:
            count = '00' + str(case_count)
        elif case_count <= 99:
            count = '0' + str(case_count)
        else:
            count = str(case_count)
        return count

    #测试用例截图id
    def image_id(self):
        global img_count
        img_count += 1
        if img_count <= 9:
            count = '00' + str(case_count)
        elif img_count <= 99:
            count = '0' + str(case_count)
        else:
            count = str(case_count)
        return count

    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(60)
        self.driver.maximize_window()
        print("case"+str(self.case_id()))
    def tearDown(self):
        img_id = self.image_id()
        file_name = img_id + ".png"
        insert_image(self.driver, file_name)
        print("image/" + file_name)
        self.driver.quit()


#class Test(Mytest):
#    def test_case(self):
#        self.driver.get("http://www.baidu.com")
#        self.driver.find_element_by_id("kw").send_keys("unittest")
#        self.driver.find_element_by_id("su").click()
#        sleep(2)

if __name__ == '__main__':

    unittest.main()


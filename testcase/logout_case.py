#coding = utf-8
import sys,unittest
sys.path.append("./models")
sys.path.append("./page_obj")
from models.myunit import Mytest
from page_obj.logoutPage import logout

class Logout_test(Mytest):
    def test1(self):
        po = logout(self.driver)
        po.user_login()
        po.user_logout()
        po.check_logout()

if __name__ == '__main__':
    unittest.main()


#coding = 'utf-8'
import unittest,random,sys
from time import sleep
sys.path.append('./models')
sys.path.append('./page_obj')
from models.myunit import Mytest
from page_obj.loginPage import login
class loginTest(Mytest):
    '''社区登录测试'''
    def test1(self):
        '''用户名密码为空登录'''
        po = login(self.driver)
        po.user_login('', '')
        self.assertEqual(po.user_login_error_hint(), '抱歉，密码空或包含非法字符')
    def test2(self):
        '''用户名正确，密码为空登录'''
        po = login(self.driver)
        po.user_login('Jialee', '')
        self.assertEqual(po.user_login_error_hint(), '抱歉，密码空或包含非法字符')
    def test3(self):
        '''用户名为空，密码正确'''
        po = login(self.driver)
        po.user_login('', 'cjl123456')
        self.assertIn('登录失败',po.user_login_error_hint())
    def test4(self):
        '''用户名密码不匹配'''
        character = random.choice('aldhjnbfhdvb')
        username = 'test123' + character
        po = login(self.driver)
        po.user_login(username, 'a1234as')
        self.assertIn('登录失败', po.user_login_error_hint())
    def test5(self):
        '''用户名密码正确且未设置登录问题'''
        po = login(self.driver)
        po.user_login()
        self.assertEqual(po.user_login_success(), 'Jialee')
    def  test6(self):
        '''用户名密码正确，登录问题未回答'''
        po = login(self.driver)
        po.user_login() #由于只申请了一个账号，在测试该用例前需手动设置登录问题
        self.assertEqual(po.user_login_error_hint(),'请选择安全提问以及填写正确的答案')
    def test7(self):
        '''用户名密码正确，登录问题非设置的问题'''
        po = login(self.driver)
        ran_val = random.choice('0123567')
        po.user_login(flag=True,value= ran_val)
        self.assertEqual(po.user_login_error_hint(), '请选择安全提问以及填写正确的答案')
    def test8(self):
        '''用户名密码正确，登录问题正确，答案错误'''
        po = login(self.driver)
        character = random.choice('aldhjnbfhdvb')
        answer = '吴亚军' + character
        po.user_login(flag=True,str=answer)
        self.assertEqual(po.user_login_error_hint(), '请选择安全提问以及填写正确的答案')
    def test9(self):
        '''用户名密码正确，登录问题回答正确，成功登录'''
        po = login(self.driver)
        po.user_login(flag=True)
        self.assertEqual(po.user_login_success(), 'Jialee')
    def test10(self):
        '''密码输错5次，15分钟之内无法登录'''
        po = login(self.driver)
        po.user_login(password='nasgf')
        for i in range(0,5):
            po.login_button()
            sleep(3)
        po.user_login() #使用正确的用户名密码仍然登录不上，需要等待
        self.assertEqual(po.user_login_error_hint(), '密码错误次数过多，请 15 分钟后重新登录')


if __name__ == '__main__':
    unittest.main()
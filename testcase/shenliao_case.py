import unittest,sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models.myunit import Mytest
from page_obj.ShenliaoPage import Shenliao
from time import sleep
class Shenliao_Test(Mytest):
    '''
    发帖测试
    '''
    def test1(self):
        '''
        发帖切换到投票按钮测试
        :return:
        '''
        po = Shenliao(self.driver)
        po.open_ft()
        po.switch_to_toupiao()
        sleep(3)
        self.assertEqual(self.driver.current_url,'http: // bbs.0513.org / forum.php?mod = post & action = newthread & special = 1 & fid = 407 & cedit = yes & extra =')

    def test2(self):
        '''
        投票切换到发帖按钮测试
        '''
        po = Shenliao(self.driver)
        po.open_ft(flag=True)
        po.switch_to_tiezi()
        sleep(3)
        self.assertEqual(self.driver.current_url,'http: // bbs.0513.org / forum.php?mod = post & action = newthread & fid = 407 & cedit = yes & extra =')

    def test3(self):
        '''
        分类选择测试（这里只测了一个，其他的省略）
        :return:
        '''
        po = Shenliao(self.driver)
        po.open_ft()
        po.select_fenlei(index='2')
        fl_class_loc = po.get_class_loc('2')
        cls = po.find_element(*fl_class_loc).get_attribute('class')
        self.assertEqual(cls,'current select')

    def test4(self):
        '''
        帖子主题填充测试（符合规定的填充）
        :return:
        '''
        po = Shenliao(self.driver)
        po.open_ft()
        po.input_subject(subjects='测试输入lalala')
        text = po.find_element(*po.bbs_neirong_loc).text
        self.assertEqual(text,'测试输入lalala')

    def test5(self):
        '''
        帖子主题填充测试（填充内容超出范围）
        :return:
        '''
        po = Shenliao(self.driver)
        po.open_ft()
        po.input_subject(subjects='测试输入lalala测试输入lalala测试输入lalala测试输入lalala测试输入lalala测试输入lalala测试输入lalala测试输入lalala测试输入lalala测试输入lalala')
        po.submit()
        text = po.find_element(*po.bbs_neirong_loc).text
        self.assertEqual(text,'输入字符串超出限制')

    def test6(self):
        '''
        帖子主题填充测试（填充内容位空）
        :return:
        '''
        po = Shenliao(self.driver)
        po.open_ft()
        po.input_subject(subjects='')
        po.submit()
        text = po.find_element(*po.bbs_neirong_loc).text
        self.assertEqual(text, '请输入主题内容')

    def test7(self):
        '''
        上传图片测试
        :return:
        '''
        po = Shenliao(self.driver)
        po.open_ft()
        po.upload_img()
        text = po.find_element(*po.bbs_neirong_loc).text
        self.assertEqual(text,'[image]Chrysanthemum.img[/image]')
    #该论坛是我随意找来联系的，因其将账号永久禁言无法继续后面的测试练习
if __name__ == '__main__':
    unittest.main()

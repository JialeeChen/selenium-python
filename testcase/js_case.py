import unittest,sys
from time import sleep
sys.path.append('./models')
from models.myunit import Mytest
class JS_Test(Mytest):
    def scroll_test(self):
        '''
        利用js拖动滚动条
        :return:
        '''
        self.driver.get("http://www.baidu.com")
        self.driver.set_window_size(600,600)
        #搜索
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        sleep(3)
        #通过javascript设置浏览器窗口的滚动条位置
        js = "window.scrollTo(100,450);"
        self.driver.execute_script(js)
        sleep(3)

    def watch_video_test(self):
        '''
        调用js播放视频
        JavaScript函数内置一个arguments对象，包含了函数调用的参数数组
        load()、play()、pause()控制视频的加载、播放、暂停
        :return:
        '''
        self.driver.get("http://videojs.com/")
        video = self.driver.find_element_by_xpath("body/Setion[1]/div/video")
        #返回播放文件地址
        url = self.driver.execute_script("return arguments[0].currentSrc;",video)
        print(url)
        #播放视频
        print("start")
        self.driver.execute_script("return arguments[0].play",video)
        #播放十五秒
        sleep(15)
        #暂停视频
        print("stop")
        self.driver.execute_script("arguments[0].pause()",video)
if __name__ == '__main__':
    unittest.main()
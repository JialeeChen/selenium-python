#coding = 'utf-8'

class Page(object):
    '''
    页面基础类，用于所有页面的继承
    '''
    bbs_url = 'http://bbs.0513.org'
    def __init__(self,driver,base_url = bbs_url):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def _open(self,url):
        url_ = self.base_url + url
        self.driver.get(url_)
        assert self.driver.current_url == url_,'Did not land on %s' % url
    def open(self):
        self._open(self.url)
    def close(self):
        self.driver.quit()

    def find_element(self,*loc):
        return self.driver.find_element(*loc)
    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)
    def script(self,src):
        return self.driver.execute_script(src)

    def iframe(self,iframedid):
        return self.driver.switch_to.frame(iframedid)
    def iframe_out(self):
        return self.driver.switch_to.default_content()

    #def alter(self,alterid):
    #    return self.driver.switch_to.alter(alterid)
    #def alter_accept(self):
    #    return self.driver

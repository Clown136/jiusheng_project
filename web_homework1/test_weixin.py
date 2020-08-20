import shelve
from time import sleep

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TestLiulan:
    def setup(self):
        self.driver = webdriver.Chrome()
        # 隐式等待，
        self.driver.implicitly_wait(5)

    def teradown(self):
        self.driver.quit()

    # shelve python 内置模块，相当于小型的数据库
    def test_cookie(self):

        # 带有登录信息的cookies
        db = shelve.open('./mydbs/cookies')
        cookies = db['cookie']
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

        for cookie in cookies:
            # if 'expiry' in cookie.keys():
            #     cookie.pop("expiry")
            self.driver.add_cookie(cookie)

        # 重新打开  已带有cookie 信息 的微信界面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(2)

        self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]').click()
        self.driver.find_element_by_id("js_upload_file_input").send_keys(r"C:‪\Users\13636\Desktop\mydatas.xlsx")
        assert "mydatas.xlsx" == self.driver.find_element_by_id("upload_file_name").text
        sleep(5)
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class TestDeleteContacts():
    def setup(self):
        caps = {
            "platformName": "android",
            "platformVersion": "6.0",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": 'true',
            "settings[waitForIdleTimeout]": 0  ##缩短动态页面的等待时间
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_contacts(self):
        # 定位到通讯录
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        # 定位到要删除的联系人
        self.driver.find_element(MobileBy.XPATH,"//*[@text='骚权']").click()
        # 进入个人信息页面
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/guk").click()
        # 点击 编辑成员
        self.driver.find_element(MobileBy.XPATH,"//*[@text='编辑成员']").click()
        # 点击删除成员
        self.driver.find_element(MobileBy.XPATH,"//*[@text='删除成员']").click()
        # 点击 确定 删除
        self.driver.find_element(MobileBy.XPATH,"//*[@text='确定']").click()
        ele_contacts = self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/b00")
        # 断言
        assert "骚权" not in ele_contacts



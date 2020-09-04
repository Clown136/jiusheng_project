from appium import webdriver
from time import sleep
from appium.webdriver.common.mobileby import MobileBy

class TestWeiXin():
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

    def test_weixin(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='工作台']").click()

        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/ghc").click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/alq").click()
        result = self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/mn").text
        print(result)
        assert "外出打卡成功" == result




from appium import webdriver

from app_homework3.basepage import BasePage
from app_homework3.main_page import MainPage

class AppWeiXin(BasePage):

    def start(self):
        # if判断语句避免driver 的重复实例化
        if self.driver == None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "hogwarts"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "true"
            caps['settings[waitForIdleTimeout]'] = 1  # 等待页面空闲的时间
            # 客户端代码与 Appium Server 建立连接,同时启动起来欢迎页 appActivity
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            # 隐式等待
            self.driver.implicitly_wait(5)
        else:
            # launch_app() 启动 desirecap 里面设置的appActivity
            self.driver.launch_app()
        return self

    def restart(self):
        # 关闭app
        self.driver.close_app()
        # 重启app
        self.driver.launch_app()

    def stop(self):
        # 停止app
        self.driver.quit()

    def go_to_mian(self) -> MainPage:
        """
        跳转到首页
        :return:
        """
        return MainPage(self.driver)





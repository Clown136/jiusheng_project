from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class BasePage:
    # 定义init方法，实例化driver其他类每次执行时都继承此方法
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
    # 定义封装find方法
    def find(self, locator):
        return self.driver.find_element(*locator)
    # 定义封装finds方法
    def finds(self, locator):
        return self.driver.find_elements(*locator)
    # 定义封装find_and_click方法
    def find_and_click(self, locator):
        self.find(locator).click()
    # 定义封装find_and_sendkeys方法
    def find_and_sendkeys(self, locator, value):
        self.find(locator).send_keys(value)
    # 定义封装wait_and_click显示等待方法
    def wait_and_click(self, element):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))

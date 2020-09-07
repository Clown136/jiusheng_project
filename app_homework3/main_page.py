"""
首页：
"""
from appium.webdriver.common.mobileby import MobileBy
from app_homework3.addressbook import AddressBook
from app_homework3.basepage import BasePage

class MainPage(BasePage):
    _addressbook_demo= (MobileBy.XPATH, "//*[@text='通讯录']")
    def goto_addressbook(self):
        # 定位通讯录
        self.find_and_click(self._addressbook_demo)
        return AddressBook(self.driver)



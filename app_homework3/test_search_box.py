"""
搜索框页面：
"""
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from app_homework3.basepage import BasePage
from app_homework3.personal_information import PersonalInformation


class SearchBox(BasePage):
    _edit_search_demo = (MobileBy.ID, "com.tencent.wework:id/fk1")
    _return_address_book_demo = (MobileBy.ID,"com.tencent.wework:id/gu_")
    def edit_search(self, contact):
        # 搜索框输入内容
        self.find_and_sendkeys(self._edit_search_demo, contact)
        # self.wait_and_click(self._edit_search_demo)
        sleep(2)
        return self

    def goto_personal_information(self, contact):
        eles = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{contact}']")
        beforenum = len(eles)
        if beforenum < 2:
            print("没有可删除的人员")
            return

        eles[1].click()
        return PersonalInformation(self.driver)

    def return_address_book(self):
        # 定位返回按钮
        self.wait_and_click(self._return_address_book_demo)
        self.find_and_click(self._return_address_book_demo)
        from app_homework3.addressbook import AddressBook
        return AddressBook(self.driver)
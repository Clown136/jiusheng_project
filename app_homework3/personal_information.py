"""
联系人个人信息页面：
"""
from appium.webdriver.common.mobileby import MobileBy
from app_homework3.add_members_data import AddMembersData
from app_homework3.basepage import BasePage


class PersonalInformation(BasePage):
    _detailed_information_demo = (MobileBy.ID, "com.tencent.wework:id/guk")
    _data_demo = (MobileBy.XPATH, f"//*[@text='编辑成员']")
    def goto_detailed_information(self):
        # 定位个人信息更多按钮
        self.find_and_click(self._detailed_information_demo)
        return self

    def goto_AddMembersData(self):
        # 定位编辑成员
        self.find_and_click(self._data_demo)
        return AddMembersData(self.driver)
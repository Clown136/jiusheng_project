"""
添加成员：
"""
from appium.webdriver.common.mobileby import MobileBy
from app_homework3.basepage import BasePage


class AddMembers(BasePage):
    _addmembersdata_demo = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    _toast_demo = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")
    def goto_addmembersdata(self):
        # 点位手动输入添加
        self.find_and_click(self._addmembersdata_demo)
        from app_homework3.add_members_data import AddMembersData
        return AddMembersData(self.driver)

    def get_toast(self):
        # 定位toast弹窗
        mytoast = self.find(self._toast_demo).text
        return mytoast




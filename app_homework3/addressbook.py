"""
通讯录：
"""
from appium.webdriver.common.mobileby import MobileBy
from app_homework3.add_members import AddMembers
from app_homework3.basepage import BasePage

class AddressBook(BasePage):
    _add_members_demo = (MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));')
    _search_demo = (MobileBy.ID, "com.tencent.wework:id/guu")
    _member_list_demo = (MobileBy.ID,"com.tencent.wework:id/b00")
    def goto_add_members(self):
        # 滑动点击添加成员
        self.find_and_click(self._add_members_demo)
        return AddMembers(self.driver)

    def goto_search(self):
        # 定位搜索框
        self.find_and_click(self._search_demo)
        from app_homework3.test_search_box import SearchBox
        return SearchBox(self.driver)

    def get_member_list(self):
        # 拿到通讯录内的成员列表
        result1 = self.finds(self._member_list_demo)
        # 列表表达式
        return [member_list.text for member_list in result1]
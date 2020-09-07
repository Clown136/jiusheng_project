"""
添加成员资料页面：
"""
from appium.webdriver.common.mobileby import MobileBy
from app_homework3.basepage import BasePage

class AddMembersData(BasePage):
    _name_demo = (MobileBy.XPATH, "//*[contains(@text, '姓名')]/../*[@text='必填']")
    _gender_demo = (MobileBy.XPATH, "//*[@text='男']")
    _female_demo = (MobileBy.XPATH, "//*[@text='女']")
    _male_demo = (MobileBy.XPATH, "//*[@text='男']")
    _phonenum_demo = (MobileBy.XPATH,
            "//*[contains(@text, '手机') and @class='android.widget.TextView']/..//*[@class='android.widget.EditText']")
    _save_demo = (MobileBy.ID, "com.tencent.wework:id/gur")
    _delete_members_demo = (MobileBy.XPATH, f"//*[@text='删除成员']")
    _click_determine_demo = (MobileBy.XPATH, f"//*[@text='确定']")
    def edit_name(self, name):
        # 定位姓名输入框
        self.find_and_sendkeys(self._name_demo, name)
        return self

    def edit_gender(self, gender):
        # 定位性别点击
        self.find_and_click(self._gender_demo)
        # if判断语句
        if gender == "女":
            # 显示等待
            self.wait_and_click(self._female_demo)
            # 定位女
            self.find_and_click(self._female_demo)
        else:
           # 显示等待
            self.wait_and_click(self._male_demo)
           # 定位男
            self.find_and_click(self._male_demo)
        return self

    def edit_phonenum(self, phonenum):
       # 定位手机号码输入框
        self.find_and_sendkeys(self._phonenum_demo, phonenum)
        return self

    def click_save(self):
        # 定位保存按钮
        self.find_and_click(self._save_demo)
        from app_homework3.add_members import AddMembers
        return AddMembers(self.driver)

    def delete_members(self):
        # 定位删除成员
        self.find_and_click(self._delete_members_demo)
        return self

    def click_determine(self):
        # 显示等待
        self.wait_and_click(self._click_determine_demo)
        # 定位点击确定按钮
        self.find_and_click(self._click_determine_demo)
        from app_homework3.test_search_box import SearchBox
        return SearchBox(self.driver)


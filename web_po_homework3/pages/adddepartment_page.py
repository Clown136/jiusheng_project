from time import sleep
from selenium.webdriver.common.by import By
from web_po_homework3.pages.basepage import BasePage
from web_po_homework3.pages.contact_page import ContactPage


class AddDepartmentPage(BasePage):
    _department_name = (By.CSS_SELECTOR,".ww_inputText:nth-child(2)")
    _choose_department = (By.CSS_SELECTOR,".js_toggle_party_list")
    _jstree_anchor = (By.CSS_SELECTOR,'.qui_dropdownMenu.ww_dropdownMenu.member_colLeft.js_party_list_container')
    _save_button = (By.CSS_SELECTOR,'#__dialog__MNDialog__ [d_ck="submit"]')
    _cancel_button = (By.CSS_SELECTOR,'#__dialog__MNDialog__ [d_ck="cancel"]')
    # 1、定位到添加部门界面中的新建部门的部门名称输入框
    # 选择所在部门
    # 选择获取到部门列表的第一个元素
    def add_new_department(self,name):
        self.find(*self._department_name).send_keys(name)
        self.find(*self._choose_department).click()
        sleep(2)

        elem_list = self.finds(*self._jstree_anchor)
        if elem_list is not None:
            elem_list[0].click()
        sleep(2)
        # return self 是为了实现返回当前页面时依然可以实现链式调用
        return self
    # 定义一个保存的方法
    # 点击确定按钮
    def save_department(self):
        self.find(*self._save_button).click()
        return ContactPage(self.driver)
    # 定义一个取消保存的方法
    # 点击取消按钮
    def cancel_department(self):
        self.find(*self._cancel_button).click()
        return ContactPage(self.driver)
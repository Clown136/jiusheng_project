from time import sleep
from selenium.webdriver.common.by import By
from web_po_homework3.pages.basepage import BasePage

class ContactPage(BasePage):
    _top_addBtn = (By.CSS_SELECTOR,".member_colLeft_top_addBtn")
    _create_party = (By.CSS_SELECTOR,".js_create_party")
    _jstree_anchor = (By.CSS_SELECTOR,".jstree-anchor")
    # 1 、定位 点击添加部门“+”号按钮  2 、定位 点击“添加部门”
    def go_to_department(self):
        from web_po_homework3.pages.adddepartment_page import AddDepartmentPage
        self.find(*self._top_addBtn).click()
        self.wait_for_clickable(self._top_addBtn)
        self.find(*self._create_party).click()
        # 对 AddDepartmentPage 类进行实例化,表示业务逻辑的转换关系
        return AddDepartmentPage(self.driver)

    def get_department_list(self):
        sleep(5)
        ele = self.finds(*self._jstree_anchor)
        return [name.text for name in ele]


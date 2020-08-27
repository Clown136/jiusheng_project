from time import sleep
from web_po_homework3.pages.main_page import MainPage

class TestDepartment:

    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.driver.quit()
    # 1.从首页跳转到通讯页面  2.跳转到点击添加部门页面  3.新建添加部门   4.点击保存
    def test_add_department(self):
        namelist = self.main.go_to_contact().go_to_department().add_new_department("酒笙").save_department().get_department_list()
        assert "酒笙" in namelist
    # 1.从首页跳转到通讯页面  2.跳转到点击添加部门页面  3.新建添加部门   4.点击取消
    def test_add_department_fail(self):
        namelist = self.main.go_to_contact().go_to_department().add_new_department("千世").cancel_department().get_department_list()
        print(namelist)
        assert "千世" not in namelist



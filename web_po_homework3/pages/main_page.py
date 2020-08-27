from selenium.webdriver.common.by import By

from web_po_homework3.pages.adddepartment_page import AddDepartmentPage
from web_po_homework3.pages.basepage import BasePage
from web_po_homework3.pages.contact_page import ContactPage

class MainPage(BasePage):

    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    _add_member = (By.XPATH,"//*[@id='_hmt_click']/div[1]/div[4]/div[2]/a[1]")
    _menu_contacts = (By.ID,"menu_contacts")
    # 点击进入通讯录
    def go_to_contact(self):
        # 对contactpage 类进行实例化，表示业务逻辑的转换关系
        self.find(*self._menu_contacts).click()
        return ContactPage(self.driver)


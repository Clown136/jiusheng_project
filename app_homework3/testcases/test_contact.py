from app_homework3.app_weixin import AppWeiXin


class TestContact:

    def setup(self):
        """
        应用的启动
        :return:
        """
        # 实例化AppWeiXin
        self.appweixin = AppWeiXin()
        # 打开app到首页
        self.main = self.appweixin.start().go_to_mian()

    def tearsown(self):
        """
          应用的关闭
          :return:
          """
        # 关闭app
        self.appweixin.stop()

    def test_addcontact(self):
        # 成员姓名
        name = "cxl11"
        # 成员性别
        gender = "男"
        # 成员号码
        phonenum = "15901012214"
        # 1、打开app到首页 2、从首页跳转到通讯录 3、从通讯录跳转到添加成员 4、从添加成员添砖到填写成员资料页面 5、填写姓名 6、填写性别
        # 7、填写手机号码 8、点击保存 9、弹出toast弹窗
        mypage = self.main.goto_addressbook().goto_add_members().goto_addmembersdata().edit_name(name).edit_gender(gender)\
            .edit_phonenum(phonenum).click_save().get_toast()
        # 断言
        assert "添加成功" == mypage

    def test_deletecontact(self):
        # 要删除联系人的姓名
        contact = 'cxl11'
        # 1、打开app到首页 2、从首页跳转到通讯录 3、从通讯录跳转到搜索框页面 3、从搜索框页面跳转到个人信息页面 4、点击个人信息页面更多
        # 5、点击编辑成员 6、添砖到成员资料页面 7、点击删除成员 8、点击确定 完成后返回到自动返回到搜索框页面 9、搜索框页面点击返回
        # 9、搜索框页面点击返回跳转到通讯录页面 10、获取联系人列表信息
        mylist1 = self.main.goto_addressbook().goto_search().edit_search(contact).goto_personal_information(contact)\
            .goto_detailed_information().goto_AddMembersData().delete_members().click_determine()\
            .return_address_book().get_member_list()
        # 断言
        assert "cxl11" not in mylist1






from jiekou_api_homework2.api_demo.label import Label
from jiekou_api_homework2.api_demo.weworks import WeWorks


class TestLabel():

    def setup(self):
        # 定义setup方法，用例执行前先执行实例化方法
        weworks = WeWorks()
        self.label = Label()
        self.token = weworks.get_token()

    def test_create_label(self):
        # 调用创建标签方法，并传入token值与id
        self.label.create_label(self.token,2)
        list = self.label.get_label_memberlist(self.token)
        # 断言list中tagname字段下的第一个值是否等于 "标签"
        assert list["taglist"][0]["tagname"] == "标签"

    def test_update_label(self):
        # 调用更新标签方法，并传入token值与id
        self.label.update_label(self.token,2)
        list = self.label.get_label_memberlist(self.token)
        # 断言list中tagname字段下的第一个值是否等于 "标签1"
        assert list["taglist"][0]["tagname"] == "标签1"

    def test_delete_label(self):
        # 调用删除标签方法，并传入token值与id
        self.label.delete_label(self.token,2)
        list = self.label.get_label_memberlist(self.token)
        # 断言删除标签列表后，获取到的标签列表长度是否等于0
        assert len(list["taglist"]) == 0

    def test_get_label_member_list(self):
        # 调用获取标签列表方法，并传入token值
        self.label.get_label_memberlist(self.token)

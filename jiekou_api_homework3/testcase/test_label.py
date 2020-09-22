import yaml
from jiekou_api_homework3.api.label import Label


class TestLabel():
    # 定义setup方法，每次方法执行前先执行setup
    def setup(self):
        # 实例化label
        self.label = Label()
        # 调用yaml方法打开yaml文件赋值给变量config_infor
        config_infor = yaml.safe_load(open("config.yaml"))
        # 这里调用label中的get_token方法（传入上方yaml文件对应的字段）获取到企业微信的token值
        self.label.get_token(config_infor["token"]["corp_secret"])

    def test_create_label(self):
        # 调用创建标签方法，并传入token值与id
        self.label.create_label(2)
        list = self.label.get_label_memberlist()
        # 调用封装jsonpath方法，传入对应的参数（json格式参数，jsonpath表达式）
        name = self.label.base_jsonpath(list, "$..tagname")
        # 断言字符串"测试"是否在name当中
        assert  "标签" in name

    def test_update_label(self):
        # 调用更新标签方法，并传入token值与id
        self.label.update_label(2)
        list = self.label.get_label_memberlist()
        # 调用封装jsonpath方法，传入对应的参数（json格式参数，jsonpath表达式）
        name = self.label.base_jsonpath(list, "$..tagname")
        # 断言list中tagname字段下的第一个值是否等于 "标签1"
        assert  "标签1" in name

    def test_delete_label(self):
        # 调用删除标签方法，并传入token值与id
        self.label.delete_label(2)
        list = self.label.get_label_memberlist()
        # 调用封装jsonpath方法，传入对应的参数（json格式参数，jsonpath表达式）
        tagid_id = self.label.base_jsonpath(list, "$..taglist")
        # 断言删除标签列表后，获取到的标签列表长度是否等于0
        assert 2 not in tagid_id

    def test_get_label_member_list(self):
        # 调用获取标签列表方法，并传入token值
        self.label.get_label_memberlist()
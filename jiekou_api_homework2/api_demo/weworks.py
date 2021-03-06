import requests

class WeWorks():

    def get_token(self):
        """
        获取token的关键参数：企业ID，通讯录凭证密钥
        :return:
        """
        corpid = "wwf13bec81e4b55c43"
        corpsecret = "w3hXuclbFpDyyuM46bvu9T11xQc8MhHeXU-m5JPsiuA"
        # 在url中传入上方定义的关键参数
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        # 发送get请求并追加参数
        r = requests.get(url=url)
        # 将请求中josn字段下的access_token字段赋值给全局变量token
        self.token = r.json()["access_token"]
        # return token，实现链式调用
        return self.token
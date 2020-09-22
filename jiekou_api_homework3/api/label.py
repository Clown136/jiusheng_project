import requests
from jiekou_api_homework3.api.wework import WeWork

class Label(WeWork):
    # 定义创建标签方法
    def create_label(self,tagid):
        # 请求的url
        create_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}"
        # 请求参数
        data = {
            "tagname": "标签",
            "tagid": tagid
        }
        # 请求信息
        req = {
            "url" : create_url,
            "method" : "post",
            "json" : data
        }
        # 因为企业微信所有的接口需使用HTTPS协议、JSON数据格式、UTF8编码。接口说明格式如下：
        # 所以在传请求体的时候 尽量使用json参数
        r = self.send_requests(req)
        return r.json()

    # 定义更新标签方法
    def update_label(self,tagid):
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}"
        data = {
            "tagid": tagid,
            "tagname": "标签1"
        }
        # 请求信息
        req = {
            "url": update_url,
            "method": "post",
            "json": data
        }
        r = self.send_requests(req)
        return r.json()

    # 定义删除标签方法
    def delete_label(self,tagid):
        delete_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={tagid}"
        # 请求信息
        req = {
            "url": delete_url,
            "method": "get"
        }
        r = self.send_requests(req)
        return r.json()

    # 定义获取标签列表方法
    def get_label_memberlist(self):
        get_label_memberlist_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        # 请求信息
        req = {
            "url": get_label_memberlist_url,
            "method": "get"
        }
        r = self.send_requests(req)
        return r.json()

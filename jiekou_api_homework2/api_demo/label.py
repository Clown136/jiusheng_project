import requests

class Label:
    # 定义创建标签方法
    def create_label(self,token,tagid):

        create_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={token}"
        data = {
            "tagname": "标签",
            "tagid": tagid
        }
        # 因为企业微信所有的接口需使用HTTPS协议、JSON数据格式、UTF8编码。接口说明格式如下：
        # 所以在传请求体的时候 尽量使用json参数
        r = requests.post(url=create_url, json=data)
        return r.json()

    # 定义更新标签方法
    def update_label(self,token,tagid):
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={token}"
        data = {
            "tagid": tagid,
            "tagname": "标签1"
        }
        r = requests.post(url=update_url, json=data)
        return r.json()

    # 定义删除标签方法
    def delete_label(self,token,tagid):
        delete_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={token}&tagid={tagid}"
        r = requests.get(url=delete_url)
        return r.json()

    # 定义获取标签列表方法
    def get_label_memberlist(self,token):
        get_label_memberlist_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={token}"
        r = requests.get(url=get_label_memberlist_url)
        return r.json()

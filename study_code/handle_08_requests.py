# encoding:utf-8
# author:wangzhicheng
# time:2019/12/19 9:58
# file:handle_08_requests.py


import requests, json
from TestScripts.handle_02_yaml import do_yaml


class HandleRequest:
    """requests请求库"""

    def __init__(self):

        self.res = requests.Session()

    def add_headers(self, headers=do_yaml.read_yaml("requests", "headers")):
        self.res.headers.update(headers)

    def handle_request(self, method, url, datas, is_json=True, **kwargs):
        """
        datas的3中格式，字典，字符串字典，json
        """
        # method全部小写
        method = method.lower()

        # 如果 datas是一个字符串，先用json.loads()给它转换，如果是json格式的可以直接转成字典
        # 如果是字符串字典就会异常，使用eval转成字典

        if isinstance(datas, str):
            try:
                datas = json.loads(datas)
            except Exception as e:
                datas = eval(datas)


        #如果是一个字典那更好，直接走下面代码

        if method == "get":

            result = self.res.request(method=method, url=url, params=datas,**kwargs)

        elif method in ("post", "patch", "delete", "put"):
            #post、patch 也可以用www form 表单格式数据，所以这里做了个is_json判断，如果请求数据要求格式是json格式就是True

            if is_json:
                result = self.res.request(method=method, url=url, json=datas, **kwargs)

            else:
                result = self.res.request(method=method, url=url, data=datas, **kwargs)
        else:
            result = None
            print(f"不支持{method}请求方式！")

        return result

    def close(self):
        self.res.close()


if __name__ == '__main__':
    do_handles = HandleRequest()

    # method="post"
    # url="http://api.lemonban.com/futureloan/member/login"
    #
    # datas='{"mobile_phone":"18774850123","pwd":"000000000"}'
    #
    # do_handles.add_headers()
    #
    # result=do_handles.handle_request(method,url,datas)
    #
    # print(result)
    # do_handles.close()


    method = "post"
    url = "https://store.test.sunmi.com/printer/api/config/print/update"
    datas = {"sn": "N301P98Q40093",
             "merchant_id": 9601,
             "user_id": 44587,
             "settings": {"density": "1", "copies": {"new_order": "2", "cancel_order": 5},
                          "header_url": "https://test.cdn.sunmi.com/IMG/PRINTER/tmp_123_header.png",
                          "footer_url": "https://test.cdn.sunmi.com/IMG/PRINTER/tmp_123_header.png",
                          "inspection_page_language": 2}
             }

    result=do_handles.handle_request(method,url,datas)

    print(result.text)

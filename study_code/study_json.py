# author:manman
# __time__:2020/9/19 10:56
# __file__:study_json.py


import json

class JsonStudy:
    """
    json.load()
    json.loads()
    json.dump()
    json.dumps()
    """

    json_data = '{"name": "zhicheng成", "age": 18, "money": 100.5,"ww":null}'
    str_list_data = '["hello", "zhicheng成", 18, 20.5]'

    dict_data = {"dict": "zhicheng成", "age": 18, "money": 100.5, "isok": True, "isno": False, "house": None}
    tuple_data = ("tuple", "zhicheng成", 18, 20.5,True,False,None)
    list_data = ["list", "zhicheng成", 18, 20.5,True,False,None]

    value1 = json.loads(json_data)
    value2 = json.loads(str_list_data)

    switch_dict1 = json.dumps(dict_data,ensure_ascii=False)  #中文正常显示
    switch_dict2 = json.dumps(tuple_data)
    switch_dict3 = json.dumps(list_data)


if __name__ == '__main__':

    js = JsonStudy()
    print(js.value1)
    print(js.value2)
    print(js.switch_dict1)
    print(repr(js.switch_dict1))
    print(repr(js.switch_dict2))
    print(repr(js.switch_dict3))

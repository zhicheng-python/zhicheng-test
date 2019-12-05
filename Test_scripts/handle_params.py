# encoding:utf-8
# author:wangzhicheng
# time:2019/11/29 19:22
# file:handle_params.py

import re

from Test_scripts.handle_yaml import do_yaml
from Test_scripts.handle_path import do_path
from Test_scripts.handle_phone import do_phone


class HandleParams:


    def register_params(self, data):

        if "{no_register_phone}" in data:
            data = re.sub(r"{no_register_phone}", str(do_phone.get_no_register_phone()), data)

        if "{exist_phone}" in data:
            data = re.sub(r"{exist_phone}", str(do_yaml.read_yaml("loan_user", "手机号", do_path.write_yaml_path)), data)

        if "{exist_pwd}" in data:

            data = re.sub(r"{exist_pwd}", str(do_yaml.read_yaml("loan_user", "密码", do_path.write_yaml_path)), data)

        return data


    def read_params(self,data):

        data=self.register_params(data)


        return data



do_params = HandleParams()
if __name__ == '__main__':
    pass

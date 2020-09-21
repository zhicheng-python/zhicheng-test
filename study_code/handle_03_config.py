#encoding:utf-8
#author:wangzhicheng
#time:2019/12/18 10:36
#file:handle_03_config.py


from configparser import ConfigParser
from TestScripts.handle_01_path import do_path



class HandleConfig:
    """读写配置文件config文件后缀的类"""

    def read_config(self,section,option,path=do_path.read_config_path):

        #创建config对象
        config = ConfigParser()
        #读取配置文件
        config.read(path,encoding="utf-8")
        #返回数据
        return config[section][option]


    def write_config(self,data,path=do_path.write_config_path):

        #创建config对象
        config = ConfigParser()

        #打开配置文件，如果没有就创建一个配置文件
        with open(path,"w",encoding="utf-8") as f:
            #把config当成一个字典，遍历data的key，把key作为config的key
            #把data[key]也就是value作为config的value
            #最后写入config.write 配置文件
            for k in data:
                config[k]=data[k]

            config.write(f)



do_config=HandleConfig()

if __name__ == '__main__':
    value=do_config.read_config("Test_3","test_3")
    print(value)

    data={"Test_4":{"test_4":"is_test_4"}}
    do_config.write_config(data)


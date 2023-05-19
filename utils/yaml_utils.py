import yaml
from utils.config import PATH
import os


class YamlUtil:
    '''
    数据驱动
    获取yml文件中的接口测试数据
    '''

    def __init__(self, file_name):
        self.file_name = file_name

    # @property改变方法的属性，直接可以通过方法的名字调用不用加括号
    @property
    def read_yaml(self):
        path = os.path.join(PATH, f'case/{self.file_name}')
        '''os.path.join 函数将多个路径组合成一个完整的路径'''
        with open(path, encoding='utf8') as f:
            return yaml.safe_load(f)
        # yaml.safe_load 从yaml文件加载数据


if __name__ == '__main__':
    print(YamlUtil('data.yml').read_yaml)

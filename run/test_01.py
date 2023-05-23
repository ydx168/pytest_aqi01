from utils.yaml_utils import YamlUtil
from utils.requests import req
import unittest


class TestBili(unittest.TestCase):

    def setUp(self) -> None:
        self.yaml_data = YamlUtil('data.yml').read_yaml

    def test_search(self):
        data = self.yaml_data['test_search']
        url, method, params = data['url'], data['method'], data['params']
        re = req.call(url, method, params=params)
        print(re)


if __name__ == '__main__':
    unittest.main(verbosity=2)

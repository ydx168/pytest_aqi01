import requests
from utils.decorators import request_check
from utils.config import host

class RequEsts:

    def __init__(self):
        self.ses = requests.session()
        self.ses.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
                                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    @request_check
    def call(self, url, method, **kwargs):
        params = kwargs['params'] if 'params' in kwargs else None
        data = kwargs['data'] if 'data' in kwargs else None
        json = kwargs['json'] if 'json' in kwargs else None
        files = kwargs['files'] if 'files' in kwargs else None
        return self.ses.request(method, host+url, params=params, data=data, files=files, json=json)

req=RequEsts()



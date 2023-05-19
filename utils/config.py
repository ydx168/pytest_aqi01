import os

'''
环境配置测试环境，生产环境，预上线环境
'''
PATH = os.path.dirname(os.path.dirname(__file__))

ENU = {
    'live': {
        'https://www.bilibili.com'
    },
    'uat': {
        ''
    },
    'sit': {
        ''
    }
}

env_name = 'live'
host1 = ENU[env_name]
host = next(iter(host1))

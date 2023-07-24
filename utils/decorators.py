from functools import wraps
import logging


def request_check(func):
    @wraps(func)
    def check(*args, **kwargs):
        if args[2] not in ['get', 'post', 'put', 'delete']:
            raise ValueError(f'请求方式错误或请求方式不存在：{args[2]}')

        re = func(*args, **kwargs)
        if re.status_code != 200:
            raise ValueError(f'请求接口异常，当前状态码为：{re.status_code} ')
        logging.info(f'接口{args[1]} 请求成功,返回值为：{re.text}')
        return re
    return check


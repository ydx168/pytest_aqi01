import os
import time

print(os.getcwd())
# getcwd获取当前目录

print(os.listdir('D:/cesetest/pytest_aqi/run'))
# 获取当前目录下的文件及文件夹，返回一个列表

print(os.name)
# 获取当前的操作系统，windows为nt，linux和unix系统为posix

print(os.path.abspath('los.py'))
# 返回文件的绝对路径

print(os.path.exists('los.py'))
# 判断文件是否存在，存在True，不存在为False

print(os.path.getsize('los.py'))
# 检查文件的大小

bb=os.path.getmtime('D:/cesetest/pytest_aqi/run/test_01.py')
# 获取文件最后一次修改时间，以时间戳的方式返回
print(bb)
aa=time.localtime(bb)
print(aa)
AA=time.strftime("%Y-%m-%d %H:%M:%S",aa)
print(AA)
# 使用time库将时间戳转化为字符形式

aa=os.path.getctime('D:/cesetest/pytest_aqi/logs/los.py')
# 获取文件创建时间，以时间戳的方式返回

bb=time.localtime(aa)
S=time.strftime("%Y-%m-%d %H:%M:%S",bb)
print(S)

aa=os.path.getatime('D:/cesetest/pytest_aqi/logs/los.py')
# 获取文件最后的访问时间，以时间戳的形式返回

b=time.localtime(aa)
A=time.strftime("%Y-%m-%d %H:%M:%S",b)
print(A)



# os.remove('D:/cesetest/pytest_aqi/aaa')
# 删除指定文件

# os.mkdir('D:/cesetest/pytest_aqi/aaa')
# 指定目录下创建一个文件夹

# os.rmdir('D:/cesetest/pytest_aqi/aaa')
# os.removedirs('D:/cesetest/pytest_aqi/aaa')
# 删除指定目录下的空文件夹




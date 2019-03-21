import time
import datetime
a=time.time()

b=time.localtime(a)
print(b)
c=time.strftime('%Y-%m-%d %H:%M:%S')
print(c)
d=time.strftime('%Y')
print(d)
print('-----------datetime模块-----------')
a=datetime.datetime.now().strftime("%Y")
print(a)
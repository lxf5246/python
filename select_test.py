"""
select 函数示例
"""

from select import select
from socket import *

s1 = socket()
s1.bind(('0.0.0.0',8888))
s1.listen(3)

s2 = socket(AF_INET,SOCK_DGRAM)
s2.bind(('0.0.0.0',8889))

f = open('test.log','r+')

print("监控IO")
rs,ws,xs = select([s1,s2,f],[s2],[])
print("rlist:",rs)
print("wlist:",ws)
print("xlist:",xs)
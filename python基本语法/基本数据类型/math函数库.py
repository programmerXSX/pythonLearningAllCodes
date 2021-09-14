#math函数库
from math import *
x, y, z = 10.1, 20.9, 30.0
print("x的绝对值{}".format(fabs(x)))
print("x与y的模{}".format(fmod(x,y)))#求余%
print("向上取整{}".format(ceil(x)))
print("向下取整{}".format(floor(int(x))))
print("x的阶乘{}".format(factorial(int(x))))
print("x与y的最大公约数{}".format(gcd(int(x),int(y))))
print("正A弦{}余弦正切".format(sin(pi/3)))
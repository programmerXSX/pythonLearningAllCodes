#基本数字类型

#整型
a = 10
print("10的十进制是a = {}".format(a) )
b = bin(a)      #转二进制
print("10的二进制是b = {}".format(b))
c = oct(a)      #转八进制
print("10的八进制是c = {}".format(c))
d = hex(a)      #转十六进制
print("10的十六进制是d = {}".format(d))

#浮点型
a, b, c= 2.5, 6, 4.3e-3
import math
print(math.pi)#常数Π
print(math.e)#自然对数的底数e

#复数类型
c = 12.3 + 4j
a, b = c.real,c.imag
#复数的实数部分和虚数部分
print(a,b)
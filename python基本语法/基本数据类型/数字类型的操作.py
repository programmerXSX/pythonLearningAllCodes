#数字类型的操作
x, y = 10, 2.5
print("x = 10, y = 2.5")
print("x + y = {}".format(x+y))
print("x - y = {}".format(x-y))
print("x * y = {}".format(x*y))
print("x / y = {}".format(x/y))     #x与y之商
print("x // y = {}".format(x//y))   #x与y的整数商
print("x % y = {}".format(x%y))     #求余
print("x ** y = {}".format(x**y))   #x的y次方

#内置的数字运算函数
print("x的绝对值是{}".format(abs(x)))
print("x/y的元组形式是：{}".format(divmod(x,y)))
print("对y四舍五入是：{}".format(round(y,1)))
print("x,y最大值是{}".format(max(x,y)))
print("x,y最小值是{}".format(min(x,y)))

#内置数字类型转换函数
x, y = 2.555, 10
print("x转换为整型是：{}".format(int(x)))
print("y转换为浮点型是：{}".format(float(y)))
print("生成一个复数：{}".format(complex(x,y)))
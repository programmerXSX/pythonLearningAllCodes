a = 1.0
print(a) # 输出 1.0
print(1.0) # 与上面的输出相同，输出 1.0

a = 1.0
print("a = %g" % a) # 输出 1.0  因为1.0是浮点数，所以使用 %g

a = 1.0
b = False
c = "python"
print(a, b, c)
print("*" * 20)  # 表示连续输出4个 *  (记住这个小窍门哟)

print("print 函数和", "format函数", "哪一个难一点呢？")
print("*" * 20)  # 表示连续输出20个 *  (记住这个小窍门哟)
# 如果是使用print函数输出多个变量，后面的变量需要用括号
print("a = %g b = %d c = %s" % (a, b, c))


#设置不换行
print(1)
print(2)
print(3)
print(4)
print(5)
print("*"*20) #表示连续输出20个 *  (记住这个小窍门哟)
#print函数中有一个缺省参数，默认是换行，直接把换行改为其他字符即可
#比如：改为空格做测试,end中的参数可以设置为自己喜欢的格式，不一定是空格
print(1,end=" ")
print(2,end=" ")
print(3,end=" ")
print(4,end=" ")
print(5)
print(1,end="")
print(2,end="")
print(3,end="")
print(4,end="")
print(5)


#format（）函数用法
str = "{}{}{}{}".format(5,6,7,8) # {} 下标没有设置，默认为 0 ，1，2，3
str1 = "{0}{1}{2}{3}".format(5,6,7,8)
str2 = "{0}{0}{2}{3}".format(5,6,7,8) # {} 根据下标索引取值
str3 = "{3}{0}{2}{1}".format(5,6,7,8)
print(str)
print(str1)
print(str2)
print(str3)



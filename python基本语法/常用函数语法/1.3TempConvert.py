# 1.3TempConvert.py
# 函数封装

def tempConvert(Valuestr):      #使用关键字def定义函数，并传入一个参数
    if Valuestr[-1] in ['F', 'f']:
        C = (eval(Valuestr[0:-1]) - 32)/1.8
        print("转换后的温度是：{:.2f}C".format(C))
    elif Valuestr[-1] in ['C','c']:
        F = 1.8*(eval(Valuestr[0:-1]))+32
        print("转换后的温度是：{:.2f}F".format(F))
    else:
        print("输入格式错误")
TempStr = input("请输入带有符号的温度值：")
tempConvert(TempStr)


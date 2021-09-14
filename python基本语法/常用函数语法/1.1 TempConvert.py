#e1.1TmepConvert.py
TempStr = input("请输入带有符号的温度值")
if TempStr[-1] in ['F','f']:
    C = (eval(TempStr[0:-1]) - 32)/1.8
#eval()函数，将输入的字符串解析为python可执行语句
#如果直接输入”hello“，eval会去掉双引号而解析为hello，由于之前没有定义这个变量
#编译器会报错
#而如果输入”‘hello’”，编译器会解析为‘hello’，是一个字符串
#eval多种功能参见《printyuformat函数.py》

    print("转换后温度是{:.2f}C".format(C))
#format()通过（）里的参数与前面的{}相对应
#将参数按顺序传入前面的{}之中
#:.2f是输出格式，表示输出数值取两位小数
elif TempStr[-1] in ['C','c']:
    F = 1.8 *eval(TempStr[0:-1])+ 32
    print("转换后温度是{:.2f}F".format(F))
else:
    print("输入格式错误！！")

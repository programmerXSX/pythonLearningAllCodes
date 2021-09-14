# CalBMI.py
height, weight = eval(input("请输入身高（米）和体重（千克）[用逗号隔开]："))
BMI = weight / (height ** 2)
print("BMI的数值为{:.2f}".format(BMI))
who, dom = "", ""
if BMI < 18.5:
    who, dom = "偏瘦", "偏瘦"
elif 18.5 <= BMI < 24:
    who, dom = "正常", "正常"
elif 24 <= BMI < 25:
    who, dom = "正常", "  偏胖"
elif 25 <= BMI < 28:
    who, dom = "偏胖", "偏胖"
elif 28 <= BMI < 30:
    who, dom = "偏胖", "肥胖"
else:
    who, dom = "肥胖", "肥胖"
print("BMI指标为国际‘{0}’，国内‘{1}’".format(who, dom))

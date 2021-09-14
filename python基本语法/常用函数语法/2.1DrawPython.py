#2.1DrawPython

import turtle                       #调用绘图函数库
turtle.setup(650,350,200,200)
#设置主窗口的大小和位置 ，四个参数(width,height,startx,starty)
#width:窗口宽度，整数表示像素值：小数表示窗口宽度与屏幕比例
#height:窗口高度，整数表示像素值；小数表示高度与屏幕比例
#startx:窗口左侧与屏幕左侧的距离，如果值是None，窗口位于水平中央
#starty:窗口顶部与屏幕顶部的距离，如果值是None，窗口位于垂直中央
turtle.penup()
#抬起画笔，之后移动画笔不会绘制形状，无参数， 别名：turtle.pu(), turtle.up()
turtle.fd(-250)
#控制画笔前进一段距离，别名：turtle.forward(distance)
turtle.pendown()
#落下画笔，之后移动画笔会绘制形状，无参数， 别名：turtle.pd(), turtle.down()
turtle.pensize(25)
#设置画笔宽度，无参数输入时返回当前画笔宽度，别名：turtle.width()
turtle.pencolor("purple")
#设置画笔颜色，无参数输入时返回当前画笔颜色，可传入颜色英文名字的字符串
#也可传入RGB颜色[0,255],0表示黑色，255是白色
turtle.seth(-40)
#用来改变画笔绘制方向，别名：turtle.setheading(to_angle)
#参数表示绝对方向角度值，参考平面直角坐标系
for i in range(4):
#for语句的循环格式如下：for i in range(<循环次数>):
    turtle.circle(40,80)
    #表示绘制一个弧形，参数为（radius,extent）,radius为正逆时针，角度为负顺时针
    #extent表示绘制角度，当extent为None时画圆
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()




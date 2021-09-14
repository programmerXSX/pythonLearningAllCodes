#同心圆
from turtle import *
def DrawRoud(radius):
    pensize(2)
    pencolor("red")
    seth(0)
    speed("fastest")
    pendown()
    circle(radius)
    penup()
    seth(-90)
    fd(20)
    seth(0)
for i in range(10):
    DrawRoud(20*i)
done()


#4.1TextProgressBar
import time
scale = 10
print("——————执行开始——————")
for i in range(scale + 1):
    a, b = '**' * i, '..' * (scale - i)
    c = (i/scale)*100
    print("[{}->{}]{:^3.0f}%".format( a, b, c))
    time.sleep(0.1)
print("———————执行结束——————")
#3.1 DayDayUp

import math
dayup = math.pow((1.0 + 0.001),365)
#pow函数，pow(x,n),x的n次方
daydown = math.pow((1.0-0.001),365)
print("向上：{:.2f},向下：{:.2f}.".format(dayup,daydown))
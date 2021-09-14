# DayDayUp
# 双休日休息
def dayUP(dayfactor):
    dayup = 1.0
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + dayfactor)
    return dayup


dayfactor = 0.01
while (dayUP(dayfactor) < 37.78):
    dayfactor += 0.001
print("每天的努力参数是：{:.2f}".format(dayfactor))

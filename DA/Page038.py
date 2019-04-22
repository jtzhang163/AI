# 绘制散点图
# 假设通过爬虫你获取到了北京2016年3,10月份每天白天的最高气温(分别位于列表a,b),那么此时如何寻找出气温和随时间(天)变化的某种规律?
# a = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
# b = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="c:/windows/fonts/simhei.ttf")

plt.figure(figsize=(20, 8), dpi=80)

y3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

x3 = range(1, 32)
x10 = range(51, 82)

x = list(x3) + list(x10)

plt.scatter(x3, y3, label="3月", color="orange")
plt.scatter(x10, y10, label="10月", color="red")

x_ticks = ["3月{}日".format(i) for i in x3] + ["10月{}日".format(i-50) for i in x10]

plt.xticks(x[::3], x_ticks[::3], fontproperties=my_font, rotation=45)

plt.legend(prop=my_font, loc="best")

plt.savefig("./output_file/page038.png")
plt.show()

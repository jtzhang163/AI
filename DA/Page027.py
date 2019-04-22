# 那么问题来了:
# 如果列表a表示10点到12点的每一分钟的气温,如何绘制折线图观察每分钟气温的变化情况?
# a= [random.randint(20,35) for i in range(120)]

from matplotlib import pyplot as plt
from matplotlib import font_manager
import random

# 设置中文字体
my_font = font_manager.FontProperties(fname="c:/windows/fonts/simhei.ttf")

random.seed(10)  # 设置随机种子，使不同时刻生成的结果都一样
a = [random.randint(20, 35) for i in range(120)]

plt.figure(figsize=(20, 6), dpi=80)

_x = range(120)
_y = a

plt.plot(_x, _y)

# python 数字格式化 {:0>2d} 数字补零 (填充左边, 宽度为2) eg: 05
_x_ticks = ["10点{:0>2d}分".format(i) for i in _x if i < 60]
_x_ticks += ["11点{:0>2d}分".format(i-60) for i in _x if i >= 60]

# 切片，使刻度变稀疏
# rotation：字符串旋转显示
plt.xticks(_x[::5], _x_ticks[::5], rotation=45, fontproperties=my_font)

# 设置图像标题，X、Y轴标签
plt.xlabel("时间", fontproperties=my_font)
plt.ylabel("温度", fontproperties=my_font)
plt.xlabel("10点到12点气温变化图", fontproperties=my_font)

plt.show()

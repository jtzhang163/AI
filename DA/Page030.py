# 假设大家在30岁的时候,根据自己的实际情况,统计出来了你和你同桌各自从11岁到30岁每年交的女(男)朋友的数量如列表a和b,请在一个图中绘制出该数据的折线图,以便比较自己和同桌20年间的差异,同时分析每年交女(男)朋友的数量走势
# a = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
# b = [1,0,3,1,2,2,3,3,2,1 ,2,1,1,1,1,1,1,1,1,1]
# 要求:
# y轴表示个数
# x轴表示岁数,比如11岁,12岁等

from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="c:/windows/fonts/simhei.ttf")

plt.figure(figsize=(20, 8), dpi=80)

y1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y2 = [1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]

x = range(11, 31)

plt.plot(x, y1, label="自己", linestyle="-", color="orange", alpha=0.5)
plt.plot(x, y2, label="同桌", linestyle="--", color="red", alpha=0.5)

plt.legend(prop=my_font, loc="best")

plt.xticks(x, ["{}岁".format(i) for i in x], fontproperties=my_font)

plt.show()

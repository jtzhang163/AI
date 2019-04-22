# 绘制条形图
# 假设你知道了列表a中电影分别在2017-09-14(b_14), 2017-09-15(b_15), 2017-09-16(b_16)三天的票房,为了展示列表中电影本身的票房以及同其他电影的数据对比情况,应该如何更加直观的呈现该数据?
#
# a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
# b_16 = [15746,312,4497,319]
# b_15 = [12357,156,2045,168]
# b_14 = [2358,399,2358,362]

from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="c:/windows/fonts/simhei.ttf")

plt.figure(figsize=(10, 8), dpi=80)

a = ["猩球崛起3：终极之战", "敦刻尔克", "蜘蛛侠：英雄归来", "战狼2"]

b_14 = [2358,399,2358,362]
b_15 = [12357,156,2045,168]
b_16 = [15746,312,4497,319]

_x = range(len(a))

plt.bar(_x, b_14, width=0.2, color="orange")
plt.bar([i+0.2 for i in _x], b_15, width=0.2, color="blue")
plt.bar([i+0.4 for i in _x], b_16, width=0.2, color="green")

plt.xticks([i + 0.3 for i in _x], a, fontproperties=my_font)

plt.ylabel("票房(万)", fontproperties=my_font)

plt.savefig("./output_file/page043_movie.png")
plt.show()

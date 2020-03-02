import matplotlib.pyplot as plt
from random_walk import Random_walk


#while True:

rw = Random_walk()
rw.fill_walk()
#设置绘图窗口的尺寸
plt.figure(dpi=128, figsize=(9, 5.4))
point_numbers = list(range(rw.num_points))
#突出起点
plt.scatter(0, 0, c='green', edgecolors='none', s=100)
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
#突出终点
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', cmap=plt.cm.Blues, edgecolors='none', s=100)
#隐藏坐标轴
# plt.axes().get_xaxis().set_visible(False)
# plt.axes().get_yaxis().set_visible(False)
plt.show()
    # keep_running = input("继续漫步？ (Y/N):")
    # if keep_running == 'n':
    #     break
import matplotlib.pyplot as plt
from random_dot_pic.random_walk import RandomWalk

while True:
    #创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw=RandomWalk(50000)
    rw.fill_walk()

    #设置绘图窗口的尺寸 单位为英寸
    plt.figure(figsize=(10,6))

    point_number=list(range(rw.num_point))
    plt.scatter(rw.x_values,rw.y_values,edgecolors='none',s=1,c=point_number,cmap=plt.cm.Blues)

    #突出
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',s=100)

    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running=input('make another walk? (y/n): ')
    if keep_running == 'n':
        break

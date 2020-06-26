import matplotlib.pyplot as plt
'''绘制散点图 并设置样式'''

x_values=list(range(1,1001,10))
y_values=[x**2 for x in x_values]    #自动计算

# s=50 表示点的大小   edgecolors='none' 表示将数据点的轮廓删除，因为在数据点很多时看起来像一条线，而不是散点图
# c=(0,0,0.8)  或 c='red' 设置点的颜色
#或者设置颜色渐变 以根据y值变化为例： 参数 c=y_values,cmap=plt.cm.Blues  cmap指出使用哪个颜色映射
plt.scatter(x_values,y_values,s=10,edgecolors='none',c=y_values,cmap=plt.cm.Reds)


#设置图表标题并给坐标轴加上标签
plt.title('Square Numbers',fontsize=24)
plt.xlabel('value',fontsize=16)
plt.ylabel('Square of Values',fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize=14)

#设置坐标轴显示范围
plt.axis([0,1100,0,1100000])


#将图表保存到文件
plt.savefig('squares_plot.png',bbox_inches='tight')   #tight表示将图表多余的空白区域剪裁掉

plt.show()





import csv
import matplotlib.pyplot as plt
from datetime import datetime

#从文件获取日期和最高、低气温
filename= 'death_valley_2014.csv'
with open(filename) as f:
    reader=csv.reader(f)    # reader是文件阅读器
    header_row=next(reader)    #访问文件下一行  这里是第一行
# for index,column_header in enumerate(header_row):   #enumerate()用来获取每个元素的索引及值
#     print(index,column_header)
    dates,highs,lows=[],[],[]
    for row in reader:
        try:
            current_date=datetime.strptime(row[0],'%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

#根据数据绘制图形
fig=plt.figure(figsize=(10,6))
plt.plot(dates,highs,c='red')
plt.plot(dates,lows,c='blue')
#填充两折线之间的区域  alpha表示颜色透明度 0为完全透明
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

#设置图形格式
plt.title('daily high and low tepmratures - 2014\nDeath valley,CA',fontsize=24)
plt.xlabel('time',fontsize=16)
plt.ylabel('temprature (F)',fontsize=16)
fig.autofmt_xdate()    #自动格式x  这里是使日期标签斜放避免重叠
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()
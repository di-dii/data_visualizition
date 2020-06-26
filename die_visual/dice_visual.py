from die_visual.die import Die
import pygal

#创建两个骰子
die1=Die()
die2=Die()

#多次投掷骰子，将结果记录在列表中
results=[]
for roll_num in range(1000):
    result=die1.roll()+die2.roll()
    results.append(result)

#分析结果
frequencys =[]
max_result=die1.num_sides+die2.num_sides
for value in range(2,max_result+1):
    frequency=results.count(value)
    frequencys.append(frequency)

#对结果可视化
hist=pygal.Bar()

hist.title='Result of rolling two D6 1000 times'
hist.x_labels=[str(x) for x in range(2,13)]
hist._x_title='Result'
hist.title='Frequency of Result'

hist.add('D6+D6',frequencys)
hist.render_to_file('dice_visual.svg')  #必须为svg  此文件在浏览器中打开
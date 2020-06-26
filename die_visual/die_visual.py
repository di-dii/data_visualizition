from die_visual.die import Die
import pygal

die=Die()

#多次投掷骰子，将结果记录在列表中
results=[]
for roll_num in range(1000):
    result=die.roll()
    results.append(result)

#分析结果
frequencys =[]
for value in range(1,die.num_sides+1):
    frequency=results.count(value)
    frequencys.append(frequency)

#对结果可视化
hist=pygal.Bar()

hist.title='Result of rolling one D6 1000 times'
hist.x_labels=['1','2','3','4','5','6']
hist._x_title='Result'
hist.title='Frequency of Result'

hist.add('D6',frequencys)
hist.render_to_file('die_visual.svg')  #必须为svg  此文件在浏览器中打开
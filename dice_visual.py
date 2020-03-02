from die import Die
import pygal

#创建六面骰子
die_1 = Die()
die_2 = Die()

results = []

#扔几次骰子，并存储在列表中
for rull_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
hist = pygal.Bar()
#xlabels = []
#hist.x_labels = []
hist.title = "Result of rolling one D6 1000 times."
#for i in range(2, max_result + 1):
#    hist.x_labels.append(i)
# hist.x_labels = xlabels
hist.x_labels = [i for i in range(2, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency"

hist.add('D6+D6', frequencies)
hist.render_to_file('dice_visual.svg')
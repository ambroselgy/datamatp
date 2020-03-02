from die import Die
import pygal

#创建六面骰子
die = Die()

results = []

#扔几次骰子，并存储在列表中
for rull_num in range(1000):
    result = die.roll()
    results.append(result)

#分析结果
frequencies = []

for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
hist = pygal.Bar()

hist.title = "Result of rolling one D6 1000 times."
hist.x_labels = [i for i in range(1, results + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
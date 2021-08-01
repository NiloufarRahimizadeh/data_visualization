from die import Die 
from plotly import offline
from plotly.graph_objs import Bar, Layout 

die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_results = die_1.num_sides + die_2.num_sides
for value in range(2, max_results):
    frequency = results.count(value)
    frequencies.append(frequency)


x_values = list(range(2, max_results+1))
data = [ Bar(x=x_values, y= frequencies)]


x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling a D6 and D10 dice 50000 times',
xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')
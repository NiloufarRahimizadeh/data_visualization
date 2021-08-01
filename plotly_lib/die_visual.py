from die import Die
from plotly import offline
from plotly.graph_objs import Layout, Bar
die = Die()
results = []

for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]
my_layout = Layout(title="results of one rolling D6 1000 time",
xaxis={'title': 'Result'}, yaxis={'title': 'frequency of result'})
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
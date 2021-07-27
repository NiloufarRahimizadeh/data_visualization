import matplotlib.pyplot as plt 


x_values = [1, 2, 3, 4]
y_values = [x**2 for x in x_values]

plt.plot(x_values, y_values,  c="red")
plt.show()
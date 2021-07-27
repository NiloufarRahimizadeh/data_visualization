import matplotlib.pyplot as plt 


x_values = [1, 2, 3, 4]
y_values = [x**2 for x in x_values]
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)
plt.show()
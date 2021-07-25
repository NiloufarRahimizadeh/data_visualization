import matplotlib.pyplot as plt


x_values = range(1,1001)
y_values = [x**2 for x in x_values]
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s =10)
ax.axis([0, 1100, 0, 1100000])
plt.show()
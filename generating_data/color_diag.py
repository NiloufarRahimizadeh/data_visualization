from matplotlib import colors
import matplotlib.pyplot as plt 

x_values = [1, 2, 3, 4]
y_values = [1, 4, 9, 16]

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, color=(0, 0.8, 0), s=10)
ax.set_xlabel("Value")
ax.set_ylabel("Square of Value")
plt.show()
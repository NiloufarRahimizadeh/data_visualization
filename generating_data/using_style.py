import matplotlib.pyplot as plt
from numpy import square


# print(plt.style.available)
# To use any of these styles, add one line of code before starting 
# to generate the plot:
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares)
plt.style.use("dark_background")
plt.show()

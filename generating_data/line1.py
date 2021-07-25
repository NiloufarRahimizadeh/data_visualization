# you’ll need to install it using pip, a module that downloads and installs Python packages.
# python3 -m pip install --user matplotlib
import matplotlib.pyplot as plt 


squares = [1, 4, 9, 16, 25]
input_values = [1, 2, 3, 4, 5] 
fig, ax = plt.subplots() # This function can generate one or more plots in the same figure.
ax.plot(input_values, squares, linewidth=3) #The variable ax represents a single plot in the figure and is the variable 
# we’ll use most of the time.
# We then use the plot() method, which will try to plot the data it’s given in a meaningful way.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis="both", labelsize=40)
plt.show()
# The function plt.show() opens Matplotlib’s viewer and displays the plot,

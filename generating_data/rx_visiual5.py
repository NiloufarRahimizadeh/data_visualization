# Cleaning Up the Axes
import matplotlib.pyplot as plt 
from rand_walk import RandomWalk


while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
    s=100)
    ax.scatter(rw.x_values, rw.y_values, s=15, 
    c=point_numbers, cmap=plt.cm.Blues, edgecolors='none')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("make another walk? (y/n)")
    if keep_running == 'n':
        break
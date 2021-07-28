import matplotlib.pyplot as plt 
from rand_walk import RandomWalk


rw = RandomWalk()
rw.fill_walk()
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()

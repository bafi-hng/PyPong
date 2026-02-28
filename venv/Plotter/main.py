import numpy as np
import matplotlib.pyplot as plt 
from math import *

""""
function = str(input("Funktion eingeben: "))
function = function.replace('x','(x)')
limit_min = float(input("x-Untergrenze eingeben: "))
limit_max = float(input("x-Obergrenze eingeben: "))

x = np.linspace(limit_min, limit_max, 100)
y = []

for n_x in x:
    n_y = eval(function.replace('x', str(n_x)))
    y.append(n_y)


fig, ax = plt.subplots(figsize=(10,7))

ax.set_ylabel('y-Achse', fontsize = 20)
ax.set_xlabel('x-Achse', fontsize = 20)

plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)

ax.plot(x, y, lw = 5, color = 'tab:blue')

ax.grid()
plt.tight_layout()
plt.show()
"""

print(log(0))
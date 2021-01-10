# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

# our X values:
dias = np.linspace(1,30,30)
# our Y values:
celsius_values_min = np.random.rand(30)*15+15
celsius_values_max = np.random.rand(30)*10
celsius_values_max += celsius_values_min
print celsius_values_min
print celsius_values_max
print dias

xmin, xmax, ymin, ymax = 1, 30, celsius_values_min.min()*0.95, celsius_values_max.max()*1.051
plt.axis([xmin, xmax, ymin, ymax])

plt.plot(dias, celsius_values_min,"b-",dias,celsius_values_max,'m-')
plt.show()

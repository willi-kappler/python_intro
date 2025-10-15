# Gauss:
import matplotlib.pyplot as plt
import numpy as np

x0 = 1.2
sigmax = 0.8
a = 2.0

x = np.arange(-10.0, 10.0, 0.001)
y = a * np.exp(-(x - x0)**2 / sigmax )

fig, ax = plt.subplots()

ax.plot(x, y)

ax.grid()
plt.show()

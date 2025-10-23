# Sinus:
import matplotlib.pyplot as plt
import numpy as np

omega = 1.2
phi = 1.0

x = np.arange(0.0, 10.0, 0.1)
y = np.sin((omega * x) + phi)

y2 = y ** 2

fig, ax = plt.subplots()

ax.plot(x, y2)

ax.grid()
plt.show()

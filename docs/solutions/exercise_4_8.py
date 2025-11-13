import numpy as np
import matplotlib.pyplot as plt

a = np.loadtxt("monthly_in_situ_co2_mlo_ready4loading.txt")
x = a[:,0]
y = a[:,1]
x2 = x[y>0]
y2 = y[y>0]
length = len(y)

p1 = np.polyfit(x2, y2, 1)
p2 = np.polyfit(x2, y2, 2)

pv1 = np.polyval(p1, x2)
pv2 = np.polyval(p2, x2)

diff1 = y2 - pv1
diff2 = y2 - pv2

fig, ax = plt.subplots()
ax.plot(x2, y2, label="original")
ax.plot(x2, pv1, label="pv1")
ax.plot(x2, pv2, label="pv2")
ax.set(xlabel="time (yrs)", ylabel="co2 (ppm)", title="co2 data")
ax.legend()
ax.grid()

fig, ax = plt.subplots()
ax.plot(x2, diff1, label="diff1")
ax.plot(x2, diff2, label="diff2")
ax.set(xlabel="time (yrs)", ylabel="co2 (ppm)", title="co2 data")
ax.legend()
ax.grid()

plt.show()

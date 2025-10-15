import numpy as np
import matplotlib.pyplot as plt

a = np.loadtxt("monthly_in_situ_co2_mlo_ready4loading.txt")
x = a[:,0]
y = a[:,1]
x = x[y>0]
y = y[y>0]
length = len(y)

p1 = np.polyfit(x, y, 1)
p2 = np.polyfit(x, y, 2)

pv1 = np.polyval(p1, x)
pv2 = np.polyval(p2, x)

diff1 = y - pv1
diff2 = y - pv2

fig, ax = plt.subplots()

ax.plot(x, y, label="original")
ax.plot(x, pv1, label="pv1")
ax.plot(x, pv2, label="pv2")
ax.plot(x, diff1, label="diff1")
ax.plot(x, diff2, label="diff2")
ax.set(xlabel="time (yrs)", ylabel="co2 (ppm)", title="co2 data")
ax.legend()
ax.grid()
plt.show()

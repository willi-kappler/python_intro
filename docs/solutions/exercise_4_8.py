import numpy as np
import matplotlib.pyplot as plt

a = np.loadtxt("monthly_in_situ_co2_mlo_ready4loading.txt")
x = a[:,0]
y = a[:,1]
x = x[y>0]
y = y[y>0]
length = len(y)

p = np.polyfit(x, y, 1)
p2 = np.polyfit(x, y, 2)

pv = np.polyval(p, x)
pv2 = np.polyval(p2, x)

diff = y - pv
diff2 = y - pv2

fig, ax = plt.subplots()

ax.plot(x, y)
ax.plot(x, diff)
ax.plot(x, diff2)
ax.plot(x, pv)
ax.plot(x, pv2)

ax.set(xlabel="time (yrs)" , ylabel="co2 (ppm)",
    title="co2 data")

ax.grid()
plt.show()

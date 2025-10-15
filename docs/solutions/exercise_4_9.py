import matplotlib.pyplot as plt
import numpy as np

def derivative(a):
    s = a.shape
    if s[1] != 2:
        print("The shape of the array must be (n, 2)!")
        return []

    x = a[:, 0]
    y = a[:, 1]
    length = len(x)
    d = np.zeros((length, 2))

    for i in range(0, length - 1):
        dx = x[i+1] - x[i]
        dy = y[i+1] - y[i]
        d[i, 1] = dy / dx
        d[i, 0] = x[i]

    d[length-1] = d[length-2]

    fig, ax = plt.subplots(2, 1, sharex=True)
    ax[0].plot(x, y)
    ax[0].set(title="original data")
    ax[0].grid()
    ax[1].plot(d[:, 0], d[:, 1])
    ax[1].set(title="derived data")
    ax[1].grid()

    plt.show()

    return d

a = np.loadtxt("monthly_in_situ_co2_mlo_ready4loading.txt")
x = a[:,0]
y = a[:,1]
x = x[y>0]
y = y[y>0]
length = len(y)
data = np.vstack((x,y)).T

d = derivative(data)

y_rand = y + np.random.randn(length)

fig, ax = plt.subplots()
#ax.plot(x, y)
#ax.plot(x, y_rand)
ax.plot(x, y - y_rand)
ax.set(xlabel="time (yrs)" , ylabel="co2 (ppm)", title="co2 data")
ax.grid()
plt.show()

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("XYShirase_GPS_Small.txt", sep="\s+", names = ["sx", "sy", "long", "lat", "elevation", "time"])

elevation = data["elevation"]
length = len(elevation)
elev_wind = np.zeros(length)

for i in range(0, length-1):
    elev_wind[i] = (elevation[i+1] + elevation[i]) / 2.0

elev_wind[-1] = elev_wind[-2]

def sliding_window(n, d):
    if n < 2:
        print("Invalid window size, must be at least 2: ", n)
        return []

    length = len(d)
    wind = np.zeros(length)

    for i in range(0, length - (n - 1)):
        s = 0.0
        for j in range(0, n):
            s += d[i+j]
        wind[i] = s / n

    for j in range(-n, 0):
        wind[j] = wind[j - 1]
    
    return wind

elev_wind2 = sliding_window(5, elevation)

elev_wind3 = elevation.rolling(5).sum()

figsize = 12
fig, ax = plt.subplots()
fig.set_figwidth(figsize)
ax.plot(data["time"], data["elevation"])
ax.set(xlabel="time (day)" , ylabel="elevation (m)", title="original data")
ax.grid()

fig, ax = plt.subplots()
fig.set_figwidth(figsize)
ax.plot(data["time"], elev_wind)
ax.set(xlabel="time (day)" , ylabel="elevation (m)", title="window size 2")
ax.grid()

fig, ax = plt.subplots()
fig.set_figwidth(figsize)
ax.plot(data["time"], elev_wind2)
ax.set(xlabel="time (day)" , ylabel="elevation (m)", title="window size 5")
ax.grid()

fig, ax = plt.subplots()
fig.set_figwidth(figsize)
ax.plot(data["time"], elev_wind3)
ax.set(xlabel="time (day)" , ylabel="elevation (m)", title="window size 5 (pandas)")
ax.grid()

plt.show()

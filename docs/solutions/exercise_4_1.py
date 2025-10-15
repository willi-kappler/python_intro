import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("monthly_in_situ_co2_mlo_ready4loading.txt")
print(f"The dimensions of the time series are {data.shape}")
print(f"We have {len(data[:, 0])} data values.")
print(f"The mean value of Co2 is at the moment {np.mean(data[:, 1])} ppm which seems low.")
print(f"The standard deviation Co2 is at the moment {np.std(data[:, 1])} ppm which seems high.")
print(f"The minimum value is: {np.min(data[:, 1])}")
print(f"The maximum value is: {np.max(data[:, 1])}")

fig, ax = plt.subplots()
ax.plot(data[:, 0], data[:, 1])
ax.set(xlabel="Time in years", ylabel="Co2 in ppm", title="Keeling Curve")

fig, ax = plt.subplots()
ax.plot(data[0:10, 0], data[0:10, 1],"r-x")
ax.set(xlabel="Time in years", ylabel="Co2 in ppm", title="Keeling Curve first ten samples")

fig, ax = plt.subplots()
ax.plot(data[-11:-1, 0], data[-11:-1, 1],"r-x")
ax.set(xlabel="Time in years", ylabel="Co2 in ppm", title="Keeling Curve last ten samples")
plt.show()

fig, ax = plt.subplots()
ax.plot(data[20:30, 0], data[20:30, 1],"r-x")
ax.set(xlabel="Time in years", ylabel="Co2 in ppm", title="Keeling Curve samples from 20 to 30")

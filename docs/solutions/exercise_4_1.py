import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("monthly_in_situ_co2_mlo_ready4loading.txt")

time = data[:, 0]
co2 = data[:, 1]

print(f"The dimensions of the time series are {data.shape}")
print(f"We have {len(time)} data values.")
print(f"The mean value of Co2 is at the moment {np.mean(co2)} ppm which seems low.")
print(f"The standard deviation Co2 is at the moment {np.std(co2)} ppm which seems high.")
print(f"The minimum value is: {np.min(co2)}")
print(f"The maximum value is: {np.max(co2)}")

fig, ax = plt.subplots()
ax.plot(time, co2)
ax.set(xlabel="Time in years", ylabel="Co2 in ppm", title="Keeling Curve")

fig, ax = plt.subplots()
ax.plot(time[0:10], co2[0:10],"r-x")
ax.set(xlabel="Time in years", ylabel="Co2 in ppm", title="Keeling Curve first ten samples")

fig, ax = plt.subplots()
ax.plot(time[-11:-1], co2[-11:-1],"r-x")
ax.set(xlabel="Time in years", ylabel="Co2 in ppm", title="Keeling Curve last ten samples")

fig, ax = plt.subplots()
ax.plot(time[20:30], co2[20:30],"r-x")
ax.set(xlabel="Time in years", ylabel="Co2 in ppm", title="Keeling Curve samples from 20 to 30")

fig, ax = plt.subplots()
ax.plot(time[0:10], co2[0:10],"r-x")
ax.plot(time[-11:-1], co2[-11:-1],"g-x")
ax.plot(time[20:30], co2[20:30],"b-x")
plt.show()

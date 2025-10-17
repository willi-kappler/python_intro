import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("monthly_in_situ_co2_mlo_ready4loading.txt")
length1 = len(data[:, 0])
good_values = []

for i in range(length1):
    time = data[i, 0]
    co2_value = data[i, 1]
    # Print all values:
    print(co2_value)

    # No data available:
    if co2_value < 0:
        print(f"No data in row: {i}, time: {time}")
    else:
        good_values.append((time, co2_value))

# No data values removed:
cleaned_data = np.array(good_values)
length2 = len(good_values)

# Visualize:
fig, ax = plt.subplots()
ax.plot(cleaned_data[:, 0], cleaned_data[:, 1])
ax.set(xlabel="Time in years", ylabel="Co2 in ppm", title="Keeling Curve")

# Derivative:
dy_dx = []

for i in range(length2 - 1):
    dx = cleaned_data[i + 1, 0] - cleaned_data[i, 0]
    dy = cleaned_data[i + 1, 1] - cleaned_data[i, 1]
    dy_dx.append((cleaned_data[i, 0], dy / dx))

derived = np.array(dy_dx)

# Visualize:
fig, ax = plt.subplots()
ax.plot(derived[:, 0], derived[:, 1])
ax.set(xlabel="Time in years", ylabel="Co2 rate per year", title="Keeling Curve")

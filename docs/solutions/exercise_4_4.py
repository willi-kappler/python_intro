import pandas as pd

data = pd.read_csv("temperature_amplitude.txt", sep=" ", names=["temp", "radar"])

temp = data["temp"]
radar = data["radar"]

for i in range(len(temp)):
    if temp[i] < 0.0:
        radar[i] = radar[i] * 10

i = 0
while i < len(temp):
    if temp[i] < 0.0:
        radar[i] = radar[i] * 10
        i = i + 1

data.to_csv("temperature_amplitude_corrected.txt", header=["temperature", "radar amplitudes"], index=False)

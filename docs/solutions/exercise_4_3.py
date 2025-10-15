import pandas as pd

data = pd.read_csv("monthly_in_situ_co2_mlo_ready4loading.txt", sep=" ", names = ["Year", "CO2 value"])
data = data[data["CO2 value"] >= 0.0]
data.to_csv("output.csv", index=False)

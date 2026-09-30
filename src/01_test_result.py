## Result 1: Wilcoxon signed-rank; n = 30, p = 0.0014

import pandas as pd
from scipy import stats

df = pd.read_csv("data/flight-spo2-clean.csv")
long_haul = df[df["long_haul"] == 1]

stat, p = stats.wilcoxon(long_haul["spo2_flight_day"], long_haul["spo2_day1"])

print("**********************************************")
print("LONG-HAUL: flight day vs day 1 baseline SpO2")
print("**********************************************")
print(f"Pairs: {len(long_haul)}")
print(f"W = {stat:.1f}")
print(f"p = {p:.6g}")
print(f"Median: {long_haul['spo2_flight_day'].median():.2f}%  ->  {long_haul['spo2_day1'].median():.2f}%")
print(f"Mean: {long_haul['spo2_flight_day'].mean():.2f}%  ->  {long_haul['spo2_day1'].mean():.2f}%")

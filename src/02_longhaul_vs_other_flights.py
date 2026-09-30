## Result 2: Mann-Whitney U; n = 30 vs 173, p = 0.0019

import numpy as np
import pandas as pd
from scipy import stats

df = pd.read_csv("data/flight-spo2-clean.csv")
long_haul = df.loc[df["long_haul"] == 1, "delta_day1"]
other = df.loc[df["long_haul"] == 0, "delta_day1"]

stat, p = stats.mannwhitneyu(long_haul, other, alternative="two-sided")

print("**********************************************")
print("LONG-HAUL vs OTHER FLIGHTS: next-day change")
print("**********************************************")
print(f"Long-haul flights: {len(long_haul)}")
print(f"Other flights: {len(other)}")
print(f"U = {stat:.1f}")
print(f"p = {p:.6g}")
print(f"Long-haul mean: {long_haul.mean():+.2f} pct points")
print(f"Other mean: {other.mean():+.2f} pct points")
print(f"Long-haul median: {long_haul.median():+.2f} pct points")
print(f"Other median: {other.median():+.2f} pct points")

rho, rho_p = stats.spearmanr(df["tz_abs"], df["delta_day1"])
kruskal = stats.kruskal(*[g["delta_day1"].to_numpy() for _, g in df.groupby("tz_abs")])

print()
print("**********************************************")
print("DOSE-RESPONSE: time zones crossed")
print("**********************************************")
for tz, group in df.groupby("tz_abs"):
    print(f"{tz} time zones: n = {len(group)}, mean = {group['delta_day1'].mean():+.2f}, "
          f"median = {group['delta_day1'].median():+.2f}")
print(f"Spearman rho = {rho:+.3f}")
print(f"Spearman p = {rho_p:.4g}")
print(f"Kruskal-Wallis H = {kruskal.statistic:.2f}")
print(f"Kruskal-Wallis p = {kruskal.pvalue:.4g}")

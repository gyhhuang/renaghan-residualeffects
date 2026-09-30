## Result 3: Wilcoxon signed-rank; n = 25, p = 0.0030

import pandas as pd
from scipy import stats

df = pd.read_csv("data/flight-spo2-clean.csv")
long_haul = df[df["long_haul"] == 1]
other = df[df["long_haul"] == 0]
both = set(long_haul["athlete_id"]) & set(other["athlete_id"])

mean_long = long_haul[long_haul["athlete_id"].isin(both)].groupby("athlete_id")["delta_day1"].mean()
mean_other = other[other["athlete_id"].isin(both)].groupby("athlete_id")["delta_day1"].mean()
difference = (mean_long - mean_other).dropna()

stat, p = stats.wilcoxon(difference)
ttest = stats.ttest_1samp(difference, 0)

print("**********************************************")
print("WITHIN-ATHLETE: long-haul vs own shorter flights")
print("**********************************************")
print(f"Athletes: {len(difference)}")
print(f"W = {stat:.1f}")
print(f"p = {p:.6g}")
print(f"Their long-haul flights: {mean_long.mean():+.2f} pct points")
print(f"Their other flights: {mean_other.mean():+.2f} pct points")
print(f"Within-athlete difference mean: {difference.mean():+.2f} pct points")
print(f"Within-athlete difference median: {difference.median():+.2f} pct points")
print(f"Paired t-test t({len(difference) - 1}) = {ttest.statistic:.2f}")
print(f"Paired t-test p = {ttest.pvalue:.6g}")

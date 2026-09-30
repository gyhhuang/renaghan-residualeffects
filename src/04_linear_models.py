## Result 4: Linear model, athlete-clustered OLS; beta = -1.98, p = 0.0005

import warnings
import pandas as pd
import statsmodels.formula.api as smf

warnings.simplefilter("ignore")

df = pd.read_csv("data/flight-spo2-clean.csv")

print("**********************************************")
print("OLS WITH CLUSTER-ROBUST STANDARD ERRORS")
print("**********************************************")
for label, groups in [("athlete", df["athlete_id"]), ("trip", df["trip_id"])]:
    fit = smf.ols("delta_day1 ~ long_haul", df).fit(
        cov_type="cluster", cov_kwds={"groups": groups}
    )
    low, high = fit.conf_int().loc["long_haul"]
    print(fit.summary())
    print()
    print(f"Clustered by {label}: beta = {fit.params['long_haul']:+.3f} pct points")
    print(f"Clustered by {label}: 95% CI = [{low:+.3f}, {high:+.3f}]")
    print(f"Clustered by {label}: p = {fit.pvalues['long_haul']:.4g}")
    print()

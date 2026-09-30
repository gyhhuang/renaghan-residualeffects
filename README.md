# Residual Effects of Air Travel on Oxygen Saturation in D1 Collegiate American Football Athletes

Data and code for  MIT Sloan Sports Analytics Conference abstract "Residual Effects of Air Travel on Oxygen Saturation in D1 Collegiate American Football Athletes", authors Eric J. Renaghan, Gabriel Huang, Harrison L. Wittels and Michael J. Wishon

## Data

`data/flight-spo2-clean.csv` — 203 athlete-flights, 47 athletes, 13 away games,
three seasons.

| column | meaning |
| --- | --- |
| `athlete_id` | de-identified athlete, stable across trips |
| `trip_id` | de-identified away game, numbered chronologically |
| `season` | 2024, 2025 or 2026 |
| `flight_distance_mi`, `flight_time_hr` | trip distance and duration |
| `tz_change`, `tz_abs` | time zones crossed; negative is westbound |
| `long_haul` | 1 if `tz_abs >= 3` |
| `spo2_flight_day` | baseline the morning of the flight, % |
| `spo2_day1` | baseline the morning after arrival, % |
| `delta_day1` | `spo2_day1 - spo2_flight_day` |


## Analyses

```
pip install -r requirements.txt
python analysis/01_test_result.py
```

| script | test | headline |
| --- | --- | --- |
| `01_test_result.py` | Wilcoxon signed-rank, flight day vs day 1 after long-haul | 99.44% to 97.16%, p = 0.0014 |
| `02_longhaul_vs_other_flights.py` | Mann-Whitney U on next-day change, plus dose-response | -1.98 vs -0.01 points, p = 0.0019 |
| `03_within_athlete_contrast.py` | Wilcoxon on athletes who flew both | -2.22 points, n = 25, p = 0.0030 |
| `04_linear_models.py` | OLS with cluster-robust SEs, plus dose models | -1.98 points, 95% CI [-3.09, -0.86], p = 0.0005 |

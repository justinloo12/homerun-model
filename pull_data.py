from pybaseball import statcast, cache
import pandas as pd

cache.enable()

print("Pulling 2025 regular season...")
season_2025 = statcast(start_dt="2025-03-27", end_dt="2025-10-05")
season_2025["data_source"] = "regular_season_2025"
print(f"  2025 season: {len(season_2025):,} rows")

print("Pulling 2026 regular season to date...")
season_2026 = statcast(
    start_dt="2026-03-26",
    end_dt=pd.Timestamp.today().strftime("%Y-%m-%d")
)
season_2026["data_source"] = "regular_season_2026"
print(f"  2026 season: {len(season_2026):,} rows")

all_data = pd.concat([season_2025, season_2026], ignore_index=True)

all_data.to_csv("homerun_data_all.csv", index=False)

print(f"\nDone! {len(all_data):,} total rows saved to homerun_data_all.csv")
print(f"Columns: {list(all_data.columns)}")

print("\nBreakdown:")
print(all_data["data_source"].value_counts())

from pybaseball import statcast, cache
import pandas as pd

# Enable cache to avoid re-downloading data
cache.enable()

# ── 2025 Regular Season ──────────────────────────────────────
print("Pulling 2025 regular season (this takes ~10 min)...")
season_2025 = statcast(start_dt="2025-03-27", end_dt="2025-10-05")
season_2025["data_source"] = "regular_season_2025"
print(f"  2025 season: {len(season_2025):,} rows")

# ── Spring Training 2026 ─────────────────────────────────────
print("Pulling spring training 2026...")
spring_2026 = statcast(start_dt="2026-02-21", end_dt="2026-03-22")
spring_2026["data_source"] = "spring_training_2026"
print(f"  Spring 2026: {len(spring_2026):,} rows")

# ── WBC 2026 ─────────────────────────────────────────────────
print("Pulling WBC 2026...")
wbc_2026 = statcast(start_dt="2026-03-05", end_dt="2026-03-17")
wbc_2026["data_source"] = "wbc_2026"
print(f"  WBC 2026: {len(wbc_2026):,} rows")

# ── Combine — keep ALL columns ───────────────────────────────
all_data = pd.concat([season_2025, spring_2026, wbc_2026], ignore_index=True)

# ── Save ─────────────────────────────────────────────────────
all_data.to_csv("homerun_data_all.csv", index=False)
print(f"\nDone! {len(all_data):,} total rows saved to homerun_data_all.csv")
print(f"Columns: {list(all_data.columns)}")
print("\nBreakdown:")
print(all_data["data_source"].value_counts())
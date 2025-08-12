import fastf1
import pandas as pd

# Enable local cache so data is stored in ./cache (speeds up subsequent runs)
fastf1.Cache.enable_cache('cache')

YEAR = 2025
WEEKEND = 'Montreal'
SESSION = 'Q'

# Example: load qualifying session for YEAR LOCATION SESSION
session = fastf1.get_session(YEAR, WEEKEND, SESSION)
session.load()

def get_all_fastest_laps(session):
    fastest_laps = []

    for driver_id in session.drivers:
        lap = session.laps.pick_drivers(driver_id).pick_fastest()

        # Ensure we always store as a DataFrame
        lap_df = pd.DataFrame([lap])
        fastest_laps.append(lap_df)

    fastest_laps_df = pd.concat(fastest_laps, ignore_index=True)
    return fastest_laps_df

session_fastest_laps = get_all_fastest_laps(session)

# Sort by lap time and get top 5
top5 = session_fastest_laps.sort_values("LapTime").head(5)

print(top5[["Driver", "LapTime", "Team"]])
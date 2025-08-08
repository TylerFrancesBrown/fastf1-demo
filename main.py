import fastf1

# Enable local cache so data is stored in ./cache (speeds up subsequent runs)
fastf1.Cache.enable_cache('cache')

YEAR = 2025
WEEKEND = 'Monaco'
SESSION = 'Q'

# Example: load qualifying session for YEAR LOCATION SESSION
session = fastf1.get_session(YEAR, WEEKEND, SESSION)
session.load()

fastest_lap = session.laps.pick_fastest()
driver = fastest_lap['Driver']
lap_time = fastest_lap['LapTime']

print(f"Fastest lap: {driver} - {lap_time}")

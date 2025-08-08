import fastf1

# Enable local cache so data is stored in ./cache (speeds up subsequent runs)
fastf1.Cache.enable_cache('cache')

# Example: load qualifying session for 2024 Bahrain
session = fastf1.get_session(2024, 'Bahrain', 'Q')
session.load()

fastest_lap = session.laps.pick_fastest()
driver = fastest_lap['Driver']
lap_time = fastest_lap['LapTime']

print(f"Fastest lap: {driver} - {lap_time}")

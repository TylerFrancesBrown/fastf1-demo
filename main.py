import fastf1
import pandas as pd

def get_all_fastest_laps(session):
    """Return a DataFrame with each driver's fastest lap from the session."""
    fastest_laps = []

    for driver_id in session.drivers:
        lap = session.laps.pick_drivers(driver_id).pick_fastest()
        lap_df = pd.DataFrame([lap])  # make it a 1-row DataFrame
        fastest_laps.append(lap_df)
    
    fastest_laps_df = pd.concat(fastest_laps, ignore_index=True)
    fastest_laps_df['LapTime'] = fastest_laps_df['LapTime'].apply(convert_timeDelta)
    return fastest_laps_df

def convert_timeDelta(timedelta):
    seconds = timedelta.total_seconds()

    minutes = divmod(seconds, 60)

    return f"{int(minutes[0])}:{minutes[1]:.3f}"

def print_leaderboard(df):
    # Loop through rows with enumerate starting at 1
    for pos, row in enumerate(df.itertuples(), 1):
        # Extract needed fields (driver, lap time)
        driver = row.Driver
        lap_time = row.LapTime

        # Format and print line (align as needed)
        print(f"{pos}. {driver:<5} {lap_time}")

def main(YEAR, WEEKEND, SESSION_CODE):
    # Enable local cache so data is stored in ./cache
    fastf1.Cache.enable_cache('cache')

    session = fastf1.get_session(YEAR, WEEKEND, SESSION_CODE)
    session.load()

    session_fastest_laps = get_all_fastest_laps(session)

    print_leaderboard(session_fastest_laps)

if __name__ == '__main__':
    main(2021, 'Abu Dhabi', 'Q')

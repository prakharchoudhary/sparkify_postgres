import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    '''
    Processes a file from `song_data` and adds record to `songs` and `artists` tables.

    Parameters:
        @cur - Cursor object to execute queries.
        @filepath - Path of the file to be processed.
    '''
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    for _, row in df.iterrows():
        song_data = list(row[["song_id", "title", "artist_id", "year", "duration"]].values)
        cur.execute(song_table_insert, song_data)
        
        # insert artist record
        artist_data = list(row[["artist_id", "artist_name", "artist_location", "artist_latitude", "artist_longitude"]].values)
        cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    '''
    Processes a file from `log_data` and adds record to `time` and `songplays` tables.

    Parameters:
        @cur - Cursor object to execute queries.
        @filepath - Path of the file to be processed.
    '''
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df['page'] == 'NextSong']

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], unit='ms')
    
    # insert time data records
    time_data = []
    for item in t:
        time_data.append((item, item.hour, item.day, item.week, item.month, item.year, item.day_name()))
    
    column_labels = ('start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday')
    
    time_df = pd.DataFrame(time_data, columns=column_labels)

    for _, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[["userId", "firstName", "lastName", "gender", "level"]]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        results = cur.execute(song_select, (row.song, row.artist, row.length))
        songid, artistid = results if results else None, None

        # insert songplay record
        songplay_data = (index, pd.to_datetime(row.ts, unit='ms'), int(row.userId), row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    '''
    Main method to get file names from data/ directory and call subsequent process methods on each filename.

    Parameters:
        @cur - Cursor object to execute queries.
        @conn - Connection object
        @filepath - Path of the file to be processed.
        @func - Process method to be called.
    '''
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    '''
    Main method.
    '''
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
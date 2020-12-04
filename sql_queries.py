# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS song;"
artist_table_drop = "DROP TABLE IF EXISTS artist;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE songplays (songplay_id int, start_time time, user_id int, level varchar, song_id varchar, artist_id varchar, session_id int, location varchar, user_agent text)
""")

user_table_create = ("""
CREATE TABLE users (user_id int, first_name varchar, last_name varchar, gender varchar(2), level varchar)
""")

song_table_create = ("""
CREATE TABLE songs (song_id varchar, title text, artist_id varchar, year int, duration decimal);
""")

artist_table_create = ("""
CREATE TABLE artists (artist_id varchar, name varchar, location varchar, latitude decimal(8), longitude decimal(8))
""")

time_table_create = ("""
CREATE TABLE time (start_time time, hour int, day int, week int, month int, year int, weekday int)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplay (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s);
""")

song_table_insert = ("""
INSERT INTO song (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s);
""")

artist_table_insert = ("""
INSERT INTO artist (artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s);
""")


time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s);
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
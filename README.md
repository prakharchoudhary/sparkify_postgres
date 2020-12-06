# Sparkify Postgres ETL

This is the first project of Udacity's Data Engineer Nanodegree. It has following goals: 
- Data modeling with Postgres
- Define fact and dimension tables for a star schema
- Build an ETL pipeline using Python

## Why is it required?

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app.

*The analytics team is particularly interested in understanding what songs users are listening to.*

## What's the Data like?

The data resides in JSON files in two major directories `log_data` and `song_data`.

`song_data` : These files contain metadata about a song and the artist of that song. Files are in JSON format and are nested in subdirectories under */data/song_data*.

__Sample__
```
{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}
```

`log_data` : These are the activity logs from the music streaming app collected over time from users. The log files in the dataset you'll be working with are partitioned by year and month. Files are in JSON format and are nested in subdirectories under */data/log_data*.

__Sample__
```
{"artist":"A Fine Frenzy","auth":"Logged In","firstName":"Anabelle","gender":"F","itemInSession":0,"lastName":"Simpson","length":267.91138,"level":"free","location":"Philadelphia-Camden-Wilmington, PA-NJ-DE-MD","method":"PUT","page":"NextSong","registration":1541044398796.0,"sessionId":256,"song":"Almost Lover (Album Version)","status":200,"ts":1541377992796,"userAgent":"\"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/36.0.1985.125 Safari\/537.36\"","userId":"69"}
```

## Project Structure

The files used in the Project are as below:
- **data** : folder nested at the home of the project, where all needed jsons reside.

- **sql_queries.py** : contains all your sql queries, and is imported into the files bellow.

- **create_tables.py** : drops and creates tables. You run this file to reset your tables before each time you run your ETL scripts.

- **test.ipynb** : displays the first few rows of each table to let you check your database.

- **etl.ipynb** : reads and processes a single file from song_data and log_data and loads the data into your tables.

- **etl.py** : reads and processes files from song_data and log_data and loads them into your tables.

- **README.md** : current file, provides discussion on my project.

- __.gitignore__ : gitignore files for python.

## What's the Database like?

The DB schema used here is the Star Schema. It has 1 FACT TABLE (songplays) and 4 DIMENSION TABLES (users, songs, artists and time.)

The schema of each table is as follows:

### FACT TABLE
__songplays__ - This tables stores the log data around song plays.

| Attribute | Datatype | Description|
|-----------|----------|------------|
| songplay_id | INT | ID of each user song play.|
| start_time | TIME | Timestamp of beggining of user activity.|
| user_id | INT | ID of user.|
| level | VARCHAR | User level. [free or paid].|
| song_id | VARCHAR | ID of song played.|
| artist_id | VARCHAR | ID of the artist of the song played.|
| session_id | INT | ID of the user session.|
| location | VARCHAR | location of user when playing the song.|
| user_agent | TEXT | Agent used by user to plays songs on the app.|

### DIMENSION TABLE
__users__ - Stores data of users

| Attribute | Datatype | Description|
|-----------|----------|------------|
| user_id |INT| ID of user.|
| first_name |VARCHAR| First name of user.|
| last_name |VARCHAR| Last name of user.|
| gender |VARCHAR(2)|  Gender of user - M, F or OT(to provide choice if user does not want to reveal).|
| level |VARCHAR|  User level [free or paid].|

__songs__ - Stores data of songs

| Attribute | Datatype | Description|
|-----------|----------|------------|
| song_id | VARCHAR | ID of song. |
| title | TEXT | Title of the song. |
| artist_id | VARCHAR | ID of the Arist who composed the song. |
| year | INT | Year the song was released. |
| duration | DECIMAL | Total runtime duration of song. |

__artist__ - Stores data of artists

| Attribute | Datatype | Description|
|-----------|----------|------------|
| artist_id | VARCHAR | ID of Artist
| name | VARCHAR | Name of Artist
| location | VARCHAR | Name of the city Artist comes from |
| latitude | DECIMAL | Latitude location of artist |
| longitude | DECIMAL | Longitude location of artist |

__time__ - Stores timestamps of the played songs.

| Attribute | Datatype | Description|
|-----------|----------|------------|
| start_time | TIME | Timestamp |
| hour | INT | Hour of the start_time |
| day | INT | Day of the start_time |
| week | INT | Week of year of the start_time |
| month | INT | Month of the start_time |
|year | INT | Year of the start_time |
| weekday | VARCHAR | Name of week day of the start_time |

## How to run?

- Ensure that you are running `Python3.x` and have the following packages:
    - psycopg2==2.8.6
    - pandas==1.1.3

- Run the `create_tables.py` script to create the database and required tables.

- Run the `etl.py` script to populate tables with data.

- Run `test.ipynb` to validate the tables have been populated.
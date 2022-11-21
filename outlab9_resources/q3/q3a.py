import sqlite3
import csv

connection = sqlite3.connect('ipl.db')

connection.execute("PRAGMA foreign_keys=off;")
connection.execute("DROP TABLE IF EXISTS TEAM;")
connection.execute('''CREATE TABLE TEAM
         (team_id INT PRIMARY KEY,
         team_name TEXT);''')

connection.execute("DROP TABLE IF EXISTS PLAYER;")
connection.execute('''CREATE TABLE PLAYER
         (player_id INT PRIMARY KEY,
         player_name TEXT,
         dob TIMESTAMP,
         batting_hand TEXT,
         bowling_skill TEXT,
         country_name TEXT);''')

connection.execute("DROP TABLE IF EXISTS MATCH;")
connection.execute('''CREATE TABLE MATCH
         (match_id INT PRIMARY KEY,
         season_year INT,
         team1 INT,
         team2 INT,
         battedfirst INT,
         battedsecond INT,
         venue_name TEXT,
         city_name TEXT,
         country_name TEXT,
         toss_winner TEXT,
         match_winner TEXT,
         toss_name TEXT,
         win_type TEXT,
         man_of_match INT,
         win_margin INT,
         FOREIGN KEY (team1) REFERENCES TEAM(team_id),
         FOREIGN KEY (team2) REFERENCES TEAM(team_id),
         FOREIGN KEY (battedfirst) REFERENCES TEAM(team_id),
         FOREIGN KEY (battedsecond) REFERENCES TEAM(team_id));''')

connection.execute("DROP TABLE IF EXISTS PLAYER_MATCH;")
connection.execute('''CREATE TABLE PLAYER_MATCH
         (playermatch_key INT PRIMARY KEY,
         match_id INT,
         player_id INT,
         batting_hand TEXT,
         bowling_skill TEXT,
         role_desc TEXT,
         team_id INT,
         FOREIGN KEY (match_id) REFERENCES MATCH(match_id),
         FOREIGN KEY (player_id) REFERENCES PLAYER(player_id),
         FOREIGN KEY (team_id) REFERENCES TEAM(team_id));''')

connection.execute("DROP TABLE IF EXISTS BALL_BY_BALL;")
# Begin

connection.execute('''CREATE TABLE BALL_BY_BALL
         (match_id INT,
         innings_no INT ,
         over_id INT ,
         ball_id INT ,
         striker_batting_position INT,
         runs_scored INT,
         extra_runs INT,
         out_type TEXT,
         striker INT,
         non_striker INT,
         bowler INT,
         PRIMARY KEY (match_id,innings_no,over_id,ball_id),
         FOREIGN KEY (match_id) REFERENCES MATCH(match_id),
         FOREIGN KEY (striker) REFERENCES PLAYER(player_id),
         FOREIGN KEY (non_striker) REFERENCES PLAYER(player_id),
         FOREIGN KEY (bowler) REFERENCES PLAYER(player_id));''')


# End
connection.execute("PRAGMA foreign_keys=on;")

cursor = connection.cursor()

file1 = open("team.csv")
next(file1)
rows1 = csv.reader(file1)
cursor.executemany("INSERT INTO TEAM VALUES (?, ?)", rows1)
file1.close()

file2 = open("match.csv")
next(file2)
rows2 = csv.reader(file2)
cursor.executemany("INSERT INTO MATCH VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", rows2)
file2.close()

file3 = open("player.csv")
next(file3)
rows3 = csv.reader(file3)
cursor.executemany("INSERT INTO PLAYER VALUES (?, ?, ?, ?, ?, ?)", rows3)
file3.close()

file4 = open("player_match.csv")
next(file4)
rows4 = csv.reader(file4)
cursor.executemany("INSERT INTO PLAYER_MATCH VALUES (?, ?, ?, ?, ?, ?, ?)", rows4)
file4.close()

file5 = open("ball_by_ball.csv")
next(file5)
rows5 = csv.reader(file5)
cursor.executemany("INSERT INTO BALL_BY_BALL VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", rows5)
file5.close()

connection.commit()
connection.close()
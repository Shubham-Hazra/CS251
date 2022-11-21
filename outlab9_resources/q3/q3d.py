import sqlite3

from soupsieve import match

connection = sqlite3.connect('ipl.db')
cursor = connection.cursor()

connection.execute("DROP TABLE IF EXISTS POINTS_TABLE;")
connection.execute('''CREATE TABLE POINTS_TABLE
         (team_id INT PRIMARY KEY,
         team_name TEXT,
         points INT DEFAULT 0,
         nrr REAL DEFAULT 0);''')

query = """SELECT team_id,team_name FROM team"""
cursor.execute(query)
rows = cursor.fetchall()
cursor.executemany("INSERT INTO POINTS_TABLE VALUES(?,?,0,0)",rows)
query = """SELECT team1,team2,match_winner,win_type,win_margin FROM match"""
cursor.execute(query)
for rows in cursor.fetchall():
    if(rows[3] == "Tie"):
        cursor.execute(f"UPDATE points_table SET points = points+1 WHERE team_id = {rows[0]}")
        cursor.execute(f"UPDATE points_table SET points = points+1 WHERE team_id = {rows[1]}")
    elif(rows[3] == "NA"):
        cursor.execute(f"UPDATE points_table SET points = points+1 WHERE team_id = {rows[0]}")
        cursor.execute(f"UPDATE points_table SET points = points+1 WHERE team_id = {rows[1]}")
    else:
        cursor.execute(f"UPDATE points_table SET points = points+2 WHERE team_id = {rows[2]}")
        if(rows[3] == "runs"):
            if(int(rows[2]) == rows[0]):
                cursor.execute(f"UPDATE points_table SET nrr = nrr + {rows[4]}/20.0 WHERE team_id = {rows[0]}")
                cursor.execute(f"UPDATE points_table SET nrr = nrr - {rows[4]}/20.0 WHERE team_id = {rows[1]}")
            else:
                cursor.execute(f"UPDATE points_table SET nrr = nrr + {rows[4]}/20.0 WHERE team_id = {rows[1]}")
                cursor.execute(f"UPDATE points_table SET nrr = nrr - {rows[4]}/20.0 WHERE team_id = {rows[0]}")
        else:
            if(int(rows[2]) == rows[0]):
                cursor.execute(f"UPDATE points_table SET nrr = nrr + {rows[4]}/10.0 WHERE team_id = {rows[0]}")
                cursor.execute(f"UPDATE points_table SET nrr = nrr - {rows[4]}/10.0 WHERE team_id = {rows[1]}")
            else:
                cursor.execute(f"UPDATE points_table SET nrr = nrr + {rows[4]}/10.0 WHERE team_id = {rows[1]}")
                cursor.execute(f"UPDATE points_table SET nrr = nrr - {rows[4]}/10.0 WHERE team_id = {rows[0]}")


query = """SELECT * FROM points_table ORDER BY points DESC,nrr DESC"""
cursor.execute(query)

for rows in cursor.fetchall():
    print(f"{rows[0]},{rows[1]},{rows[2]},",end="")
    print("{:.2f}".format(rows[3]))
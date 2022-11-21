import sqlite3

connection = sqlite3.connect('ipl.db')
cursor = connection.cursor()

query = """SELECT player_id,player_name,(SELECT SUM(runs_scored) FROM ball_by_ball WHERE player.player_id = ball_by_ball.striker GROUP BY striker)runs FROM player ORDER BY runs DESC,player_name ASC LIMIT 20"""

cursor.execute(query)

for row in cursor.fetchall():
    print(f"{row[0]},{row[1]},{row[2]}")
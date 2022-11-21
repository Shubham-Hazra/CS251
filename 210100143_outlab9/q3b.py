import sqlite3

connection = sqlite3.connect('ipl.db')
cursor = connection.cursor()

query = """SELECT total.venue_name,AVG(total.runs) FROM (SELECT venue_name,sum(runs_scored+extra_runs) RUNS FROM ball_by_ball,match WHERE match.match_id = ball_by_ball.match_id GROUP BY match.match_id) AS total GROUP BY total.venue_name ORDER BY AVG(total.runs) DESC,total.venue_name ASC"""

cursor.execute(query)
for row in cursor.fetchall():
    print(f"{row[0]},",end="")
    print("{:.2f}".format(row[1]))
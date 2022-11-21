import sqlite3
import csv
import sys

try:
    sqliteConnection = sqlite3.connect('zipcodesDB.db')
    sqlite_create_table_query = '''CREATE TABLE zipcodesInfo(
                                zip_code TEXT PRIMARY KEY,
                                latitude REAL,
                                longitude REAL,
                                city TEXT,
                                state TEXT,
                                county TEXT);'''
    cursor = sqliteConnection.cursor()
    cursor.execute(sqlite_create_table_query)
    sqlite_insert_query = """INSERT INTO zipcodesInfo
                          (zip_code,latitude,longitude,city,state,county) 
                          VALUES (?, ?, ?, ?, ?, ?);"""
    recordList = []
    with open('zipcodes.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            if 'zip_code' in lines:
                continue
            else:
                recordList.append(lines)
    cursor.executemany(sqlite_insert_query, recordList)
    state = sys.argv[1]
    query = """SELECT zip_code,MAX(latitude) FROM zipcodesInfo WHERE state = ?"""
    l = []
    cursor.execute(query,(state,))
    for item in cursor.fetchall():
        l.append(item[0])
    if l[0] == None:
        print("NOT FOUND")
    else:
        print(l[0])
    sqliteConnection.commit()
    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()


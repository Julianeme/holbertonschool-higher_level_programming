#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # Open database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], db=argv[3], charset="utf8")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    try:
        # Execute the SQL command
        cursor.execute("SELECT cities.id, cities.name, states.name \
                       FROM states JOIN cities ON cities.state_id = states.id\
                       ORDER BY cities.id")
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            print(row)
    except:
        print("Error: unable to fecth data")

    # disconnect from server
    cursor.close()
    db.close()

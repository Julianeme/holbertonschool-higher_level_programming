#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

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
        cursor.execute("SELECT * FROM states ORDER BY id"))
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            if row[1] == argv[4]:
                print(row)
    except:
        print("Error: unable to fecth data")

    # disconnect from server
    cursor.close()
    db.close()

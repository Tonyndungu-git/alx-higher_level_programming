#!/usr/bin/python3
''' '''

import sys
import MySQLdb

def get_cities_of_state(username, password, database, state_name):
    ''' Connect to MySQL server '''
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()

    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()

    for row in rows:
        print(f"{row[1]}, ", end="")
    print ("\n")
    db.close()

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    get_cities_of_state(username, password, database, state_name)

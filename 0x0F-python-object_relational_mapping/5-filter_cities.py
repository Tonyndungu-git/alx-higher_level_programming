#!/usr/bin/python3
''' search for citities in a certain state'''

import sys
import MySQLdb


def main():
    conn = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3],
                        charset="utf8"
                            )
    state_name = sys.argv[4]
    cursor = conn.cursor()
    cursor.execute("SELECT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id WHERE states.name LIKE %s \
    ORDER BY cities.id", (state_name,))
    rows = cursor.fetchall()
    re = ""
    for row in rows:
        re += row[0] + ", "
    print(re[0:-2:])
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()

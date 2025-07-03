#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument.
"""
import sys
import MySQLdb


def main():
    """
    Connect to the database and display states matching the provided name.
    """

    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    mysql_db = sys.argv[3]
    state_name = sys.argv[4]

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_pass,
        db=mysql_db,
        charset="utf8"
    )

    cursor = connection.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()

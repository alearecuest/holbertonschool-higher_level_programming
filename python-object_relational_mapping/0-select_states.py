#!/usr/bin/python3
"""
List all states from the MySQL database hbtn_0e_0_usa,
ordered by id, using MySQLdb.
"""

import sys
import MySQLdb


def main():
    """
    Connect to the database using CLI args and print each row
    from the 'states' table, sorted by id.
    """
    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    mysql_db = sys.argv[3]

    connection = MySQLdb.connect(
        host="127.0.0.1",
        port=3306,
        user=mysql_user,
        passwd=mysql_pass,
        db=mysql_db,
        charset="utf8"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()

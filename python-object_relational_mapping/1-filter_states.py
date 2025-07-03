#!/usr/bin/python3
"""
Lists all states with names starting with
upper N from the database hbtn_0e_0_usa.
"""
import sys
import MySQLdb


def main():
    """
    Connect to the database using CLI args and print states
    with names starting with 'N', sorted by id.
    """
    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    mysql_db = sys.argv[3]
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_pass,
        db=mysql_db,
        charset="utf8"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name" \
    "LIKE BINARY 'N%' ORDER BY id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()

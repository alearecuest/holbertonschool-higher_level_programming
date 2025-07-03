#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument.
This version is safe from MySQL injections.
"""
import sys
import MySQLdb


def main():
    """
    Connect to the database and display states matching the provided name.
    Uses parameterized query to prevent SQL injection.
    """
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    estado = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db
    )

    cur = conn.cursor()
    
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cur.execute(query, (estado,))

    rows = cur.fetchall()
    for r in rows:
        print(r)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()

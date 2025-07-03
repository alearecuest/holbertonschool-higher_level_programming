#!/usr/bin/python3
"""
Script que lista todas las ciudades de un estado específico
"""
import sys
import MySQLdb


def main():
    """
    Función principal que conecta a la base de datos y muestra las ciudades
    del estado especificado.
    """
    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    mysql_db = sys.argv[3]
    state_name = sys.argv[4]  # El estado que busco

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_pass,
        db=mysql_db
    )

    cursor = db.cursor()

    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    
    cursor.execute(query, (state_name,))

    cities = cursor.fetchall()

    city_names = [city[0] for city in cities]
    print(", ".join(city_names))

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
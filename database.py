#!/usr/bin/env python3
# coding: utf-8

import mysql.connector
from mysql.connector import errorcode
# -tc- ne pas utiliser l'étoile dans un import. La pep8 dit de l'éviter
from config import *
from constant import *


# -tc- plutôt qu'une fonction qui voys connecte et vous
# -tc- déconnecte de base immédiatement, définir une classe
# -tc- Database représentant la connection.
def database():

    cnx = mysql.connector.connect(**DB_CONFIG)
    cursor = cnx.cursor(buffered=True)

    try:
        cursor.execute("DROP DATABASE IF EXISTS {}".format(DB_CONFIG["database"]))
        print("database is deleted")
    except mysql.connector.Error as err:
        print("Failed delete database: {}".format(err))
        exit(1)

    # -tc- Quel intérêt ici de créer une fonction dans la fonction?
    def create_database(cursor):
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8mb4'".format(
                    DB_CONFIG["database"]
                )
            )
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

    try:
        cursor.execute("USE {}".format(DB_CONFIG["database"]))
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(DB_CONFIG["database"]))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            print("Database {} created successfully.".format(DB_CONFIG["database"]))
            cnx.database = DB_CONFIG["database"]
        else:
            print(err)
            exit(1)

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end="")
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

    cursor.close()
    cnx.close()

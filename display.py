#!/usr/bin/env python3
# coding: utf-8

import mysql.connector
from mysql.connector import errorcode
# -tc- ne pas utiliser l'étoile avec import
from config import *
from constant import *

# -tc- vous n'allez pas vous connecter et vous déconnecter à
# -tc- chaque fois que vous avez besoin de la connection. Créer
# -tc- une classe Database pour gérer la connection
def display():

    cnx = mysql.connector.connect(**DB_CONFIG)
    cursor = cnx.cursor(buffered=True)

    try:
        # -tc- vous n'avez pas besoin d'un use à chaque chois. Vous
        # -tc- pouvez vous connecter directement à la base
        cursor.execute("USE {}".format(DB_CONFIG["database"]))

    except mysql.connector.Error as err:
        print("Failed display: {}".format(err))
        exit(1)

    # -tc- ne définissez pas une fonction à l'intérieur d'une autre sans bonne raison. Ici, cette
    # -tc- fonction ne sert à rien, car pas appelée
    def display_save():

        try:
            cursor.execute(display_save) # -tc- attention, votre variable a le même nom que votre fonction

        except mysql.connector.Error as err:
            print("Failed display_save: {}".format(err))
            exit(1)         

    cursor.close()
    cnx.close()

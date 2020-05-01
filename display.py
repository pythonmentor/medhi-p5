#!/usr/bin/env python3
# coding: utf-8

import mysql.connector
from mysql.connector import errorcode
from config import *
from constant import *

def display():

    cnx = mysql.connector.connect(**DB_CONFIG)
    cursor = cnx.cursor(buffered=True)

    try:

        cursor.execute("USE {}".format(DB_CONFIG["database"]))

    except mysql.connector.Error as err:
        print("Failed display: {}".format(err))
        exit(1)

    def display_save():

        try:
            cursor.execute(display_save)

        except mysql.connector.Error as err:
            print("Failed display_save: {}".format(err))
            exit(1)         

    cursor.close()
    cnx.close()
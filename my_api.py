#!/usr/bin/env python3
# coding: utf-8

import sys
import mysql.connector
from mysql.connector import errorcode
from config import *
from database import *
import request

def main():

    cnx = mysql.connector.connect(**DB_CONFIG)
    cursor = cnx.cursor(buffered=True)
    list_prod = []
    main_menu = True
    cat_choice = False
    prod_display = False
    third_choice = False
    fourth_choice = False

    while main_menu :

        print(LINE)
        print(SPACE)
        print("1 Trouver un substitut")
        print("2 Accès sauvegarde")
        print("3 Remplir Database")
        print(SPACE)
        print("4 Quitter le programme")

        print(LINE)
        print(SPACE)
        r = int(input("Sélectionner un numéro: "))
        print(LINE)
        print(SPACE)

        if r == 1:
            cat_choice = True

        elif r == 2:
            print("***Sauvegarde vide.***")
            print(LINE)
            print(SPACE)

        elif r == 3:

            cnx
            cursor

            database()
            print(LINE)
            print(SPACE)
            print("Waiting, request in progress ...")
            req = request.Request()
            req.make_request()
            print(LINE)
            print(SPACE)
            print("Request complete.")
            print(LINE)
            print(SPACE)

            cursor.close()
            cnx.close()

        elif r == 4:
            print("***Au revoir!***")
            print(LINE)
            print(SPACE)
            # main_menu = False

        else:

            print(LINE)
            print(SPACE)
            print("***Pour faire une sélection. Tapez son numéro.***")
            print(LINE)

        while cat_choice:

            print('1', name_category[0])
            print('2', name_category[1])
            print('3', name_category[2])
            print('4', name_category[3])
            print('5', name_category[4])
            print(SPACE)
            print("6 Retour au menu principal")
            
            print(LINE)
            print(SPACE)

            r = int(input("Sélectionner un numéro: "))

            if r >= 1 and r <= 5:

                print(LINE)
                print(SPACE)
                print("Sélection de la catégorie: {}".format(name_category[r-1]))
                print(LINE)
                print(SPACE)
                cat_choice = False
                prod_display = True

            elif r == 6:

                main_menu = True
                cat_choice = False
                prod_display = False
                third_choice = False
                fourth_choice = False

            else:

                print(LINE)
                print(SPACE)
                print("***Pour sélectionnez une catégorie. Tapez son numéro.***")
                print(LINE)
                print(SPACE)

        while prod_display:

            cnx
            cursor

            cursor.execute("USE {}".format(DB_CONFIG['database']))
            cursor.execute(display_product.format(r))

            print("{:^4} | {:^13} | {:^10} | {}".format("id", "barcode", "nutriscore", "name"))

            for (p_id, barcode, name, nutri) in cursor:
                list_prod.append(p_id)
                print("{:^4} | {:^13} | {:^10} | {}".format(p_id, barcode, nutri.upper(), name))

            r = int(input("Sélectionner un id: "))

            if r in list_prod:

                cnx
                cursor
                
                cursor.execute("USE {}".format(DB_CONFIG['database']))
                cursor.execute(select_product.format(r))
                print(select_product.format(r))
                print("{:^4} | {:^13} | {:^10} | {}".format("id", "barcode", "nutriscore", "name"))
                print("{:^4} | {:^13} | {:^10} | {}".format(p_id, barcode, nutri.upper(), name))

            else:

                print("not")	

            cursor.close()
            cnx.close()

            prod_display = False
            third_choice = True

        while third_choice:

            r = int(input("6 Retour au menu principal: "))

            if r == 6:

                main_menu = True
                cat_choice = False
                prod_display = False
                third_choice = False


if __name__ == "__main__":
    main()

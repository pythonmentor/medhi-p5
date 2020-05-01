#!/usr/bin/env python3
# coding: utf-8

import sys
import mysql.connector
from mysql.connector import errorcode
from config import *
from constant import *
from database import *
from product import *
import request


def main():

    list_prod = []
    list_sub = []
    list_save = []
    main_menu = True
    display_sub = False
    cat_choice = False
    prod_display = False
    restart = False
    choice_sub = False
    select_sub = False
    save_substitut = False
    error_id0 = False
    error_id1 = False

    while main_menu:

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
            main_menu = False
            display_sub = True

        elif r == 3:

            list_save = False
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

        elif r == 4:
            print("***Au revoir!***")
            print(LINE)
            print(SPACE)
            main_menu = False

        else:

            print(LINE)
            print(SPACE)
            print("***Attention: Pour faire une sélection. Tapez son numéro.***")
            print(LINE)

        while cat_choice:

            print("1", name_category[0])
            print("2", name_category[1])
            print("3", name_category[2])
            print("4", name_category[3])
            print("5", name_category[4])
            print(SPACE)
            print("6 Retour au menu principal")
            print(LINE)
            print(SPACE)

            r0 = int(input("Sélectionner un numéro: "))

            if r0 >= 1 and r0 <= 5:

                print(LINE)
                print(SPACE)
                print("Sélection de la catégorie: {}".format(name_category[r0 - 1]))
                print(LINE)
                print(SPACE)
                cat_choice = False
                prod_display = True

            elif r0 == 6:

                main_menu = True
                cat_choice = False
                prod_display = False
                restart = False
                save_substitut = False

            else:

                print(LINE)
                print(SPACE)
                print("***Attention: Pour sélectionnez une catégorie. Tapez son numéro.***")
                print(LINE)
                print(SPACE)

        while display_sub:

            cursor.execute("USE {}".format(DB_CONFIG["database"]))
            cursor.execute(display_save)

            count = cursor.rowcount

            if count == 0:

                print("sauvegarde vide")

            else:

                print(
                    "{:^10} | {:^10} | {:^10} | {:^100} | {:^50}".format(
                        "Produits", "Favoris","nutriscore", "nom du favoris", "magasin"
                    )
                )

                print(4*LINE)
                print(SPACE)

                for (prod_id, fav_id, name, nutri, market) in cursor:

                    print(
                        "{:^10} | {:^10} | {:^10} | {:^100} | {:^50}".format(
                            prod_id, fav_id, nutri.upper(), name, market
                        )
                    )

                print(SPACE)
                print(4*LINE)


            main_menu = True
            cat_choice = False
            prod_display = False
            restart = False
            display_sub = False

        while prod_display:

            print(LINE)
            print(LINE)

            cursor.execute("USE {}".format(DB_CONFIG["database"]))
            cursor.execute(display_product.format(r0))

            print(
                "{:^4} | {:^13} | {:^10} | {}".format(
                    "id", "barcode", "nutriscore", "name"
                )
            )

            for (p_id, barcode, name, nutri) in cursor:

                print(
                    "{:^4} | {:^13} | {:^10} | {}".format(
                        p_id, barcode, nutri.upper(), name
                    )
                )

                list_prod.append(p_id)

            if error_id0 is True:

                print(SPACE)
                print("***Attention: Pour sélectionnez un produit. Tapez son id.***")
                print(SPACE)

            r1 = int(input("Sélectionner un id: "))

            if r1 in list_prod:

                print(LINE)
                print(SPACE)
                print("*** Produit sélectionner ***")
                print(LINE)
                print(SPACE)

                cursor.execute(select_product.format(r1))

                print(
                    "{:^4} | {:^13} | {:^10} | {}".format(
                        "id", "barcode", "nutriscore", "name"
                    )
                )
                
                for (p_id, barcode, name, nutri) in cursor:

                    print(
                        "{:^4} | {:^13} | {:^10} | {}".format(
                            p_id, barcode, nutri.upper(), name
                        )
                    )

                prod_display = False
                choice_sub = True

            else:
             
                error_id0 = True
                prod_display = True

        while choice_sub:

            print(LINE)
            print(SPACE)
            print("*** Substitut proposer ***")
            print(LINE)
            print(SPACE)

            cursor.execute(choice_substitut.format(nutri, r0))

            print(
                "{:^4} | {:^13} | {:^10} | {}".format(
                    "id", "barcode", "nutriscore", "name"
                )
            )
                
            for (p_id, barcode, name, nutri) in cursor:

                print(
                    "{:^4} | {:^13} | {:^10} | {}".format(
                        p_id, barcode, nutri.upper(), name
                    )
                )
                list_sub.append(p_id)

            if error_id1 is True:

                print(SPACE)
                print("***Attention: Pour sélectionnez un produit. Tapez son id.***")
                print(SPACE)

            r2 = int(input("Sélectionner un substitut: "))

            if r2 in list_sub:

                print(LINE)
                print(SPACE)
                print("*** Substitut sélectionner ***")
                print(LINE)
                print(SPACE)

                cursor.execute(select_product.format(r2))

                print(
                    "{:^4} | {:^13} | {:^10} | {}".format(
                        "id", "barcode", "nutriscore", "name"
                    )
                )
                
                for (p_id, barcode, name, nutri) in cursor:

                    print(
                        "{:^4} | {:^13} | {:^10} | {}".format(
                            p_id, barcode, nutri.upper(), name
                        )
                    )

                cat_choice = False
                prod_display = False
                choice_sub = False
                save_substitut = True
                restart = False

            else:

                error_id1 = True
                choice_sub = True

            if r == 2:

                main_menu = False
                cat_choice = False
                prod_display = False
                choice_sub = False
                save_substitut = False
                restart = True

        while save_substitut:

            list_sub = [r1, r2]

            print(LINE)
            print(SPACE)
            print("1", "oui")
            print("2", "non")
            print(LINE)
            print(SPACE)
            r = int(input("Voulez-vous sauvegarder ?: "))
            print(LINE)
            print(SPACE)

            if r == 1:

                try:

                    cursor.execute("USE {}".format(DB_CONFIG["database"]))
                    cursor.execute(add_favorite, list_sub)

                    list_save = True

                    print("sauvegarde effectuer")

                except:

                    print("substitut déjà enregistrer pour ce produit")

                save_substitut = False
                restart = True 

            if r == 2:

                main_menu = False
                cat_choice = False
                prod_display = False
                save_substitut = False
                restart = True


        while restart:

            print(LINE)
            print(SPACE)
            print("1", "Retour au menu principal")
            print("2", "Quitter le programme")
            print(LINE)
            print(SPACE)

            r = int(input("Retour au menu principal: "))

            if r == 1:

                main_menu = True
                cat_choice = False
                prod_display = False
                restart = False

            if r == 2:

                main_menu = False
                cat_choice = False
                prod_display = False
                restart = False

if __name__ == "__main__":

    cnx = mysql.connector.connect(**DB_CONFIG)
    cursor = cnx.cursor(buffered=True)
    cursor
    main()
    cursor.close()
    cnx.close()

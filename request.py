#!/usr/bin/env python3
# coding: utf-8

import mysql.connector
from mysql.connector import errorcode
import requests
from config import *
from database import *
from product import *

class Request():

    def __init__(self):
        cnx = mysql.connector.connect(**DB_CONFIG)
        cursor = cnx.cursor(buffered=True)
        self.categories = name_category
        self.cat = 0
        self.nb_pages = 0
        self.nb_prod = 0
        self.nb_prod_remove = 0
        self.nb_prod_to_keep = 0
        self.url = 'https://fr.openfoodfacts.org/categorie/{}/{}.json'
        self.id = cursor.lastrowid

    def make_request(self): 

        cnx = mysql.connector.connect(**DB_CONFIG)
        cursor = cnx.cursor(buffered=True)

        for category in self.categories:

            self.nb_pages = 1
            cursor.execute(add_category, (self.id, self.categories[self.cat]))
            print(self.categories[self.cat],"...waiting...")
            self.cat +=1

            for p in range(10):

                response = requests.get(self.url.format(category, self.nb_pages))
                resp = response.json()
                self.nb_pages += 1

                for i in range(20):

                    self.nb_prod += 1
    
                    dict = {
                    'barcode' : resp["products"][i].get("_id", 0),
                    'name' : resp["products"][i].get("product_name_fr", "0"),
                    'nutriscore' : resp["products"][i].get("nutrition_grades", "0"),
                    'url' : resp["products"][i].get("url", "0"),
                    'market' : resp["products"][i].get("stores", "0"),
                    'cat_id' : self.cat
                    }

                    prod = Products(
                        dict.get('barcode'), 
                        dict.get('name'), 
                        dict.get('nutriscore'), 
                        dict.get('url'), 
                        dict.get('market'),
                        dict.get('cat_id')
                        )

                    correct_barcode = int(prod.element[0]) >3000000000000 and int(prod.element[0]) <8000000000000
                    correct_name = str(prod.element[1]) != "0" and str(prod.element[1]) != ""
                    correct_nutriscore = str(prod.element[2]) != "0"

                    if correct_barcode and correct_name and correct_nutriscore:

                        prod.add_p()

                        self.nb_prod_to_keep += 1
                        self.nb_prod_remove = self.nb_prod - self.nb_prod_to_keep

        print("{} products collected.".format(self.nb_prod))
        print("{} products removed.".format(self.nb_prod_remove))
        print("{} products added.".format(self.nb_prod_to_keep))


        cursor.close()
        cnx.close()

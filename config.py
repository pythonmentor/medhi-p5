#!/usr/bin/env python3
# coding: utf-8

DB_CONFIG = {
    'host': 'localhost',
    'user': 'p5_user',
    'password': 'p5_user',
    'database': 'project5',
    'charset': 'utf8',
    'autocommit': True,
    }

LINE = "________________________________________________________"
SPACE = "                                                        "


#################################################################################################


name_category = [
             'Jus et nectars', 
             'Produits fermentés',
             'Desserts',  
             'Matières grasses',
             'Snacks',
             ]

add_category = ("INSERT INTO Categories "
                "(c_id, name) "
                "VALUES (%s, %s)")

add_favorite = ("INSERT INTO Favorites "
                "(code) "
                "VALUES (%s)")

add_product = ("INSERT INTO Products "
               "(barcode, name, score, url, market, cat_id) "
               " VALUES (%s, %s, %s, %s, %s, %s)")

display_product = ("SELECT p_id, barcode, name, score FROM Products WHERE cat_id = {}")

select_product = ("SELECT p_id, barcode, name, score FROM Products WHERE p_id = {}")

# record_substitut = 

# query = (jointure pour afficher favorites)
# cursor.execute pour mettre dans la table favorite


#################################################################################################


TABLES = {}

TABLES['Categories'] = (
    "CREATE TABLE `Categories` ("
    "   `c_id` SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
    "   `name` VARCHAR(120)"
    ") ENGINE=InnoDB")

TABLES['Products'] = (
    "CREATE TABLE `Products` ("
    "   `p_id` SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
    "   `cat_id` SMALLINT NOT NULL, "
    "   `barcode` CHAR(14) NOT NULL,"
    "   `name` VARCHAR(210) NOT NULL,"
    "   `score` CHAR(1) NULL,"
    "   `nova` CHAR(1) NULL,"
    "   `url` TEXT NULL,"
    "   `market` VARCHAR(210) NULL,"
    "  CONSTRAINT `cat_id` FOREIGN KEY (`cat_id`) "
    "     REFERENCES `Categories` (`c_id`) ON DELETE CASCADE"   
    ") ENGINE=InnoDB")

TABLES['Favorites'] = ( 
    "CREATE TABLE `Favorites` ("
    "   `id` SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
    "   `prod_id` SMALLINT NOT NULL, "
    "  CONSTRAINT `prod_id` FOREIGN KEY (`prod_id`) "
    "     REFERENCES `Products` (`p_id`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")



#################################################################################################

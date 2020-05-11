
# -tc- éliminer les étoiles et trier correctement les import
from database import *
from config import *
from constant import *
import mysql.connector
from mysql.connector import errorcode

# -tc- créer également des classe pour catégorie, magasin, favori


class Products: # -tc- une classe se nomme au singulier (comme une table d'ailleurs)

    def __init__(self, barcode, name, nutriscore, url, market, cat_id):

        self.element = [
            barcode,
            name,
            nutriscore,
            url,
            market,
            cat_id, # -tc- si vous voulez le faire orienté-objet, utiliser un objet pour la catégorie
        ]
        # -tc- pourquoi un seul attribut et pas des attributs barcode, name, etc.

    def add_p(self):

        cnx = mysql.connector.connect(**DB_CONFIG)
        cursor = cnx.cursor(buffered=True)

        cursor.execute(add_product, self.element)

        cursor.close()
        cnx.close()

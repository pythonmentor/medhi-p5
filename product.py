from database import *
from config import *
from constant import *
import mysql.connector
from mysql.connector import errorcode


class Products:

    def __init__(self, barcode, name, nutriscore, url, market, cat_id):

        self.element = [
            barcode,
            name,
            nutriscore,
            url,
            market,
            cat_id,
        ]

    def add_p(self):

        cnx = mysql.connector.connect(**DB_CONFIG)
        cursor = cnx.cursor(buffered=True)

        cursor.execute(add_product, self.element)

        cursor.close()
        cnx.close()

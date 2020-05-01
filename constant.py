LINE = "___________________________________________________"
SPACE = "                                                  "


#################################################################################################


name_category = [
    "Jus et nectars",
    "Produits fermentés",
    "Desserts",
    "Matières grasses",
    "Snacks",
]

add_category = ("INSERT INTO Categories "
                "(c_id, name)"
                "VALUES (%s, %s)"
)

add_favorite = ("INSERT INTO Favorites "
                "(prod_id, fav_id)"
                "VALUES (%s, %s)"
)

add_product = (
    "INSERT INTO Products "
    "(barcode, name, score, url, market, cat_id)"
    " VALUES (%s, %s, %s, %s, %s, %s)"
)

display_product = "SELECT p_id, barcode, name, score FROM Products WHERE cat_id = {}"

select_product = "SELECT p_id, barcode, name, score FROM Products WHERE p_id = {}"

choice_substitut = "SELECT p_id, barcode, name, score FROM Products WHERE score <= '{}' AND cat_id = {} ORDER BY score ASC LIMIT 20"

display_save = "SELECT fav_id, prod_id, name, score, market FROM Products FULL JOIN Favorites ON p_id = Favorites.fav_id"


#################################################################################################


TABLES = {}

TABLES["Categories"] = (
    "CREATE TABLE `Categories` ("
    "   `c_id` SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
    "   `name` VARCHAR(120)"
    ") ENGINE=InnoDB"
)

TABLES["Products"] = (
    "CREATE TABLE `Products` ("
    "   `p_id` SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
    "   `cat_id` SMALLINT NOT NULL, "
    "   `barcode` CHAR(14) NOT NULL,"
    "   `name` VARCHAR(210) NOT NULL,"
    "   `score` CHAR(1) NULL,"
    "   `url` TEXT NULL,"
    "   `market` VARCHAR(210) NULL,"
    "  CONSTRAINT `cat_id` FOREIGN KEY (`cat_id`) "
    "     REFERENCES `Categories` (`c_id`) ON DELETE CASCADE"
    ") ENGINE=InnoDB"
)

TABLES["Favorites"] = (
    "CREATE TABLE `Favorites` ("
    "   `prod_id` SMALLINT , "
    "   `fav_id` SMALLINT , "
    "  CONSTRAINT `prod_id` FOREIGN KEY (`prod_id`) "
    "     REFERENCES `Products` (`p_id`) ON DELETE CASCADE,"
    "  CONSTRAINT `fav_id` FOREIGN KEY (`fav_id`) "
    "     REFERENCES `Products` (`p_id`) ON DELETE CASCADE,"
    "  UNIQUE KEY (`fav_id`, `prod_id`)"
    ") ENGINE=InnoDB"
)

#################################################################################################

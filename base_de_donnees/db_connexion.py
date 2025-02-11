import mysql.connector
from mysql.connector import errorcode
import DatabaseUtils.base_de_donnees  # Importez votre classe


try:
    conn = mysql.connector.connect(
        host="94.239.97.139",
        user="injectionsql",
        password="injectionsql",
        database="articles"
    )
    cursor = conn.cursor()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Erreur d'authentification : vérifiez vos identifiants.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("La base de données n'existe pas.")
    else:
        print(err)
    exit(1)

# Instanciation de DatabaseUtils pour initialiser la table
db_utils = DatabaseUtils(conn, cursor)
db_utils.creat_table()  # Création de la table dès que la connexion est établie

# Vous pouvez ensuite continuer avec le reste de votre application,
# par exemple en instanciant votre ArticleManager qui utilisera la connexion.

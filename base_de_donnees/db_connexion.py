import mysql.connector
from mysql.connector import errorcode
from database import DatabaseUtils
import json
import os


class ConnexionDatabase:
    def __init__(self):
        self.config = self.load_config()

        # Vérification de la présence des clés requises
        required_keys = ['host', 'port', 'user', 'password']
        missing_keys = [key for key in required_keys if key not in self.config]
        if missing_keys:
            print(f"Erreur : Les clés suivantes sont manquantes dans le fichier de configuration : {', '.join(missing_keys)}")
            exit(1)

        try:
            self.conn = mysql.connector.connect(
                host=self.config['host'],
                port=self.config['port'],
                user=self.config['user'],
                password=self.config['password'],
            )
            self.cursor = self.conn.cursor()
            print("Connexion réussie à la base de données !")

            self._init_db()  # Appel à l'initialisation de la base de données

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Erreur d'authentification : vérifiez votre utilisateur et mot de passe.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("La base de données n'existe pas.")
            else:
                print("Erreur lors de la connexion :", err)
            exit(1)

    def _init_db(self):
        # Méthode d'initialisation de la base de données
        # Vous pouvez ajouter ici le code nécessaire pour initialiser votre base de données,
        # par exemple la création de tables ou d'autres opérations.
        pass

    @staticmethod
    def load_config(filename='config.json'):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(script_dir)
        config_path = os.path.join(parent_dir, filename)

        if not os.path.exists(config_path):
            print(f"Erreur : Le fichier {config_path} est introuvable.")
            exit(1)

        with open(config_path, 'r', encoding='utf-8') as file:
            return json.load(file)


# Initialisation de la connexion à la base de données
connexion_db = ConnexionDatabase()

# Instanciation de DatabaseUtils pour initialiser la table
if hasattr(connexion_db, 'conn') and hasattr(connexion_db, 'cursor'):
    db_utils = DatabaseUtils(connexion_db.conn, connexion_db.cursor)
    db_utils.creat_table()  # Création de la table dès que la connexion est établie

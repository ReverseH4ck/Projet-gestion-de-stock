import mysql.connector
from mysql.connector import Error
import logging
from utils.get_db_info import Log

# Configurer le module logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def connexion():
    """
    Établit une connexion à la base de données en utilisant la configuration
    fournie par la méthode Log.settings().
    Renvoie l'objet de connexion pour permettre son utilisation.
    """
    try:
        # Récupération des paramètres de connexion depuis config.json
        log_DB = Log.settings()

        # Connexion à la base de données
        connection = mysql.connector.connect(**log_DB)
        if connection.is_connected():
            logging.info("Connexion à la base de données réussie !")
            return connection

    except FileNotFoundError as e:
        logging.error(f"Le fichier de configuration est introuvable : {e}")
    except ValueError as e:
        logging.error(f"Une erreur liée aux données est survenue : {e}")
    except Error as e:
        logging.error(f"Erreur de connexion à la base de données MariaDB : {e}")
    except Exception as e:
        logging.error(f"Une erreur inattendue est survenue : {e}")

    return None
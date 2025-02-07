import mysql.connector
from mysql.connector import Error
import logging
from .get_db_info import Log

# Configurer le module logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Global connection object
_db_connection = None


def connexion():
    """
    Essaie d'établir une connexion à la base de données en utilisant
    la configuration fournie par la méthode Log.settings().
    Retourne True si la connexion est réussie, sinon False.
    """
    global _db_connection
    try:
        # Récupérer les paramètres de connexion à partir de config.json
        log_DB = Log.settings()

        # Essayer d'établir la connexion
        _db_connection = mysql.connector.connect(**log_DB)
        if _db_connection.is_connected():
            logging.info("Connexion à la base de données réussie !")
            return True

    except FileNotFoundError as e:
        logging.error(f"Le fichier config.json est introuvable : {e}")
        return False
    except ValueError as e:
        logging.error(f"Erreur de contenu dans config.json : {e}")
        return False
    except Error as e:
        logging.error(f"Erreur de connexion à la base de données : {e}")
        return False
    except Exception as e:
        logging.error(f"Erreur inattendue : {e}")
        return False

    return False


def fermer_connexion():
    """
    Ferme la connexion à la base de données si elle est ouverte.
    Retourne True si la fermeture a été effectuée avec succès ou
    si aucune connexion n'était ouverte, False sinon.
    """
    global _db_connection
    try:
        if _db_connection and _db_connection.is_connected():
            _db_connection.close()
            logging.info("Connexion à la base de données fermée avec succès.")
            return True
        else:
            logging.info("Aucune connexion à fermer.")
            return True

    except Error as e:
        logging.error(f"Erreur lors de la fermeture de la connexion : {e}")
        return False
    except Exception as e:
        logging.error(f"Erreur inattendue lors de la fermeture : {e}")
        return False

import mysql.connector
from mysql.connector import Error
from get_db_info import Log
import logging

# Configuration des logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def connexion() -> None:
    """
    Cette fonction établit une connection à la base de données en utilisant la configuration
    retournée par la méthode Log.settings(), et effectue une simple connection.
    """
    try:
        # Récupération de la configuration de base de données
        log_DB = Log.settings()

        # Validation des paramètres de connection à la base de données.
        required_keys = {"host", "port", "database", "user", "password"}
        missing_keys = required_keys - log_DB.keys()
        if missing_keys:
            raise ValueError(f"Les valeurs de connection suivantes sont manquantes: {missing_keys}")

        # Connect to the database
        connection = mysql.connector.connect(**log_DB)
        if connection.is_connected():
            logging.info("Connexion à la base de données effectuée!")

    except Error as e:
        logging.error(f"Erreur durant la connexion à la base de données: {e}")

    except Exception as e:
        logging.error(f"Une erreur inattendue est survenue {e}")

    finally:
        # Vérification de la fermeture de la base de données.
        try:
            if 'connection' in locals() and connection.is_connected():
                connection.close()
                logging.info("Connexion à la base de données fermée.")
        except NameError:
            logging.debug("L'objet de connection n'existe pas.")
        except Exception as e:
            logging.error(f"Erreur durant la fermeture de la connection: {e}")


if __name__ == "__main__":
    # Execute la fonction connexion() quand ce fichier est executé
    connexion()
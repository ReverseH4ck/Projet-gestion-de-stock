import mysql.connector
from mysql.connector import Error
from get_db_info import Log
import logging

# Configurer le module logging pour afficher les messages
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def connexion() -> None:
    """
    Etablit une connexion à la base de données en utilisant la configuration
    fournie par la méthode Log.settings().
    Si une erreur survient, elle est capturée et affichée dans les logs.
    """
    try:
        # Récupération des paramètres de connexion depuis config.json
        log_DB = Log.settings()

        # Connexion à la base de données
        connection = mysql.connector.connect(**log_DB)
        if connection.is_connected():
            logging.info("Connexion à la base de données réussie !")

    except FileNotFoundError as e:
        # Gestion de l'absence du fichier config.json
        logging.error(f"Le fichier de configuration est introuvable : {e}")
    except ValueError as e:
        # Gestion des erreurs liées aux données mal formatées ou manquantes
        logging.error(f"Une erreur liée aux données est survenue : {e}")
    except Error as e:
        # Erreurs spécifiques à MySQL
        logging.error(f"Erreur de connexion à la base de données MySQL : {e}")
    except Exception as e:
        # Toute autre erreur inattendue
        logging.error(f"Une erreur inattendue est survenue : {e}")
    finally:
        # Fermeture sécurisée de la connexion
        try:
            if 'connection' in locals() and connection.is_connected():
                connection.close()
                logging.info("Connexion fermée.")
        except Exception as e:
            logging.error(f"Erreur lors de la fermeture de la connexion à la base de données : {e}")


if __name__ == "__main__":
    # Exécute la fonction connexion si le script est lancé directement
    connexion()

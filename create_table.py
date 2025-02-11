
import mysql.connector
from utils import db_connection_open as db_connection


class DbManage:

    @staticmethod
    def create_table():
        """
        Crée une table 'produits' dans la base de données si elle n'existe pas déjà.
        """
        conn = None  # Initialisation de la connexion
        try:
            # Obtenir une connexion depuis db_connection
            conn = db_connection.connexion()

            # Vérifier que la connexion est bien établie
            if conn and conn.is_connected():
                print("Connexion réussie.")

                # Créer un curseur pour exécuter des requêtes SQL
                cursor = conn.cursor()

                # Créer une table si elle n'existe pas
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS produits (
                    nom_produit VARCHAR(255) NOT NULL,
                    prix INT NOT NULL,
                    modele VARCHAR(255) NOT NULL,
                    reference INT NOT NULL,
                    quantitee INT NOT NULL,
                    PRIMARY KEY (reference)
                )
                """)

                print("Table 'produits' créée avec succès.")

                # Fermer le curseur
                cursor.close()

        except mysql.connector.Error as err:
            print(f"Erreur MariaDB : {err}")
        except Exception as e:
            print(f"Erreur : {e}")
        finally:
            # Fermer la connexion à la base de données
            if conn and conn.is_connected():
                conn.close()
                print("Connexion fermée.")


if __name__ == '__main__':
    DbManage.create_table()

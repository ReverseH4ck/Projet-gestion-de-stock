import mysql.connector  # Module pour interagir avec une base de données MariaDB/MySQL.
from utils import \
    db_connection_open as db_connection  # Importation de la fonction de connexion depuis un module utilitaire.


class Product_View:
    """
    Classe contenant une méthode statique pour afficher les produits dans une table de la base de données.
    """

    @staticmethod
    def view_products():
        """
        Affiche tous les produits disponibles dans la table 'produits' de la base de données.

        La méthode récupère toutes les colonnes de la table et affiche les informations formatées
        pour chaque ligne de produit. Si la table est vide, un message est affiché.
        """
        conn = None  # Initialisation de la variable de connexion.

        try:
            # Établir une connexion à la base de données.
            conn = db_connection.connexion()

            # Vérifier si la connexion est établie et active.
            if conn and conn.is_connected():
                cursor = conn.cursor()  # Création d'un curseur pour exécuter des requêtes SQL.

                # Requête SQL pour récupérer toutes les colonnes de la table 'produits'.
                query = "SELECT * FROM produits"
                cursor.execute(query)  # Exécution de la requête.

                # Récupération de toutes les lignes de résultats.
                rows = cursor.fetchall()

                # Vérification si des résultats sont retournés.
                if rows:
                    # Parcourir et afficher chaque produit.
                    for row in rows:
                        print(f"Nom : {row[0]}, Prix : {row[1]}, Modèle : {row[2]}, "
                              f"Référence : {row[3]}, Quantité : {row[4]}")
                else:
                    # Message si la table 'produits' est vide.
                    print("La table 'produits' est vide.")

                cursor.close()  # Fermeture du curseur après utilisation.

        # Gestion des erreurs spécifiques à MariaDB.
        except mysql.connector.Error as err:
            print(f"Erreur MariaDB : {err}")

        # Gestion des erreurs générales.
        except Exception as e:
            print(f"Erreur : {e}")

        # Assurer la fermeture sécurisée de la connexion à la base de données.
        finally:
            if conn and conn.is_connected():
                conn.close()


# Exemple d'utilisation du script.
if __name__ == '__main__':
    # Appel de la méthode pour afficher tous les produits de la table 'produits'.
    Product_View.view_products()

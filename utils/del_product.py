import mysql.connector  # Module pour interagir avec une base de données MariaDB/MySQL.
from utils import \
    db_connection_open as db_connection  # Importation de la fonction de connexion depuis un module utilitaire.


class Del_product:
    """
    Classe contenant des méthodes pour gérer les opérations de suppression ou
    mise à jour de la quantité de produits dans une base de données.
    """

    @staticmethod
    def delete_product_quantity(reference: str, quantity: int):
        """
        Supprime ou met à jour la quantité d'un produit dans la table 'produits' de la base de données.

        Args:
            reference (str): La référence unique du produit à traiter.
            quantity (int): La quantité à retirer du stock.
        """
        conn = None  # Initialisation de la variable de connexion.

        try:
            # Établir une connexion à la base de données.
            conn = db_connection.connexion()

            # Vérifier si la connexion est établie et active.
            if conn and conn.is_connected():
                cursor = conn.cursor()  # Création d'un curseur pour exécuter des requêtes SQL.

                # Requête pour récupérer la quantité actuelle du produit avec la référence donnée.
                query_select = "SELECT quantitee FROM produits WHERE reference = %s"
                cursor.execute(query_select, (reference,))
                result = cursor.fetchone()  # Récupération du premier résultat.

                # Si aucun produit n'est trouvé avec la référence, on quitte la méthode.
                if not result:
                    return

                current_quantity = result[0]  # Extraction de la quantité actuelle du produit.

                # Vérifier si la quantité à retirer est supérieure ou égale à la quantité en stock.
                if quantity >= current_quantity:
                    # Si oui, supprimer complètement le produit de la table.
                    query_delete = "DELETE FROM produits WHERE reference = %s"
                    cursor.execute(query_delete, (reference,))
                else:
                    # Sinon, mettre à jour la quantité restante après la soustraction.
                    new_quantity = current_quantity - quantity
                    query_update = "UPDATE produits SET quantitee = %s WHERE reference = %s"
                    cursor.execute(query_update, (new_quantity, reference))

                conn.commit()  # Confirmer les modifications dans la base de données.
                cursor.close()  # Fermer le curseur.

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
    # Appel de la méthode pour retirer les unités du produit avec la référence .
    Del_product.delete_product_quantity(reference="1234", quantity=289)

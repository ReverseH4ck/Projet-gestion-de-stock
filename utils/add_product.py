import mysql.connector  # Module pour interagir avec une base de données MariaDB/MySQL.
from utils import \
    db_connection_open as db_connection  # Importation de la fonction de connexion depuis un module utilitaire.


class Product_Add:
    """
    Classe contenant une méthode statique pour ajouter ou mettre à jour des produits dans une table de la base de données.
    """

    @staticmethod
    def product_adder(nom_produit: str, prix: int, modele: str, reference: str, quantitee: int):
        """
        Ajoute un nouveau produit ou met à jour la quantité d'un produit existant dans la table 'produits'.

        Args:
            nom_produit (str): Nom du produit à ajouter.
            prix (int): Prix du produit.
            modele (str): Modèle du produit.
            reference (str): Référence unique du produit.
            quantitee (int): Quantité à ajouter ou mettre à jour.
        """
        conn = None  # Initialisation de la variable de connexion.

        try:
            # Établir une connexion à la base de données.
            conn = db_connection.connexion()

            # Vérifier si la connexion est établie et active.
            if conn and conn.is_connected():
                cursor = conn.cursor()  # Création d'un curseur pour exécuter des requêtes SQL.

                # Requête pour vérifier si un produit avec cette référence existe déjà.
                query_check = "SELECT quantitee FROM produits WHERE reference = %s"
                cursor.execute(query_check, (reference,))
                result = cursor.fetchone()  # Récupération du premier résultat.

                if result:
                    # Si le produit existe, mettre à jour la quantité.
                    current_quantity = result[0]  # Quantité actuelle.
                    new_quantity = current_quantity + quantitee  # Nouvelle quantité après ajout.
                    query_update = """
                    UPDATE produits
                    SET quantitee = %s
                    WHERE reference = %s
                    """
                    cursor.execute(query_update, (new_quantity, reference))
                else:
                    # Si le produit n'existe pas, insérer une nouvelle ligne.
                    query_insert = """
                    INSERT INTO produits (nom_produit, prix, modele, reference, quantitee)
                    VALUES (%s, %s, %s, %s, %s)
                    """
                    cursor.execute(query_insert, (nom_produit, prix, modele, reference, quantitee))

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
    # Appel de la méthode pour ajouter ou mettre à jour un produit dans la table 'produits'.
    Product_Add.product_adder(
        nom_produit="iPhone X",  # Nom du produit.
        prix=1000,  # Prix du produit.
        modele="2022",  # Modèle du produit.
        reference="1234",  # Référence unique du produit.
        quantitee=100  # Quantité à ajouter.
    )

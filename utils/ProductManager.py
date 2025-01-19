from Gestion_de_stocks.produits import produit  # Importation de la classe Article pour centraliser les informations des produits.
from utils import db_connection_open as db_connection  # Importation de la fonction de connexion depuis un module utilitaire.


class ProductManager:
    """
    Classe pour gérer les opérations CRUD (Create, Read, Update, Delete) sur les produits en utilisant la classe Article.
    """

    @staticmethod
    def add_or_update_product(article: produit.Article):
        """
        Ajoute ou met à jour un produit dans la base de données.

        Args:
            article (Article): Une instance de la classe Article contenant les informations du produit.
        """
        conn = None
        try:
            conn = db_connection.connexion()
            if conn and conn.is_connected():
                cursor = conn.cursor()

                # Vérifier si le produit existe déjà
                query_check = "SELECT quantitee FROM produits WHERE reference = %s"
                cursor.execute(query_check, (article.reference,))
                result = cursor.fetchone()

                if result:
                    # Mise à jour de la quantité
                    current_quantity = result[0]
                    new_quantity = current_quantity + article.quantitee
                    query_update = "UPDATE produits SET quantitee = %s WHERE reference = %s"
                    cursor.execute(query_update, (new_quantity, article.reference))
                else:
                    # Insertion d'un nouveau produit
                    query_insert = """
                    INSERT INTO produits (nom_produit, prix, modele, reference, quantitee)
                    VALUES (%s, %s, %s, %s, %s)
                    """
                    cursor.execute(query_insert, (
                        article.nom_produit,
                        article.prix,
                        article.modele,
                        article.reference,
                        article.quantitee,
                    ))

                conn.commit()
                cursor.close()
        except Exception as e:
            print(f"Erreur lors de l'ajout ou de la mise à jour du produit : {e}")
        finally:
            if conn and conn.is_connected():
                conn.close()

    @staticmethod
    def delete_product(reference: str, quantity: int):
        """
        Supprime ou met à jour la quantité d'un produit dans la base de données.

        Args:
            reference (str): La référence unique du produit à traiter.
            quantity (int): La quantité à retirer.
        """
        conn = None
        try:
            conn = db_connection.connexion()
            if conn and conn.is_connected():
                cursor = conn.cursor()

                # Vérifier la quantité actuelle
                query_select = "SELECT quantitee FROM produits WHERE reference = %s"
                cursor.execute(query_select, (reference,))
                result = cursor.fetchone()

                if not result:
                    print("Produit introuvable.")
                    return

                current_quantity = result[0]
                if quantity >= current_quantity:
                    # Suppression complète
                    query_delete = "DELETE FROM produits WHERE reference = %s"
                    cursor.execute(query_delete, (reference,))
                else:
                    # Mise à jour de la quantité
                    new_quantity = current_quantity - quantity
                    query_update = "UPDATE produits SET quantitee = %s WHERE reference = %s"
                    cursor.execute(query_update, (new_quantity, reference))

                conn.commit()
                cursor.close()
        except Exception as e:
            print(f"Erreur lors de la suppression ou mise à jour : {e}")
        finally:
            if conn and conn.is_connected():
                conn.close()

    @staticmethod
    def view_all_products():
        """
        Affiche tous les produits dans la base de données.
        """
        conn = None
        try:
            conn = db_connection.connexion()
            if conn and conn.is_connected():
                cursor = conn.cursor()

                # Récupérer tous les produits
                query = "SELECT nom_produit, prix, modele, reference, quantitee FROM produits"
                cursor.execute(query)
                rows = cursor.fetchall()

                if rows:
                    for row in rows:
                        print(f"Nom : {row[0]}, Prix : {row[1]}, Modèle : {row[2]}, Référence : {row[3]}, Quantité : {row[4]}")
                else:
                    print("Aucun produit disponible.")

                cursor.close()
        except Exception as e:
            print(f"Erreur lors de la récupération des produits : {e}")
        finally:
            if conn and conn.is_connected():
                conn.close()


# Exemple d'utilisation
if __name__ == '__main__':
    # Ajouter ou mettre à jour un produit
    new_article = produit.Article("iPhone 12", 1200, "2023", "5678", 50)
    ProductManager.add_or_update_product(new_article)

    # Supprimer une quantité ou un produit entier
    ProductManager.delete_product("5678", 201)

    # Afficher tous les produits
    ProductManager.view_all_products()

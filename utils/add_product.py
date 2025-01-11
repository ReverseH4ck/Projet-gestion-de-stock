import mysql.connector
from utils import db_connection_open as db_connection


class Product_Add:
    @staticmethod
    def product_adder(nom_produit: str, prix: int, modele: str, reference: str, quantitee: int):
        conn = None
        try:
            conn = db_connection.connexion()

            if conn and conn.is_connected():
                cursor = conn.cursor()

                query_check = "SELECT quantitee FROM produits WHERE reference = %s"
                cursor.execute(query_check, (reference,))
                result = cursor.fetchone()

                if result:
                    current_quantity = result[0]
                    new_quantity = current_quantity + quantitee
                    query_update = """
                    UPDATE produits
                    SET quantitee = %s
                    WHERE reference = %s
                    """
                    cursor.execute(query_update, (new_quantity, reference))
                else:
                    query_insert = """
                    INSERT INTO produits (nom_produit, prix, modele, reference, quantitee)
                    VALUES (%s, %s, %s, %s, %s)
                    """
                    cursor.execute(query_insert, (nom_produit, prix, modele, reference, quantitee))

                conn.commit()
                cursor.close()

        except mysql.connector.Error as err:
            print(f"Erreur MariaDB : {err}")
        except Exception as e:
            print(f"Erreur : {e}")
        finally:
            if conn and conn.is_connected():
                conn.close()


if __name__ == '__main__':
    ProductManager.upsert_product(
        nom_produit="iphone X",
        prix=1000,
        modele="2022",
        reference="1234",
        quantitee=100
    )

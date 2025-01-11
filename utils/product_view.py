import mysql.connector
from utils import db_connection_open as db_connection


class Product_View:
    @staticmethod
    def view_products():
        conn = None
        try:
            conn = db_connection.connexion()

            if conn and conn.is_connected():
                cursor = conn.cursor()

                query = "SELECT * FROM produits"
                cursor.execute(query)

                rows = cursor.fetchall()

                if rows:
                    for row in rows:
                        print(f"Nom : {row[0]}, Prix : {row[1]}, Modèle : {row[2]}, Référence : {row[3]}, Quantité : {row[4]}")
                else:
                    print("La table 'produits' est vide.")

                cursor.close()

        except mysql.connector.Error as err:
            print(f"Erreur MariaDB : {err}")
        except Exception as e:
            print(f"Erreur : {e}")
        finally:
            if conn and conn.is_connected():
                conn.close()


if __name__ == '__main__':
    Product_View.view_products()

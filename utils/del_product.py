import mysql.connector
from utils import db_connection_open as db_connection


class Del_product:
    @staticmethod
    def delete_product_quantity(reference: str, quantity: int):
        conn = None
        try:
            conn = db_connection.connexion()

            if conn and conn.is_connected():
                cursor = conn.cursor()

                query_select = "SELECT quantitee FROM produits WHERE reference = %s"
                cursor.execute(query_select, (reference,))
                result = cursor.fetchone()

                if not result:
                    return

                current_quantity = result[0]

                if quantity >= current_quantity:
                    query_delete = "DELETE FROM produits WHERE reference = %s"
                    cursor.execute(query_delete, (reference,))
                else:
                    new_quantity = current_quantity - quantity
                    query_update = "UPDATE produits SET quantitee = %s WHERE reference = %s"
                    cursor.execute(query_update, (new_quantity, reference))

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
    Del_product.delete_product_quantity(reference="1234", quantity=289)

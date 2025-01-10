import mysql.connector
from mysql.connector import Error
from get_db_info import Log


def connexion():
    # Informations de connexion
    log_DB = Log.settings()

    try:
        # Connexion à la base de données
        connection = mysql.connector.connect(**log_DB)

        if connection.is_connected():
            print("Connexion réussie !")

    except Error as e:
        print(f"Erreur de connexion : {e}")

    finally:
        try:
            if connection.is_connected():
                connection.close()
                print("Connexion fermée.")
        except NameError:
            pass  # In case 'connection' was never defined
        except Exception as e:
            print(f"Error while closing the connection: {e}")


if __name__ == "__main__":
    connexion()

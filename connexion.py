import mysql.connector
from mysql.connector import Error
from settings import Log

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
        # Fermer la connexion si elle est ouverte
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Connexion fermée.")

if __name__ == "__main__":
    connexion()
import mysql.connector
import json

class DatabaseUtils:
    def __init__(self):
        # Chargement automatique de config.json
        with open("config.json", "r") as f:
            config = json.load(f)

            self.conn = mysql.connector.connect(
                host=config['host'],
                port=config['port'],
                user=config['user'],
                password=config['password'],
                database=config['name']
            )
        self.cursor = self.conn.cursor()

    def create_articles_table(self):
        """Crée la table articles si elle n'existe pas déjà."""
        create_table_query = """
            CREATE TABLE IF NOT EXISTS articles (
                reference INT PRIMARY KEY,
                nom_article VARCHAR(255) NOT NULL,
                quantite INT NOT NULL,
                prix INT NOT NULL
            )
        """
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def create_fournisseur_table(self):
        create_table_query = """
            CREATE TABLE IF NOT EXISTS fournisseurs (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nom_fournisseur VARCHAR(255) NOT NULL,
                numero INT NOT NULL,
                adresse VARCHAR(255) NOT NULL
            )
        """
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def create_clients_table(self):
        create_table_query = """
            CREATE TABLE IF NOT EXISTS clients (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nom_client VARCHAR(255) NOT NULL,
                numero INT NOT NULL,
                adresse VARCHAR(255) NOT NULL
            )
        """
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def close(self):
        """Ferme proprement la connexion."""
        self.cursor.close()
        self.conn.close()

## Exemple d'utilisation directe (si exécuté seul)
#if __name__ == "__main__":
#    db = DatabaseUtils()
#    db.create_articles_table()
#    db.create_fournisseur_table()
#    db.create_clients_table()
#    db.close()
#
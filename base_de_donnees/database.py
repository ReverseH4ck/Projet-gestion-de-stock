class DatabaseUtils:
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

    def creat_table(self):
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

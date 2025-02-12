class DatabaseUtils:
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

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
        adresse VARCHAR(255) NOT NULL,)
        """


        self.cursor.execute(create_table_query)
        self.conn.commit()


    def create_clients_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS clients (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nom_client VARCHAR(255) NOT NULL,
        numero INT NOT NULL,
        adresse VARCHAR(255) NOT NULL,)
        """

        self.cursor.execute(create_table_query)
        self.conn.commit()
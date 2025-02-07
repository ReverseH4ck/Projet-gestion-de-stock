import mysql.connector
import json
import os


class DatabaseManager:
    """A helper class to manage database connections."""

    @staticmethod
    def get_database_config():
        """Load database configuration from config.json."""
        try:
            # Define the path to the config.json file
            config_path = os.path.join(os.path.dirname(__file__), "..", "..", "config.json")
            with open(config_path, "r", encoding="utf-8") as config_file:
                config = json.load(config_file)
                return config
        except FileNotFoundError:
            print(f"Erreur : Le fichier config.json est introuvable.")
        except json.JSONDecodeError:
            print("Erreur : Impossible de décoder config.json.")
        return None

    @staticmethod
    def get_connection():
        """Create and return a new database connection."""
        config = DatabaseManager.get_database_config()
        if not config:
            print("Impossible de charger les informations de configuration de la base de données.")
            return None

        try:
            connection = mysql.connector.connect(
                host=config.get("database-host"),
                port=config.get("database-port"),
                user=config.get("database-user"),
                password=config.get("database-password"),
                database=config.get("database-name")
            )
            print("Connexion à la base de données réussie !")
            return connection
        except mysql.connector.Error as e:
            print(f"Erreur lors de la connexion à la base de données : {e}")
            return None

    @staticmethod
    def close_connection(connection):
        """Close the database connection."""
        if connection and connection.is_connected():
            connection.close()
            print("Connexion à la base de données fermée.")


class Article:
    def __init__(self, nom_produit, prix, modele, reference, quantitee):
        self.nom_produit = nom_produit
        self.prix = float(prix)
        self.modele = modele
        self.reference = reference
        self.quantitee = quantitee

    @staticmethod
    def ensure_table_exists(connection):
        """Ensure the `articles` table exists in the database."""
        cursor = connection.cursor()
        try:
            # Check if the table exists
            cursor.execute("SHOW TABLES LIKE 'articles'")
            result = cursor.fetchone()
            if not result:
                # Create the `articles` table if it doesn't exist
                print("La table 'articles' n'existe pas. Création de la table.")
                create_table_query = """
                CREATE TABLE articles (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nom VARCHAR(255) NOT NULL,
                    prix DECIMAL(10, 2) NOT NULL,
                    modele VARCHAR(255) NOT NULL,
                    reference VARCHAR(255) NOT NULL UNIQUE,
                    quantitee INT NOT NULL
                );
                """
                cursor.execute(create_table_query)
                connection.commit()
                print("Table 'articles' créée avec succès.")
        except mysql.connector.Error as error:
            print(f"Erreur lors de la vérification ou création de la table : {error}")
        finally:
            cursor.close()

    @staticmethod
    def ajout_article():
        """Create a new article instance based on user input."""
        nom_produit = input("Nom article : ")
        prix = float(input("Prix : "))
        modele = input("Modèle : ")
        reference = input("Référence : ")
        quantitee = int(input("Quantité : "))
        return Article(nom_produit, prix, modele, reference, quantitee)

    @staticmethod
    def ajouter_article_a_la_base(article):
        """Add an article to the database."""
        connection = DatabaseManager.get_connection()
        if not connection:
            print("Impossible de se connecter à la base. Annulation de l'ajout.")
            return

        cursor = None
        try:
            # Ensure the table exists
            Article.ensure_table_exists(connection)

            # Add the article to the table
            cursor = connection.cursor()
            query = "INSERT INTO articles (nom, prix, modele, reference, quantitee) VALUES (%s, %s, %s, %s, %s)"
            data = (article.nom_produit, article.prix, article.modele, article.reference, article.quantitee)
            cursor.execute(query, data)
            connection.commit()
            print("Article ajouté avec succès.")
        except mysql.connector.Error as error:
            print(f"Erreur lors de l'ajout de l'article : {error}")
        finally:
            if cursor:
                cursor.close()
            DatabaseManager.close_connection(connection)

    @staticmethod
    def supprimer_article(reference):
        """Remove an article from the database by reference."""
        connection = DatabaseManager.get_connection()
        if not connection:
            print("Impossible de se connecter à la base. Annulation de la suppression.")
            return

        cursor = None
        try:
            # Ensure the table exists
            Article.ensure_table_exists(connection)

            cursor = connection.cursor()
            query = "DELETE FROM articles WHERE reference = %s"
            cursor.execute(query, (reference,))
            connection.commit()
            if cursor.rowcount > 0:
                print("Article supprimé avec succès.")
            else:
                print("Aucun article trouvé avec cette référence.")
        except mysql.connector.Error as error:
            print(f"Erreur lors de la suppression de l'article : {error}")
        finally:
            if cursor:
                cursor.close()
            DatabaseManager.close_connection(connection)

    @staticmethod
    def recuperer_article(reference):
        """Retrieve an article from the database by reference."""
        connection = DatabaseManager.get_connection()
        if not connection:
            print("Impossible de se connecter à la base. Annulation de la récupération.")
            return None

        cursor = None
        try:
            # Ensure the table exists
            Article.ensure_table_exists(connection)

            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM articles WHERE reference = %s"
            cursor.execute(query, (reference,))
            resultat = cursor.fetchone()

            if resultat:
                # Create an Article instance with the retrieved data
                article = Article(
                    nom_produit=resultat["nom"],
                    prix=resultat["prix"],
                    modele=resultat["modele"],
                    reference=resultat["reference"],
                    quantitee=resultat["quantitee"]
                )

                # Display all information about the article
                print("\nInformations sur l'article récupéré :")
                print(f"Nom du produit : {article.nom_produit}")
                print(f"Prix : {article.prix:.2f} €")
                print(f"Modèle : {article.modele}")
                print(f"Référence : {article.reference}")
                print(f"Quantité en stock : {article.quantitee}")

                return article
            else:
                print("Article introuvable.")
                return None
        except mysql.connector.Error as error:
            print(f"Erreur lors de la récupération de l'article : {error}")
        finally:
            if cursor:
                cursor.close()
            DatabaseManager.close_connection(connection)

    def modifier_article(self):
        """Modify the current article instance based on user input."""
        print(f"Article actuel : {self.nom_produit} | Référence : {self.reference}")

        # Ask for new values (keep current values if input is empty)
        self.nom_produit = input(f"Nom [{self.nom_produit}] : ") or self.nom_produit
        self.prix = float(input(f"Prix [{self.prix}] : ") or self.prix)
        self.modele = input(f"Modèle [{self.modele}] : ") or self.modele
        self.quantitee = int(input(f"Quantité [{self.quantitee}] : ") or self.quantitee)

    def sauvegarde_modification(self):
        """Save modifications of the article to the database."""
        connection = DatabaseManager.get_connection()
        if not connection:
            print("Impossible de se connecter à la base. Annulation de la sauvegarde.")
            return

        cursor = None
        try:
            # Ensure the table exists
            Article.ensure_table_exists(connection)

            cursor = connection.cursor()
            query = "UPDATE articles SET nom = %s, prix = %s, modele = %s, quantitee = %s WHERE reference = %s"
            data = (self.nom_produit, self.prix, self.modele, self.quantitee, self.reference)
            cursor.execute(query, data)
            connection.commit()

            if cursor.rowcount > 0:
                print("Article modifié avec succès.")
            else:
                print("Aucune modification n'a été effectuée.")
        except mysql.connector.Error as error:
            print(f"Erreur lors de la mise à jour : {error}")
        finally:
            if cursor:
                cursor.close()
            DatabaseManager.close_connection(connection)


if __name__ == "__main__":
    while True:
        print("\nQue voulez-vous faire ?")
        print("1. Récupérer un article")
        print("2. Ajouter un nouvel article")
        print("3. Supprimer un article")
        print("4. Quitter")
        choix = input("Entrez votre choix : ").strip()

        if choix == "1":
            ref = input("Entrez la référence de l'article à récupérer : ").strip()
            article = Article.recuperer_article(ref)
            if not article:
                print("Aucun article n'a été trouvé.")
            else:
                print("\nInformations sur l'article récupéré :")
                print(f"Nom du produit : {article.nom_produit}")
                print(f"Prix : {article.prix:.2f} €")
                print(f"Modèle : {article.modele}")
                print(f"Référence : {article.reference}")
                print(f"Quantité en stock : {article.quantitee}")

        elif choix == "2":
            print("Ajout d'un nouvel article :")
            nouvel_article = Article.ajout_article()
            Article.ajouter_article_a_la_base(nouvel_article)

        elif choix == "3":
            ref = input("Entrez la référence de l'article à supprimer : ").strip()
            Article.supprimer_article(ref)

        elif choix == "4":
            print("Au revoir !")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")

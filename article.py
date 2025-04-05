import mysql.connector
from mysql.connector import errorcode
import json
import os


class Article:
    def __init__(self, nom_article, reference, quantite, prix, id_fournisseur=None):
        self.nom_article = nom_article
        self.reference = reference
        self.quantite = quantite
        self.prix = prix

    def __str__(self):
        return f"{self.nom_article}\n (Réf: {self.reference}) - Quantité: {self.quantite}, Prix: {self.prix}€"

def load_config(filename='config.json'):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, filename)

    if not os.path.exists(config_path):
        print(f"Erreur : Le fichier {config_path} est introuvable.")
        exit(1)

    with open(config_path, 'r') as file:
        return json.load(file)

config = load_config()

class ArticleManager:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host=config['host'],
                port=config['port'],
                user=config['user'],
                password=config['password'],
                database=config['database']
            )
            self.cursor = self.conn.cursor()
            self._init_db()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Erreur d'authentification : vérifiez votre utilisateur et mot de passe.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("La base de données n'existe pas.")
            else:
                print(err)
            exit(1)

    def _init_db(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS articles (
                    reference INT PRIMARY KEY,
                    nom_article VARCHAR(255) NOT NULL,
                    quantite INT DEFAULT 0,
                    prix FLOAT DEFAULT 0
                )
            """)
            self.conn.commit()
        except mysql.connector.Error as err:
            print("Erreur lors de la création de la table :", err)

    def add_article(self):
        nom_article = input("Nom de l'article : ")
        try:
            reference = int(input("Entrez la référence de l'article (nombre entier) : "))
            quantite = int(input("Entrez la quantité : "))
            prix = int(input("Entrez le prix de l'article : "))
        except ValueError:
            print("Erreur : Veuillez saisir des nombres valides pour la référence, la quantité et le prix.")
            return

        self.cursor.execute("SELECT * FROM articles WHERE reference = %s", (reference,))
        if self.cursor.fetchone() is not None:
            print("Erreur : Un article avec cette référence existe déjà.")
            return

        article = Article(nom_article, reference, quantite, prix)
        try:
            self.cursor.execute(
                "INSERT INTO articles (reference, nom_article, quantite, prix) VALUES (%s, %s, %s, %s)",
                (article.reference, article.nom_article, article.quantite, article.prix)
            )
            self.conn.commit()
            print(f"Article {article.nom_article} (Réf: {article.reference}) ajouté avec succès.")
        except mysql.connector.Error as err:
            print("Erreur lors de l'insertion de l'article :", err)

    def edit_article(self):
        try:
            reference = int(input("Entrez la référence de l'article à modifier : "))
        except ValueError:
            print("Erreur : La référence doit être un nombre entier.")
            return

        self.cursor.execute("SELECT * FROM articles WHERE reference = %s", (reference,))
        result = self.cursor.fetchone()
        if result is None:
            print("Erreur : Aucun article trouvé avec cette référence.")
            return

        print("Article actuel:")
        print(f"Nom: {result[1]}, Quantité: {result[2]}, Prix: {result[3]}€")

        new_nom = input("Nouveau nom (laisser vide pour conserver l'actuel): ")
        new_quantite_input = input("Nouvelle quantité (laisser vide pour conserver l'actuelle): ")
        new_prix_input = input("Nouveau prix (laisser vide pour conserver l'actuel): ")

        new_nom = new_nom if new_nom.strip() != "" else result[1]
        try:
            new_quantite = int(new_quantite_input) if new_quantite_input.strip() != "" else result[2]
            new_prix = int(new_prix_input) if new_prix_input.strip() != "" else result[3]
        except ValueError:
            print("Erreur : La quantité et le prix doivent être des nombres entiers.")
            return

        try:
            self.cursor.execute(
                "UPDATE articles SET nom_article = %s, quantite = %s, prix = %s WHERE reference = %s",
                (new_nom, new_quantite, new_prix, reference)
            )
            self.conn.commit()
            print(f"Article (Réf: {reference}) modifié avec succès.")
        except mysql.connector.Error as err:
            print("Erreur lors de la modification de l'article :", err)

    def delete_article(self):
        try:
            reference = int(input("Entrez la référence de l'article à supprimer : "))
        except ValueError:
            print("Erreur : La référence doit être un nombre entier.")
            return

        self.cursor.execute("SELECT * FROM articles WHERE reference = %s", (reference,))
        if self.cursor.fetchone() is None:
            print("Erreur : Aucun article trouvé avec cette référence.")
            return

        confirmation = input("Êtes-vous sûr de vouloir supprimer cet article ? (o/n): ")
        if confirmation.lower() == "o":
            try:
                self.cursor.execute("DELETE FROM articles WHERE reference = %s", (reference,))
                self.conn.commit()
                print(f"Article (Réf: {reference}) supprimé avec succès.")
            except mysql.connector.Error as err:
                print("Erreur lors de la suppression de l'article :", err)
        else:
            print("Suppression annulée.")

    def list_articles(self):
        print("=== Liste des articles ===")
        self.cursor.execute("SELECT * FROM articles")
        articles = self.cursor.fetchall()
        if articles:
            for art in articles:
                print(f"Réf: {art[0]}, Nom: {art[1]}, Quantité: {art[2]}, Prix: {art[3]}€")
        else:
            print("Aucun article trouvé.")

    def close(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    config = load_config()
    print("Configuration chargée :", config)

    try:
        connexion = mysql.connector.connect(
            host=config["host"],
            port=config["port"],
            user=config["user"],
            password=config["password"]
        )
        print("Connexion réussie à la base de données !")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Erreur d'authentification : vérifiez votre utilisateur et mot de passe.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de données n'existe pas.")
        else:
            print("Erreur lors de la connexion :", err)
        exit(1)

class Fournisseur:
    def __init__(self, id, nom):
        self.id = id
        self.nom = nom

    def __str__(self):
        return self.nom


        self.id = id
        self.nom = nom

class FournisseurManager:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
        self._init_db()

    def _init_db(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS fournisseurs (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nom VARCHAR(255) NOT NULL UNIQUE
            )
        """)
        self.conn.commit()

    def get_all(self):
        self.cursor.execute("SELECT id, nom FROM fournisseurs")
        rows = self.cursor.fetchall()
        return [Fournisseur(id, nom) for id, nom in rows]

    
    def add(self, nom):
        try:
            self.cursor.execute("INSERT INTO fournisseurs (nom) VALUES (%s)", (nom,))
            self.conn.commit()
        except mysql.connector.IntegrityError as e:
            print(f"Erreur : Le fournisseur '{nom}' existe déjà.")
        self.conn.commit()

    def update(self, id, nouveau_nom):
        self.cursor.execute("UPDATE fournisseurs SET nom = %s WHERE id = %s", (nouveau_nom, id))
        self.conn.commit()

    def delete(self, id):
        self.cursor.execute("DELETE FROM fournisseurs WHERE id = %s", (id,))
        self.conn.commit()

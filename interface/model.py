
from article import ArticleManager, Article, FournisseurManager, Fournisseur

class Model:
    def __init__(self):
        self.article_manager = ArticleManager()
        self.fournisseur_manager = FournisseurManager(self.article_manager.conn)

    def ajouter_produit(self, nom, reference, quantite, prix):
        article = Article(nom, reference, quantite, prix)
        self.article_manager.cursor.execute(
            "INSERT INTO articles (reference, nom_article, quantite, prix) VALUES (%s, %s, %s, %s)",
            (article.reference, article.nom_article, article.quantite, article.prix)
        )
        self.article_manager.conn.commit()

    def modifier_produit(self, reference, nom, quantite, prix):
        self.article_manager.cursor.execute(
            "UPDATE articles SET nom_article = %s, quantite = %s, prix = %s WHERE reference = %s",
            (nom, quantite, prix, reference)
        )
        self.article_manager.conn.commit()

    def supprimer_produit(self, reference):
        self.article_manager.cursor.execute("DELETE FROM articles WHERE reference = %s", (reference,))
        self.article_manager.conn.commit()

    def get_produits(self):
        self.article_manager.cursor.execute("SELECT reference, nom_article, quantite, prix FROM articles")
        articles = self.article_manager.cursor.fetchall()
        return [Article(nom, ref, qte, prix) for ref, nom, qte, prix in articles]

    # Fournisseurs en base de données
    def ajouter_fournisseur(self, nom):
        self.fournisseur_manager.add(nom)

    def modifier_fournisseur(self, id, nouveau_nom):
        self.fournisseur_manager.update(id, nouveau_nom)

    def supprimer_fournisseur(self, id):
        self.fournisseur_manager.delete(id)

    def get_fournisseurs(self):
        return self.fournisseur_manager.get_all()


from article import ArticleManager, Article, FournisseurManager, Fournisseur
import pandas as pd

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

    def get_fournisseurs(self):
        return self.fournisseur_manager.get_all()

    def ajouter_fournisseur(self, nom):
        self.fournisseur_manager.add(nom)

    def modifier_fournisseur(self, id, nouveau_nom):
        self.fournisseur_manager.update(id, nouveau_nom)

    def supprimer_fournisseur(self, id):
        self.fournisseur_manager.delete(id)

    def exporter_donnees(self, chemin):
        self.article_manager.cursor.execute("SELECT reference, nom_article, quantite, prix FROM articles")
        produits = self.article_manager.cursor.fetchall()
        df_produits = pd.DataFrame(produits, columns=["Référence", "Nom", "Quantité", "Prix"])

        self.article_manager.cursor.execute("SELECT id, nom FROM fournisseurs")
        fournisseurs = self.article_manager.cursor.fetchall()
        df_fournisseurs = pd.DataFrame(fournisseurs, columns=["ID", "Nom"])

        df_ventes = pd.DataFrame(columns=["(Aucune vente enregistrée)"])

        with pd.ExcelWriter(chemin, engine='xlsxwriter') as writer:
            df_produits.to_excel(writer, sheet_name="Produits", index=False)
            df_fournisseurs.to_excel(writer, sheet_name="Fournisseurs", index=False)
            df_ventes.to_excel(writer, sheet_name="Ventes", index=False)


    def effectuer_vente(self, reference, quantite_vendue):
        self.article_manager.cursor.execute(
            "SELECT quantite FROM articles WHERE reference = %s", (reference,)
        )
        result = self.article_manager.cursor.fetchone()
        if result:
            nouvelle_quantite = result[0] - quantite_vendue
            if nouvelle_quantite < 0:
                raise ValueError("Stock insuffisant pour cette vente.")
            self.article_manager.cursor.execute(
                "UPDATE articles SET quantite = %s WHERE reference = %s",
                (nouvelle_quantite, reference)
            )
            self.article_manager.conn.commit()
        else:
            raise ValueError("Article non trouvé pour cette référence.")
    
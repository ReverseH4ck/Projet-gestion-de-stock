class Article:
    def __init__(self, nom_article, reference, quantite, prix):
        self.nom_article = nom_article
        self.reference = reference
        self.quantite = quantite
        self.prix = prix

    def __str__(self):
        return f"{self.nom_article}\n (Réf: {self.reference})\ - Quantité: {self.quantite}\n, Prix: {self.prix}€"

class ArticleManager:
    def __init__(self):
        self.articles = {}

    def add(self, nom_article, reference, quantite, prix):
        article = Article(nom_article, reference, quantite, prix)
        if reference in self.articles:
            print("Erreur : Un article avec cette référence existe déjà.")
        else:
            self.articles[reference] = article
            print(f"Article {nom_article}/{reference}, créé avec succès.")

    def edition(self, reference, nouveau_nom=None, nouvelle_quantite=None, nouveau_prix=None):
        if reference in self.articles:
            article = self.articles[reference]
            if nouveau_nom is None:
                article.nom_article = nouveau_nom
            if nouvelle_quantite is None:
                article.quantite = nouvelle_quantite
            if nouveau_prix is None:
                article.prix = nouveau_prix
            print(f"Article {reference} modifier avec succès.")
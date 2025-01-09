from produits.produit import Article
from fournisseurs.fournisseur import Fournisseur


def main():

  # fonction ajout d'article et de fournisseur
  produit = Article.ajout_article()
  produit.caracteristique_produit()

  fournisseur = Fournisseur.ajout_fournisseur()
  fournisseur.information_fournisseur()


if __name__ == "__main__":
  main()

from produits.produit import Article
from fournisseurs.fournisseur import Fournisseur
from produits.iphone import Iphone
from fournisseurs.amazon import Amazon


def main():
  iphone16_pro_max = Iphone("iphone 16", 1700, "iphone 16 pro max", 50, 987654321, "Noir",  256)
  iphone16_pro_max.caracteristique()

  nom_fournisseur = input("Entrez votre nom : ")
  num_fournisseur = int(input("Entrez votre numero : "))
  email = input("Entrez votre email : ")
  adresse = input("Entrez votre adresse : ")

  amazon = Amazon(nom_fournisseur, num_fournisseur, email, adresse)
  amazon.informations()

if __name__ == "__main__":
  main()

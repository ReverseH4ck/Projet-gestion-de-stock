from produits.produit import Article
from fournisseurs.fournisseur import Fournisseur
from produits.iphone import Iphone
from fournisseurs.amazon import Amazon

def main():
  iphone16_pro_max = Iphone("iphone 16", 1700, "iphone 16 pro max", 50, 987654321, "Noir",  256)
  iphone16_pro_max.caracteristique()

  amazon = Amazon("Amazon", "06123457891", "test@gmail.com", "Dans ton cul")
  amazon.informations()

if __name__ == "__main__":
  main()

from produits.produit import Produit
from produits.iphone import Iphone

def main():
  iphone16_pro_max = Iphone("iphone 16", 1700, "iphone 16 pro max", 50, "Noir",987654321,  256)
  iphone16_pro_max.caracteristique()


if __name__ == "__main__":
  main()
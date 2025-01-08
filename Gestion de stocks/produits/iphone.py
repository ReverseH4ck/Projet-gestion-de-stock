from produits.produit import Produit

class Iphone(Produit):
  def __init__(self, nom_produit, modele, reference, prix, quantitee, couleur, memoire):
    super().__init__(nom_produit, modele, reference, prix, quantitee)
    self.couleur = couleur
    self.memoire = memoire
  
  def caracteristique(self):
    super().caracteristique()
    print(f"Couleur : {self.couleur}\n"
          f"Mémoire : {self.memoire} Go")
  
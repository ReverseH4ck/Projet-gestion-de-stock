class Produit:
  def __init__(self, nom_produit, prix, modele, reference, quantitee):
    self.nom_produit = nom_produit
    self.modele = modele
    self.reference = reference
    self.prix = prix
    self.quantitee = quantitee

  def caracteristique(self):
    print(f"Produit : {self.nom_produit}\n"
          f"Prix : {self.prix} €\n"
          f"Modèle : {self.modele}\n"
          f"Reference : {self.reference}\n"
          f"Quantitée : {self.quantitee}")


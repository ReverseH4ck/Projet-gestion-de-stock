class Article:
  def __init__(self, nom_produit, prix, modele, reference, quantitee):
    self.nom_produit = nom_produit
    self.prix = int(prix)
    self.modele = modele
    self.reference = reference
    self.quantitee = quantitee

  def ajout_article():
    nom_produit = input("Nom article : ")
    prix = int(input("Prix : "))
    modele = input("Modèle : ")
    reference = input("Référence : ")
    quantitee = input("Quantées : ")
    return Article(nom_produit, prix, modele, reference, quantitee)
  
  def get_nom_produit(self):
    return self.nom_produit

  def get_prix(self):
    return self.prix

  def get_modele(self):
    return self.modele
  
  def get_reference(self):
    return self.reference
  
  def get_quantiee(self):
    return self.quantitee
  

  def caracteristique_produit(self):
    print(f"Produit : {self.get_nom_produit()}\n"
          f"Prix : {self.get_prix()} €\n"
          f"Modèle : {self.get_modele()}\n"
          f"Reference : {self.get_reference()}\n"
          f"Quantitée : {self.get_quantiee()}")




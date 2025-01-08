class Fournisseur:
  def __init__(self, nom_fournisseur, num_telephone, email, adresse):
    self.nom_fournisseur = nom_fournisseur
    self.num_telephone = num_telephone
    self.email = email
    self.adresse = adresse

  def information_fournisseur(self):
    print(f"Nom du fournisseur : {self.nom_fournisseur}\n"
          f"Numéro de téléphone : {self.num_telephone}\n"
          f"Email : {self.email}\n"
          f"Adresse : {self.adresse}")


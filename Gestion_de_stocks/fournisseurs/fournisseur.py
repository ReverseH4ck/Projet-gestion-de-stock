class Fournisseur:
  def __init__(self, nom_fournisseur, num_telephone, email, adresse):
    self.nom_fournisseur = nom_fournisseur
    self.num_telephone = num_telephone
    self.email = email
    self.adresse = adresse
  
  def ajout_fournisseur():
    nom_fournisseur = input("Nom fournisseur : ")
    num_telephone = input("Numéro téléphone : ")
    email = input("Votre email : ")
    adresse = input("Votre adresse : ")
    return Fournisseur(nom_fournisseur, num_telephone, email, adresse)
  
  def get_nom_fournisseur(self):
    return self.nom_fournisseur
  
  def get_num_fournisseur(self):
    return self.num_telephone
  
  def get_email(self):
    return self.email
  
  def get_adresse(self):
    return self.adresse

  def information_fournisseur(self):
    print(f"Nom du fournisseur : {self.get_nom_fournisseur()}\n"
          f"Numéro de téléphone : {self.get_num_fournisseur()}\n"
          f"Email : {self.get_email()}\n"
          f"Adresse : {self.get_adresse()}")



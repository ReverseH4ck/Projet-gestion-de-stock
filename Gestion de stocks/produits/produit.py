import mysql.connector
from utils import db_connection_open

class Article:
  def __init__(self, nom_produit, prix, modele, reference, quantitee):
    self.nom_produit = nom_produit
    self.prix = float(prix)
    self.modele = modele
    self.reference = reference
    self.quantitee = quantitee

  def ajout_article():
    nom_produit = input("Nom article : ")
    prix = float(input("Prix : "))
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

  def recuperer_article(reference):
    try:
      connection = db_connection()
      cursor = connection.cursor(dictionary=True)
      query = "SELECT * FROM articles WHERE reference = %s"
      cursor.execute(query, (reference,))
      resultat = cursor.fetchone()

      if resultat:
        return Article(
          nom_produit=resultat["nom"],
          prix=resultat["prix"],
          modele=resultat["modele"],
          reference=resultat["reference"],
          quantitee=resultat["quantitee"],
        )
      else:
        print("Article introuvable.")
        return None
      
    except mysql.connection.Error as error:
      print(f"Erreur lors de la connexion a la base {error}")

    finally:
      if connection.is_connected():
        cursor.close()
        connection.close()

  def modifier_article(self):
    print(f"Article actuel : {self.get_nom_produit} Référence : {self.get_reference}")

 # Demande les nouvelles valeurs à l'utilisateur (laisser vide pour conserver la valeur actuelle)
    self.nom_produit = input(f"[{self.nom_produit}] : ") or self.nom_produit
    self.prix = float(input(f"[{self.prix}] : ") or self.prix)
    self.modele = input(f"Modèle : [{self.modele}] : ") or self.modele
    self.quantitee = int(input(f"Quantité [{self.quantitee}] : ") or self.quantitee)
  
  def sauvegarde_modification(self):
    try:
      connection = db_connection()
      cursor = connection.cursor()
      query = "UPDATE articles SET nom = %s, modele = %s, quantitee = %s WHERE reference = %s"
      data = (self.nom_produit, self.prix, self.modele, self.quantitee, self.reference)
      cursor.execute(query, (data,))
      connection.commit()

      if cursor.rowcount > 0:
        print("Article modifier avec succès.")
      else:
        print("Aucune modification n'a été effectuée.")
    except mysql.connector.Error as error:
      print(f"Erreur lors de la mise à jour : {error}")
    finally:
      if connection.is_connected():
        cursor.close()
        connection.close()
  
  # Exemple d'utilisation
if __name__ == "__main__":
    # Récupérer un article à partir de la base
  ref = input("Entrez la référence de l'article à modifier : ")
  article = Article.recuperer_article(ref)

  if article:
    article.caracteristique_produit()
    article.modifier_article()
    article.sauvegarde_modification()

# Modèle : gestion des données et logique métier

class Model:
    def __init__(self):
        self.liste_produits = []
        self.liste_fournisseurs = []

    def ajouter_produit(self, produit):
        self.liste_produits.append(produit)

    def modifier_produit(self, index, nouveau_nom):
        if 0 <= index < len(self.liste_produits):
            self.liste_produits[index] = nouveau_nom

    def supprimer_produit(self, index):
        if 0 <= index < len(self.liste_produits):
            del self.liste_produits[index]

    def get_produits(self):
        return self.liste_produits

    def ajouter_fournisseur(self, nom):
        if nom.strip() and nom not in self.liste_fournisseurs:
            self.liste_fournisseurs.append(nom)

    def modifier_fournisseur(self, index, nouveau_nom):
        if 0 <= index < len(self.liste_fournisseurs):
            self.liste_fournisseurs[index] = nouveau_nom

    def supprimer_fournisseur(self, index):
        if 0 <= index < len(self.liste_fournisseurs):
            del self.liste_fournisseurs[index]

    def get_fournisseurs(self):
        return self.liste_fournisseurs
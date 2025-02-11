class Model:
    def __init__(self):
        self.produits = []  # Liste de produits (pour exemple)

    def ajouter_produit(self, produit):
        self.produits.append(produit)

    def supprimer_produit(self, index):
        if 0 <= index < len(self.produits):
            self.produits.pop(index)

    def modifier_produit(self, index, produit):
        if 0 <= index < len(self.produits):
            self.produits[index] = produit

    def get_produits(self):
        return self.produits

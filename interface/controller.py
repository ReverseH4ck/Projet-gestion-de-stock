from view import View
from model import Model

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Initialisation des actions
        self.view.set_action_buttons(self.ajouter_produit, self.modifier_produit, self.supprimer_produit, self.quit)
        self.view.bproduits.config(command=self.view.switch_to_produits)
        self.view.switch_to_principal()

    def ajouter_produit(self):
        produit = "Nouveau Produit"  # Exemple : cela pourrait être un input de l'utilisateur
        self.model.ajouter_produit(produit)
        self.view.afficher_produits(self.model.get_produits())

    def modifier_produit(self):
        # Code pour modifier un produit (exemple simplifié)
        if self.model.get_produits():
            self.model.modifier_produit(0, "Produit Modifié")
        self.view.afficher_produits(self.model.get_produits())

    def supprimer_produit(self):
        # Code pour supprimer un produit (exemple simplifié)
        if self.model.get_produits():
            self.model.supprimer_produit(0)
        self.view.afficher_produits(self.model.get_produits())

    def quit(self):
        self.view.window.quit()

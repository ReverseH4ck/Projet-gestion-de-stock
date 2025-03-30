# Contrôleur : relie la vue et le modèle

from .model import Model
from Interface.view import View

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Connexion des actions aux boutons
        self.view.set_action_buttons(self.ajouter_produit, self.modifier_produit, self.supprimer_produit, self.quitter_application)
        self.view.bproduits.config(command=self.view.switch_to_produits)
        self.view.switch_to_principal()

    def ajouter_produit(self):
        nom = self.view.get_input_produit()
        if nom.strip():
            self.model.ajouter_produit(nom)
            self.view.afficher_produits(self.model.get_produits())

    def modifier_produit(self):
        index = self.view.get_selected_index()
        nouveau_nom = self.view.get_input_produit()
        if index is not None and nouveau_nom.strip():
            self.model.modifier_produit(index, nouveau_nom)
            self.view.afficher_produits(self.model.get_produits())

    def supprimer_produit(self):
        index = self.view.get_selected_index()
        if index is not None:
            self.model.supprimer_produit(index)
            self.view.selected_index = None
            self.view.set_input_produit("")
            self.view.afficher_produits(self.model.get_produits())

    def quitter_application(self):
        self.view.window.quit()

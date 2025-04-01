# Contrôleur : relie la vue et le modèle

from interface.model import Model

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.set_action_buttons(self.ajouter_produit, self.modifier_produit, self.supprimer_produit, self.quitter_application)
        self.view.set_action_fournisseur(self.ajouter_fournisseur, self.modifier_fournisseur, self.supprimer_fournisseur)

        self.view.bproduits.config(command=self.view.switch_to_produits)
        self.view.bfournisseurs.config(command=self.afficher_fournisseurs)
        self.view.switch_to_principal()
        self.rafraichir_produits()
        self.rafraichir_fournisseurs()

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

    def ajouter_fournisseur(self):
        nom = self.view.get_nouveau_fournisseur()
        if nom.strip():
            self.model.ajouter_fournisseur(nom)
            self.rafraichir_fournisseurs()
            self.view.entry_nouveau_fournisseur.delete(0, 'end')

    def modifier_fournisseur(self):
        index = self.view.get_selected_fournisseur_index()
        nouveau_nom = self.view.get_nouveau_fournisseur()
        if index is not None and nouveau_nom.strip():
            self.model.modifier_fournisseur(index, nouveau_nom)
            self.rafraichir_fournisseurs()
            self.view.entry_nouveau_fournisseur.delete(0, 'end')

    def supprimer_fournisseur(self):
        index = self.view.get_selected_fournisseur_index()
        if index is not None:
            self.model.supprimer_fournisseur(index)
            self.rafraichir_fournisseurs()
            self.view.entry_nouveau_fournisseur.delete(0, 'end')

    def afficher_fournisseurs(self):
        self.view.switch_to_fournisseurs()
        self.rafraichir_fournisseurs()

    def rafraichir_produits(self):
        self.view.afficher_produits(self.model.get_produits())

    def rafraichir_fournisseurs(self):
        self.view.afficher_liste_fournisseurs(self.model.get_fournisseurs())

    def quitter_application(self):
        self.view.window.quit()

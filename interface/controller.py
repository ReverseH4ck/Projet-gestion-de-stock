
from interface.model import Model
from tkinter import filedialog, messagebox

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.set_action_buttons(self.ajouter_produit, self.modifier_produit, self.supprimer_produit)
        self.view.bproduits.config(command=self.view.switch_to_produits)
        self.view.brapports.config(command=self.view.switch_to_rapports)
        self.view.bexporter.config(command=self.exporter_rapport)

        self.view.bfournisseurs.config(command=self.view.switch_to_fournisseurs)
        self.view.bajouter_fournisseur.config(command=self.ajouter_fournisseur)
        self.view.bmodifier_fournisseur.config(command=self.modifier_fournisseur)
        self.view.bsupprimer_fournisseur.config(command=self.supprimer_fournisseur)

        self.rafraichir_produits()
        self.rafraichir_fournisseurs()

    def ajouter_produit(self):
        data = self.view.get_input_produit()
        try:
            nom = data['nom']
            reference = int(data['reference'])
            quantite = int(data['quantite'])
            prix = float(data['prix'])
        except ValueError:
            print("Champs invalides")
            return

        self.model.ajouter_produit(nom, reference, quantite, prix)
        self.rafraichir_produits()

    def modifier_produit(self):
        index = self.view.get_selected_index()
        if index is None:
            print("Aucun produit sélectionné")
            return

        produit = self.model.get_produits()[index]
        data = self.view.get_input_produit()
        try:
            nom = data['nom']
            quantite = int(data['quantite'])
            prix = float(data['prix'])
        except ValueError:
            print("Champs invalides")
            return

        self.model.modifier_produit(produit.reference, nom, quantite, prix)
        self.rafraichir_produits()

    def supprimer_produit(self):
        index = self.view.get_selected_index()
        if index is None:
            print("Aucun produit sélectionné")
            return

        produit = self.model.get_produits()[index]
        self.model.supprimer_produit(produit.reference)
        self.rafraichir_produits()

    def rafraichir_produits(self):
        self.view.afficher_produits(self.model.get_produits())

    def afficher_fournisseurs(self):
        self.view.switch_to_fournisseurs()
        self.rafraichir_fournisseurs()

    def rafraichir_fournisseurs(self):
        self.view.afficher_fournisseurs(self.model.get_fournisseurs())

    def ajouter_fournisseur(self):
        nom = self.view.entry_fournisseur.get()
        if nom.strip():
            self.model.ajouter_fournisseur(nom)
            self.view.entry_fournisseur.delete(0, 'end')
            self.rafraichir_fournisseurs()

    def modifier_fournisseur(self):
        index = self.view.get_selected_fournisseur_index()
        nouveau_nom = self.view.entry_fournisseur.get()
        if index is not None and nouveau_nom.strip():
            fournisseur = self.model.get_fournisseurs()[index]
            self.model.modifier_fournisseur(fournisseur.id, nouveau_nom)
            self.view.entry_fournisseur.delete(0, 'end')
            self.view.selected_fournisseur_index = None
            self.rafraichir_fournisseurs()

    def supprimer_fournisseur(self):
        index = self.view.get_selected_fournisseur_index()
        if index is not None:
            fournisseur = self.model.get_fournisseurs()[index]
            self.model.supprimer_fournisseur(fournisseur.id)
            self.view.entry_fournisseur.delete(0, 'end')
            self.view.selected_fournisseur_index = None
            self.rafraichir_fournisseurs()

    def exporter_rapport(self):
        chemin = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Fichier Excel", "*.xlsx")],
            title="Enregistrer le rapport"
        )
        if chemin:
            try:
                self.model.exporter_donnees(chemin)
                messagebox.showinfo("Export réussi", f"Le rapport a été exporté vers :\n{chemin}")
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors de l'export : {e}")

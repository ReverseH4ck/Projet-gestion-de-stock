
from tkinter import *

class View:
    def __init__(self, window):
        self.window = window
        self.window.title("Gestion de Stock")
        self.window.geometry("1280x720")
        self.window.config(bg='#1e1e1e')

        self.selected_index = None
        self.selected_fournisseur_index = None

        # Frames principales
        self.frame_menu = Frame(window, bg='#1e1e1e')
        self.frame_menu.pack(side=LEFT, fill=Y)

        self.frame_principal = Frame(window, bg='#1e1e1e')
        self.frame_produit = Frame(window, bg='#1e1e1e')
        self.frame_fournisseur = Frame(window, bg='#1e1e1e')
        self.frame_ventes = Frame(window, bg='#1e1e1e')
        self.frame_rapports = Frame(window, bg='#1e1e1e')

        self.frame_principal.pack(expand=YES, fill=BOTH)

        # Menu boutons
        self.baccueil = Button(self.frame_menu, text="🏠 Accueil", bg='#2980b9', fg='white', command=self.switch_to_principal)
        self.bproduits = Button(self.frame_menu, text="📦 Produits", bg='#2980b9', fg='white', command=self.switch_to_produits)
        self.bfournisseurs = Button(self.frame_menu, text="🚚 Fournisseurs", bg='#2980b9', fg='white', command=self.switch_to_fournisseurs)
        self.bventes = Button(self.frame_menu, text="🛒 Ventes", bg='#2980b9', fg='white', command=self.switch_to_ventes)
        self.brapports = Button(self.frame_menu, text="📊 Rapports", bg='#2980b9', fg='white', command=self.switch_to_rapports)
        self.bquitter = Button(self.frame_menu, text="❌ Quitter", bg='#e74c3c', fg='white', command=self.window.quit)

        for b in [self.baccueil, self.bproduits, self.bfournisseurs, self.bventes, self.brapports, self.bquitter]:
            b.pack(pady=10, fill=X)

        # Accueil
        self.label_accueil = Label(self.frame_principal, text="Bienvenue dans l'application de gestion de stock", font=("Impact", 20), fg='white', bg='#1e1e1e')
        self.label_accueil.pack(pady=20)

        # Produits
        self.label_titre_produits = Label(self.frame_produit, text="Gestion des Produits", font=("Impact", 30), bg='#1e1e1e', fg='white')
        self.label_titre_produits.pack(pady=20)
        self._produits_ui()

        # Fournisseurs
        self.label_titre_fournisseurs = Label(self.frame_fournisseur, text="Fournisseurs", font=("Impact", 30), bg='#1e1e1e', fg='white')
        self.label_titre_fournisseurs.pack(pady=20)
        self._fournisseurs_ui()

        # Ventes
        self.label_titre_ventes = Label(self.frame_ventes, text="Module Ventes", font=("Impact", 30), bg='#1e1e1e', fg='white')
        self.label_titre_ventes.pack(pady=20)
        self._ventes_ui()

        # Rapports
        self.label_titre_rapports = Label(self.frame_rapports, text="Module Rapports", font=("Impact", 30), bg='#1e1e1e', fg='white')
        self.label_titre_rapports.pack(pady=20)
        self._rapports_ui()

    def _produits_ui(self):
        self.frame_form = Frame(self.frame_produit, bg='#1e1e1e')
        self.frame_form.pack(pady=10)

        self.entry_nom = Entry(self.frame_form, width=30)
        self.entry_reference = Entry(self.frame_form, width=30)
        self.entry_quantite = Entry(self.frame_form, width=30)
        self.entry_prix = Entry(self.frame_form, width=30)

        Label(self.frame_form, text="Nom", bg='#1e1e1e', fg='white').grid(row=0, column=0)
        self.entry_nom.grid(row=0, column=1, padx=10, pady=5)
        Label(self.frame_form, text="Référence", bg='#1e1e1e', fg='white').grid(row=1, column=0)
        self.entry_reference.grid(row=1, column=1, padx=10, pady=5)
        Label(self.frame_form, text="Quantité", bg='#1e1e1e', fg='white').grid(row=2, column=0)
        self.entry_quantite.grid(row=2, column=1, padx=10, pady=5)
        Label(self.frame_form, text="Prix", bg='#1e1e1e', fg='white').grid(row=3, column=0)
        self.entry_prix.grid(row=3, column=1, padx=10, pady=5)

        self.frame_btns = Frame(self.frame_produit, bg='#1e1e1e')
        self.frame_btns.pack(pady=10)
        self.bajouter = Button(self.frame_btns, text="Ajouter", bg='#27ae60', fg='white')
        self.bmodifier = Button(self.frame_btns, text="Modifier", bg='#f39c12', fg='white')
        self.bsupprimer = Button(self.frame_btns, text="Supprimer", bg='#c0392b', fg='white')
        self.bajouter.grid(row=0, column=0, padx=10)
        self.bmodifier.grid(row=0, column=1, padx=10)
        self.bsupprimer.grid(row=0, column=2, padx=10)

        self.frame_liste = Frame(self.frame_produit, bg='#1e1e1e')
        self.frame_liste.pack(pady=20)

    def _fournisseurs_ui(self):
        self.entry_fournisseur = Entry(self.frame_fournisseur, width=50)
        self.entry_fournisseur.pack(pady=10)
        self.bajouter_fournisseur = Button(self.frame_fournisseur, text="Ajouter Fournisseur", bg='#27ae60', fg='white')
        self.bmodifier_fournisseur = Button(self.frame_fournisseur, text="Modifier Fournisseur", bg='#f39c12', fg='white')
        self.bsupprimer_fournisseur = Button(self.frame_fournisseur, text="Supprimer Fournisseur", bg='#c0392b', fg='white')
        self.bajouter_fournisseur.pack(pady=5)
        self.bmodifier_fournisseur.pack(pady=5)
        self.bsupprimer_fournisseur.pack(pady=5)

    def _ventes_ui(self):
        self.label_info_ventes = Label(self.frame_ventes, text="Sélection d'article + quantité vendue", font=("Courier", 14), bg='#1e1e1e', fg='white')
        self.label_info_ventes.pack(pady=10)
        self.entry_qte_vendue = Entry(self.frame_ventes, width=20)
        self.entry_qte_vendue.pack(pady=5)
        self.bvalider_vente = Button(self.frame_ventes, text="Valider Vente", bg='#27ae60', fg='white')
        self.bvalider_vente.pack(pady=5)

    def _rapports_ui(self):
        self.label_rapport = Label(self.frame_rapports, text="État du stock affiché ici", font=("Courier", 14), bg='#1e1e1e', fg='white')
        self.label_rapport.pack(pady=10)
        self.bexporter = Button(self.frame_rapports, text="Exporter", bg='#3498db', fg='white')
        self.bexporter.pack(pady=5)

    def switch_to_principal(self):
        self._switch_frame(self.frame_principal)

    def switch_to_produits(self):
        self._switch_frame(self.frame_produit)

    def switch_to_fournisseurs(self):
        self._switch_frame(self.frame_fournisseur)

    def switch_to_ventes(self):
        self._switch_frame(self.frame_ventes)

    def switch_to_rapports(self):
        self._switch_frame(self.frame_rapports)

    def _switch_frame(self, target_frame):
        for f in [self.frame_principal, self.frame_produit, self.frame_fournisseur, self.frame_ventes, self.frame_rapports]:
            f.pack_forget()
        target_frame.pack(expand=YES, fill=BOTH)

    def afficher_produits(self, produits):
        for widget in self.frame_liste.winfo_children():
            widget.destroy()
        for index, produit in enumerate(produits):
            texte = f"{produit.nom_article} | Réf: {produit.reference} | Qte: {produit.quantite} | Prix: {produit.prix}€"
            bouton = Button(self.frame_liste, text=texte, command=lambda i=index: self.selectionner_produit(i), width=100)
            bouton.pack(pady=2)

    def selectionner_produit(self, index):
        self.selected_index = index

    def get_selected_index(self):
        return self.selected_index

    def get_input_produit(self):
        return {
            'nom': self.entry_nom.get(),
            'reference': self.entry_reference.get(),
            'quantite': self.entry_quantite.get(),
            'prix': self.entry_prix.get()
        }

    def set_input_produit(self, produit):
        self.entry_nom.delete(0, END)
        self.entry_nom.insert(0, produit.nom_article)
        self.entry_reference.delete(0, END)
        self.entry_reference.insert(0, produit.reference)
        self.entry_quantite.delete(0, END)
        self.entry_quantite.insert(0, produit.quantite)
        self.entry_prix.delete(0, END)
        self.entry_prix.insert(0, produit.prix)

    def set_action_buttons(self, ajout, modifier, supprimer):
        self.bajouter.config(command=ajout)
        self.bmodifier.config(command=modifier)
        self.bsupprimer.config(command=supprimer)

    def afficher_fournisseurs(self, fournisseurs):
        if hasattr(self, 'frame_liste_fournisseurs'):
            for widget in self.frame_liste_fournisseurs.winfo_children():
                widget.destroy()
        else:
            self.frame_liste_fournisseurs = Frame(self.frame_fournisseur, bg='#1e1e1e')
            self.frame_liste_fournisseurs.pack(pady=20)

        for index, nom in enumerate(fournisseurs):
            bg_color = "#1abc9c" if index == self.selected_fournisseur_index else "#34495e"
            bouton = Button(self.frame_liste_fournisseurs, text=nom, bg=bg_color, fg="white",
                            width=40, command=lambda i=index: self.selectionner_fournisseur(i))
            bouton.pack(pady=2)

    def selectionner_fournisseur(self, index):
        self.selected_fournisseur_index = index
        self.entry_fournisseur.delete(0, END)
        fournisseurs = self.controller.model.get_fournisseurs()
        if 0 <= index < len(fournisseurs):
            self.entry_fournisseur.insert(0, fournisseurs[index])

    def get_selected_fournisseur_index(self):
        return self.selected_fournisseur_index

    def set_controller(self, controller):
        self.controller = controller

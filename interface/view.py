# Vue : interface graphique en tkinter

from tkinter import *

class View:
    def __init__(self, window):
        self.window = window
        self.window.title("Projet")
        self.window.geometry("1920x1080")
        self.window.config(background='#1e1e1e')
        self.window.minsize(480, 360)

        # Frame menu à gauche
        self.frame_menu = Frame(window, bg='#1e1e1e')
        self.frame_menu.pack(side=LEFT, anchor=N, padx=30)

        # Deux pages principales
        self.frame_produit = Frame(window, bg='#1e1e1e')
        self.frame_principal = Frame(window, bg='#1e1e1e')
        self.frame_principal.pack(expand=YES)

        # Titre page d'accueil
        self.label_titre_accueil = Label(self.frame_principal, text="APPLICATION", font=("Impact", 60), bg='#1e1e1e', fg='#ecf0f1')
        self.label_titre_accueil.pack(pady=40)

        self.label_sous_titre = Label(self.frame_principal, text="Bienvenue sur l'application", font=("Courier", 20), bg='#1e1e1e', fg='#bdc3c7')
        self.label_sous_titre.pack(pady=10)

        # Boutons menu principal
        self.bproduits = Button(self.frame_principal, text="📦 Produits", font=("Impact", 20), bg='#2980b9', fg='white', relief=FLAT)
        self.bfournisseurs = Button(self.frame_principal, text="🚚 Fournisseurs", font=("Impact", 20), bg='#2980b9', fg='white', relief=FLAT)
        self.bventes = Button(self.frame_principal, text="🛒 Ventes", font=("Impact", 20), bg='#2980b9', fg='white', relief=FLAT)
        self.brapports = Button(self.frame_principal, text="📊 Rapports", font=("Impact", 20), bg='#2980b9', fg='white', relief=FLAT)
        self.bquitter = Button(self.frame_principal, text="❌ Quitter", font=("Impact", 20), bg='#e74c3c', fg='white', relief=FLAT)

        # Placement des boutons
        for btn in [self.bproduits, self.bfournisseurs, self.bventes, self.brapports, self.bquitter]:
            btn.pack(pady=15)
            self.apply_button_hover_animation(btn)

        # Bouton retour menu
        self.bmenu = Button(self.frame_principal, text="🏠", font=("Impact", 20), bg='#2980b9', fg='white', relief=FLAT)
        self.bmenu.place(x=30, y=30)
        self.apply_button_hover_animation(self.bmenu)

        # Page Produits
        self.selected_index = None

        self.label_titre_produits = Label(self.frame_produit, text="Produits", font=("Impact", 60), bg='#1e1e1e', fg='#ecf0f1')
        self.label_titre_produits.pack(pady=(40, 20))

        # Boutons Ajouter / Modifier / Supprimer en ligne
        self.frame_actions = Frame(self.frame_produit, bg='#1e1e1e')
        self.frame_actions.pack(pady=10)

        self.bajouter = Button(self.frame_actions, text="+ Ajouter", font=("Impact", 16), bg='#2980b9', fg='white', relief=FLAT)
        self.bmodifier = Button(self.frame_actions, text="✏️ Modifier", font=("Impact", 16), bg='#2980b9', fg='white', relief=FLAT)
        self.bsupprimer = Button(self.frame_actions, text="💥 Supprimer", font=("Impact", 16), bg='#2980b9', fg='white', relief=FLAT)

        self.bajouter.grid(row=0, column=0, padx=20)
        self.bmodifier.grid(row=0, column=1, padx=20)
        self.bsupprimer.grid(row=0, column=2, padx=20)

        # Champ de texte pour saisir ou modifier un produit
        self.champ_texte = Entry(self.frame_produit, font=("Courier", 16), bg="#2c3e50", fg="white", insertbackground="white", relief=FLAT)
        self.champ_texte.pack(pady=40, ipadx=100, ipady=10)

        # Frame pour afficher les produits
        self.frame_liste_produits = Frame(self.frame_produit, bg='#1e1e1e')
        self.frame_liste_produits.pack(pady=30)

        for btn in [self.bajouter, self.bmodifier, self.bsupprimer]:
            self.apply_button_hover_animation(btn)

    # Boutons survol effet
    def apply_button_hover_animation(self, button):
        def on_enter(event, b=button):
            b.config(bg='#3498db' if b != self.bquitter else '#c0392b')
        def on_leave(event, b=button):
            b.config(bg='#2980b9' if b != self.bquitter else '#e74c3c')
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

    # Affichage des produits (horizontal)
    def afficher_produits(self, produits):
        for widget in self.frame_liste_produits.winfo_children():
            widget.destroy()

        for index, nom in enumerate(produits):
            bouton = Button(self.frame_liste_produits, text=nom, font=("Courier", 14), bg="#34495e", fg="white", relief=RAISED, padx=10, pady=5)
            bouton.grid(row=0, column=index, padx=10)
            bouton.bind("<Button-1>", lambda e, i=index: self.selectionner_produit(i))

    # Obtenir contenu champ
    def get_input_produit(self):
        return self.champ_texte.get()

    # Écrire dans le champ
    def set_input_produit(self, texte):
        self.champ_texte.delete(0, END)
        self.champ_texte.insert(0, texte)

    # Index du produit sélectionné
    def get_selected_index(self):
        return self.selected_index

    # Sélection d’un produit
    def selectionner_produit(self, index):
        self.selected_index = index
        self.set_input_produit(self.frame_liste_produits.winfo_children()[index]["text"])

    # Associer les fonctions aux boutons
    def set_action_buttons(self, ajout, modifier, supprimer, quitter):
        self.bajouter.config(command=ajout)
        self.bmodifier.config(command=modifier)
        self.bsupprimer.config(command=supprimer)
        self.bquitter.config(command=quitter)
        self.bmenu.config(command=self.switch_to_principal)

    # Aller à la page Produits
    def switch_to_produits(self):
        self.frame_principal.pack_forget()
        self.frame_produit.pack(expand=YES, fill=BOTH)

    # Retour à l'accueil
    def switch_to_principal(self):
        self.frame_produit.pack_forget()
        self.frame_principal.pack(expand=YES, fill=BOTH)

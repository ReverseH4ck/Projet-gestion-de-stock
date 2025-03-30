# Vue : interface graphique en tkinter

from tkinter import *

class View:
    def __init__(self, window):
        self.window = window
        self.window.title("Projet")
        self.window.geometry("1920x1080")
        self.window.config(background='#1e1e1e')
        self.window.minsize(480, 360)

        # Frame menu (pour d'éventuelles options futures)
        self.frame_menu = Frame(window, bg='#1e1e1e')
        self.frame_menu.pack(side=LEFT, anchor=N, padx=30)

        # Frames pour la page d'accueil et la page produits
        self.frame_principal = Frame(window, bg='#1e1e1e')
        self.frame_produit = Frame(window, bg='#1e1e1e')
        self.frame_principal.pack(expand=YES)

        # Bouton Menu toujours visible (enfant direct de la fenêtre)
        self.bmenu = Button(self.window, text="🏠", font=("Impact", 20), bg='#2980b9', fg='white', relief=FLAT, padx=10, pady=5, bd=0)
        self.bmenu.place(x=30, y=30)

        # Page d'accueil : titres
        self.label_titre_accueil = Label(self.frame_principal, text="APPLICATION", font=("Impact", 60), bg='#1e1e1e', fg='#ecf0f1')
        self.label_titre_accueil.pack(pady=40)

        self.label_sous_titre = Label(self.frame_principal, text="Bienvenue sur l'application", font=("Courier", 20), bg='#1e1e1e', fg='#bdc3c7')
        self.label_sous_titre.pack(pady=10)

        # Boutons du menu principal
        self.bproduits = Button(self.frame_principal, text="📦 Produits", font=("Impact", 20), bg='#2980b9', fg='white', relief=FLAT)
        self.bfournisseurs = Button(self.frame_principal, text="🚚 Fournisseurs", font=("Impact", 20), bg='#2980b9', fg='white', relief=FLAT)
        self.bventes = Button(self.frame_principal, text="🛒 Ventes", font=("Impact", 20), bg='#2980b9', fg='white', relief=FLAT)
        self.brapports = Button(self.frame_principal, text="📊 Rapports", font=("Impact", 20), bg='#2980b9', fg='white', relief=FLAT)
        self.bquitter = Button(self.frame_principal, text="❌ Quitter", font=("Impact", 20), bg='#e74c3c', fg='white', relief=FLAT)

        for btn in [self.bproduits, self.bfournisseurs, self.bventes, self.brapports, self.bquitter]:
            btn.pack(pady=15)
            self.apply_button_hover_animation(btn)

        # Page Produits
        self.selected_index = None

        # Titre de la page produits
        self.label_titre_produits = Label(self.frame_produit, text="Produits", font=("Impact", 60), bg='#1e1e1e', fg='#ecf0f1')
        self.label_titre_produits.pack(pady=(40, 20))

        # Boutons d'action alignés horizontalement
        self.frame_actions = Frame(self.frame_produit, bg='#1e1e1e')
        self.frame_actions.pack(pady=10)

        self.bajouter = Button(self.frame_actions, text="+ Ajouter", font=("Impact", 16), bg='#2980b9', fg='white', relief=FLAT, padx=20, pady=10)
        self.bmodifier = Button(self.frame_actions, text="✏️ Modifier", font=("Impact", 16), bg='#2980b9', fg='white', relief=FLAT, padx=20, pady=10)
        self.bsupprimer = Button(self.frame_actions, text="💥 Supprimer", font=("Impact", 16), bg='#2980b9', fg='white', relief=FLAT, padx=20, pady=10)

        self.bajouter.grid(row=0, column=0, padx=20)
        self.bmodifier.grid(row=0, column=1, padx=20)
        self.bsupprimer.grid(row=0, column=2, padx=20)

        # Champ de saisie pour ajouter/modifier un produit
        self.champ_texte = Entry(self.frame_produit, font=("Courier", 16), bg="#2c3e50", fg="white", insertbackground="white", relief=FLAT)
        self.champ_texte.pack(pady=40, ipadx=100, ipady=10)

        # Zone d'affichage des produits (boutons alignés horizontalement)
        self.frame_liste_produits = Frame(self.frame_produit, bg='#1e1e1e')
        self.frame_liste_produits.pack(pady=30)

        for btn in [self.bajouter, self.bmodifier, self.bsupprimer, self.bmenu]:
            self.apply_button_hover_animation(btn)

    # Animation simple sur le survol des boutons
    def apply_button_hover_animation(self, button):
        def on_enter(event, b=button):
            if b == self.bquitter:
                b.config(bg='#c0392b')
            else:
                b.config(bg='#3498db')
        def on_leave(event, b=button):
            if b == self.bquitter:
                b.config(bg='#e74c3c')
            else:
                b.config(bg='#2980b9')
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

    # Afficher les produits sous forme de boutons
    def afficher_produits(self, produits):
        for widget in self.frame_liste_produits.winfo_children():
            widget.destroy()
        for index, nom in enumerate(produits):
            bouton = Button(self.frame_liste_produits, text=nom, font=("Courier", 14), bg="#34495e", fg="white", relief=RAISED, padx=10, pady=5)
            bouton.grid(row=0, column=index, padx=10)
            bouton.bind("<Button-1>", lambda e, i=index: self.selectionner_produit(i))

    # Retourner le contenu du champ de texte
    def get_input_produit(self):
        return self.champ_texte.get()

    # Mettre à jour le champ de texte avec le nom d'un produit
    def set_input_produit(self, texte):
        self.champ_texte.delete(0, END)
        self.champ_texte.insert(0, texte)

    # Obtenir l'index du produit sélectionné
    def get_selected_index(self):
        return self.selected_index

    # Lorsqu'un produit est sélectionné, remplir le champ de texte
    def selectionner_produit(self, index):
        self.selected_index = index
        self.set_input_produit(self.frame_liste_produits.winfo_children()[index]["text"])

    # Associer les fonctions aux boutons d'action
    def set_action_buttons(self, ajout, modifier, supprimer, quitter):
        self.bajouter.config(command=ajout)
        self.bmodifier.config(command=modifier)
        self.bsupprimer.config(command=supprimer)
        self.bquitter.config(command=quitter)
        self.bmenu.config(command=self.switch_to_principal)

    # Afficher la page produits
    def switch_to_produits(self):
        self.frame_principal.pack_forget()
        self.frame_produit.pack(expand=YES, fill=BOTH)

    # Retour à la page d'accueil
    def switch_to_principal(self):
        self.frame_produit.pack_forget()
        self.frame_principal.pack(expand=YES, fill=BOTH)

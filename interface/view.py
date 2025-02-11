from tkinter import *
from tkinter import ttk


class View:
    def __init__(self, window):
        self.window = window
        self.window.title("Projet")
        self.window.geometry("1920x1080")
        self.window.iconbitmap("")
        self.window.config(background='#212122')
        self.window.minsize(480, 360)

        self.frame_menu = Frame(window, bg='#212122')
        self.frame_menu.pack(side=LEFT, anchor=N, padx=30)

        self.frame_produit = Frame(window, bg='#212122')
        
        self.frame_principal = Frame(window, bg='#212122')
        self.frame_principal.pack(expand=YES)

        # Titre et sous-titre de la page principale
        self.label_title = Label(self.frame_principal, text="APPLICATION", font=("Impact", 60), bg='#212122', fg='#c75402')
        self.label_title.pack(expand=YES)

        self.label_subtitle = Label(self.frame_principal, text="Bienvenue sur l'application", font=("Courier", 20), bg='#212122', fg='white')
        self.label_subtitle.pack(expand=YES)

        # Boutons de la page principale
        self.bproduits = Button(self.frame_principal, text="📦 Produits", font=("Impact", 20), bg='#c75402', fg='white')
        self.bfournisseurs = Button(self.frame_principal, text="🚚 Fournisseurs", font=("Impact", 20), bg='#c75402', fg='white')
        self.bventes = Button(self.frame_principal, text="🛒 Ventes", font=("Impact", 20), bg='#c75402', fg='white')
        self.brapports = Button(self.frame_principal, text="📊 Rapports", font=("Impact", 20), bg='#c75402', fg='white')
        self.bquitter = Button(self.frame_principal, text="❌ Quitter", font=("Impact", 20), bg='#c75402', fg='white')

        self.bproduits.pack(pady=25, fill=X)
        self.bfournisseurs.pack(pady=25, fill=X)
        self.bventes.pack(pady=25, fill=X)
        self.brapports.pack(pady=25, fill=X)
        self.bquitter.pack(pady=25, fill=X)

        # Boutons de la page Produits
        self.bajout = Button(self.frame_produit, text="+ Ajouter", font=("Impact", 20), bg='#c75402', fg='white')
        self.bmodifier = Button(self.frame_produit, text="✏️ Modifier", font=("Impact", 20), bg='#c75402', fg='white')
        self.bsupprimer = Button(self.frame_produit, text="💥 Supprimer", font=("Impact", 20), bg='#c75402', fg='white')

        self.bajout.pack(pady=25)
        self.bajout.place(x=470, y=120)

        self.bmodifier.pack(pady=25)
        self.bmodifier.place(x=595, y=120)

        self.bsupprimer.pack(pady=25)
        self.bsupprimer.place(x=755, y=120)

    def afficher_produits(self, produits):
        """Met à jour l'affichage des produits"""
        for widget in self.frame_produit.winfo_children():
            widget.destroy()  # On détruit les anciens widgets
        
        # Ajoute le label pour les produits
        label_title2 = Label(self.frame_produit, text="Produits", font=("Impact", 60), bg='#212122', fg='#c75402')
        label_title2.pack(pady=20)
        
        # Affiche les produits sous forme de liste
        for produit in produits:
            label_produit = Label(self.frame_produit, text=produit, font=("Courier", 20), bg='#212122', fg='white')
            label_produit.pack(pady=10)

    def set_action_buttons(self, ajout, modifier, supprimer, quitter):
        self.bajout.config(command=ajout)
        self.bmodifier.config(command=modifier)
        self.bsupprimer.config(command=supprimer)
        self.bquitter.config(command=quitter)

    def switch_to_produits(self):
        """Affiche la page Produits"""
        self.frame_principal.pack_forget()
        self.frame_produit.pack(expand=YES, fill=BOTH)

    def switch_to_principal(self):
        """Retourne à la page principale"""
        self.frame_produit.pack_forget()
        self.frame_principal.pack(expand=YES, fill=BOTH)

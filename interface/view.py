from tkinter import *
from tkinter import ttk

class View:
    def __init__(self, window):
        # Paramètres de la fenêtre principale
        self.window = window
        self.window.title("Projet")
        self.window.geometry("1920x1080")
        self.window.config(background='#1e1e1e')
        self.window.minsize(480, 360)

        # Frame Menu
        self.frame_menu = Frame(window, bg='#1e1e1e')
        self.frame_menu.pack(side=LEFT, anchor=N, padx=30)

        # Frame Produit et Frame Principal
        self.frame_produit = Frame(window, bg='#1e1e1e')
        self.frame_principal = Frame(window, bg='#1e1e1e')
        self.frame_principal.pack(expand=YES)

        # Titres
        self.label_title = Label(self.frame_principal, text="APPLICATION", font=("Impact", 60), bg='#1e1e1e', fg='#ecf0f1')
        self.label_title.pack(expand=YES)

        self.label_subtitle = Label(self.frame_principal, text="Bienvenue sur l'application", font=("Courier", 20), bg='#1e1e1e', fg='#bdc3c7')
        self.label_subtitle.pack(expand=YES)

        # Boutons principaux
        self.bproduits = Button(self.frame_principal, text="📦 Produits", font=("Impact", 20), bg='#2980b9', fg='white', relief=FLAT)
        self.bfournisseurs = Button(self.frame_principal, text="🚚 Fournisseurs", font=("Impact", 20), bg='#2980b9', fg='white', relief=FLAT)
        self.bventes = Button(self.frame_principal, text="🛒 Ventes", font=("Impact", 20), bg='#2980b9', fg='white', relief=FLAT)
        self.brapports = Button(self.frame_principal, text="📊 Rapports", font=("Impact", 20), bg='#2980b9', fg='white', relief=FLAT)
        self.bquitter = Button(self.frame_principal, text="❌ Quitter", font=("Impact", 20), bg='#e74c3c', fg='white', relief=FLAT)

        # Placement des boutons principaux
        self.bproduits.pack(pady=25)
        self.bfournisseurs.pack(pady=25)
        self.bventes.pack(pady=25)
        self.brapports.pack(pady=25)
        self.bquitter.pack(pady=25)

        # Menu
        self.bmenu = Button(self.frame_principal, text="🏠", font=("Impact", 20), bg='#2980b9', fg='white', relief=FLAT, padx=10, pady=5, bd=0)
        self.bmenu.place(x=30, y=30)

        # Boutons de la page produit
        self.bajout = Button(self.frame_produit, text="+ Ajouter", font=("Impact", 20), bg='#2980b9', fg='white', relief=FLAT)
        self.bmodifier = Button(self.frame_produit, text="✏️ Modifier", font=("Impact", 20), bg='#2980b9', fg='white', relief=FLAT)
        self.bsupprimer = Button(self.frame_produit, text="💥 Supprimer", font=("Impact", 20), bg='#2980b9', fg='white', relief=FLAT)

        # Placement des boutons de la page produit
        self.bajout.pack(pady=25)
        self.bajout.place(x=470, y=120)

        self.bmodifier.pack(pady=25)
        self.bmodifier.place(x=595, y=120)

        self.bsupprimer.pack(pady=25)
        self.bsupprimer.place(x=755, y=120)

        # Animation sur survol des boutons
        self.apply_button_hover_animation(self.bproduits)
        self.apply_button_hover_animation(self.bfournisseurs)
        self.apply_button_hover_animation(self.bventes)
        self.apply_button_hover_animation(self.brapports)
        self.apply_button_hover_animation(self.bquitter)
        self.apply_button_hover_animation(self.bajout)
        self.apply_button_hover_animation(self.bmodifier)
        self.apply_button_hover_animation(self.bsupprimer)
        self.apply_button_hover_animation(self.bmenu)

    # Fonction d'animation au survol des boutons
    def apply_button_hover_animation(self, button):
        def on_enter(event, b=button):
            if b == self.bquitter:
                b.config(bg='#c0392b')
            elif b in [self.bajout, self.bmodifier, self.bsupprimer]:
                b.config(bg='#3498db')
            elif b == self.bmenu:
                b.config(bg='#3498db')
            else:
                b.config(bg='#3498db')

        def on_leave(event, b=button):
            if b == self.bquitter:
                b.config(bg='#e74c3c')
            elif b in [self.bajout, self.bmodifier, self.bsupprimer]:
                b.config(bg='#2980b9')
            elif b == self.bmenu:
                b.config(bg='#2980b9')
            else:
                b.config(bg='#2980b9')

        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

    # Fonction pour afficher les produits
    def afficher_produits(self, produits):
        for widget in self.frame_produit.winfo_children():
            widget.destroy()

        label_title2 = Label(self.frame_produit, text="Produits", font=("Impact", 60), bg='#1e1e1e', fg='#ecf0f1')
        label_title2.pack(pady=20)

        for produit in produits:
            label_produit = Label(self.frame_produit, text=produit, font=("Courier", 20), bg='#1e1e1e', fg='#bdc3c7')
            label_produit.pack(pady=10)

    # Fonction pour définir les actions des boutons
    def set_action_buttons(self, ajout, modifier, supprimer, quitter):
        self.bajout.config(command=ajout)
        self.bmodifier.config(command=modifier)
        self.bsupprimer.config(command=supprimer)
        self.bquitter.config(command=quitter)
        self.bmenu.config(command=self.switch_to_principal)

    # Fonction pour changer de page vers produits
    def switch_to_produits(self):
        self.frame_principal.pack_forget()
        self.frame_produit.pack(expand=YES, fill=BOTH)

    # Fonction pour revenir à la page principale
    def switch_to_principal(self):
        self.frame_produit.pack_forget()
        self.frame_principal.pack(expand=YES, fill=BOTH)

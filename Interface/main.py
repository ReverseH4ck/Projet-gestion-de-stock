from tkinter import *
from tkinter import ttk
import webbrowser
from PIL import Image, ImageTk

# Options de la fenêtre principale
window = Tk()
window.title("Projet")
window.geometry("1920x1080")
window.iconbitmap("")
window.config(background='#212122')
window.minsize(480, 360)

# BOUTON MENU

frame_menu = Frame(window, bg='#212122')
frame_menu.pack(side=LEFT, anchor=N, padx=30)

# Page Produit
frame_produit = Frame(window, bg='#212122')

def openproduits():
    frame.pack_forget()
    frame_produit.pack(expand=YES, fill=BOTH)

# Contenu de la page produit
label_title2 = Label(frame_produit, text="Produits ", font=("Impact", 60), bg='#212122', fg='#c75402')
label_title2.pack(pady=20)  


# Page Principal
frame = Frame(window, bg='#212122')
frame.pack(expand=YES)

#Contenu de la page principal
# TITRE
label_title = Label(frame, text="APPLICATION", font=("Impact", 60), bg='#212122', fg='#c75402')
label_title.pack(expand=YES)

# SOUS-TITRE
label_title = Label(frame, text="Bienvenue sur l'application", font=("Courier", 20), bg='#212122', fg='white')
label_title.pack(expand=YES)

# -- BOUTONS --

# Boutons - Fonctionnalité

def quit():
    window.destroy()

# Bouton Menu - Fonctionnalité
def open_menu():
    frame_produit.pack_forget()
    frame.pack()

# Boutons - Apparence
bproduits = Button(frame, text="📦 Produits", font=("Impact", 20), bg='#c75402', fg='white', command=openproduits)
bfournisseurs = Button(frame, text="🚚 Fournisseurs", font=("Impact", 20), bg='#c75402', fg='white')
bventes = Button(frame, text="🛒 Ventes", font=("Impact", 20), bg='#c75402', fg='white')
brapports = Button(frame, text="📊 Rapports", font=("Impact", 20), bg='#c75402', fg='white')
bquitter = Button(frame, text="❌ Quitter", font=("Impact", 20), bg='#c75402', fg='white', command=quit)
bmenu = Button(frame_menu, text="🏠", font=("Impact", 20), bg='#c75402', fg='white',command=open_menu)
bajout = Button(frame_produit, text="+ Ajouter", font=("Impact", 20), bg='#c75402', fg='white',)
bmodifier = Button(frame_produit, text="✏️ Modifier", font=("Impact", 20), bg='#c75402', fg='white',)
bsupprimer = Button(frame_produit, text="💥Supprimer", font=("Impact", 20), bg='#c75402', fg='white',)

# Boutons - Affichage
bproduits.pack(pady=25, fill=X,)
bfournisseurs.pack(pady=25, fill=X)
bventes.pack(pady=25, fill=X)
brapports.pack(pady=25, fill=X)
bquitter.pack(pady=25, fill=X)
bmenu.pack(pady=25,)

# Boutons - Affichage (Fenêtre Produits) 
bajout.pack(pady=25,)
bajout.place(x=470,y=120)

bmodifier.pack(pady=25,)
bmodifier.place(x=595,y=120)

bsupprimer.pack(pady=25,)
bsupprimer.place(x=755,y=120)

# Fonctions de survol des boutons
def entree(event):
    event.widget['background'] = '#9e4202'  
    event.widget['foreground'] = '#95ff00'   
    event.widget.config(cursor="hand2")


def sortie(event):
    event.widget['background'] = '#c75402'  
    event.widget['foreground'] = 'white'  
    event.widget.config(cursor="")  

# Utilisations de nos fonctions survols pour nos boutons 
for button in [bproduits, bfournisseurs, bventes, brapports, bquitter, bajout,bmodifier,bsupprimer,bmenu]:
    button.bind("<Enter>", entree)
    button.bind("<Leave>", sortie)

# Afficher la fenêtre
window.mainloop()
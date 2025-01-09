from tkinter import *
from tkinter import ttk
import webbrowser
from PIL import Image, ImageTk

# Options de la fenêtre principale
window = Tk()
window.title("Projet")
window.geometry("1920x1080")
window.iconbitmap("Interface/ressources/logo.ico")
window.config(background='#212122')
window.minsize(480, 360)

# Frame Produit
frame_produit = Frame(window, bg='#212122')

def openproduits():
    frame.pack_forget()
    frame_produit.pack(expand=YES, fill=BOTH)

# Contenu du frame produits
label_title2 = Label(frame_produit, text="Produits ", font=("Impact", 60), bg='#212122', fg='#c75402')
label_title2.pack(pady=20)  


#Frame Menu
frame = Frame(window, bg='#212122')
# Ajout de texte 
label_title = Label(frame, text="APPLICATION", font=("Impact", 60), bg='#212122', fg='#c75402')
label_title.pack(expand=YES)

# Afficher le frame 
frame.pack(expand=YES)

label_title = Label(frame, text="Bienvenue sur l'application", font=("Courier", 20), bg='#212122', fg='white')

label_title.pack(expand=YES)

# Boutons - Quitter
def quit():
    window.destroy()


# Boutons - Apparence
bproduits = Button(frame, text="📦 Produits", font=("Impact", 40), bg='#c75402', fg='white', command=openproduits)
bfournisseurs = Button(frame, text="🚚 Fournisseurs", font=("Impact", 40), bg='#c75402', fg='white')
bventes = Button(frame, text="🛒 Ventes", font=("Impact", 40), bg='#c75402', fg='white')
brapports = Button(frame, text="📊 Rapports", font=("Impact", 40), bg='#c75402', fg='white')
bquitter = Button(frame, text="❌ Quitter", font=("Impact", 40), bg='#c75402', fg='white', command=quit)


# Boutons - Affichage 
bproduits.pack(pady=25, fill=X)
bfournisseurs.pack(pady=25, fill=X)
bventes.pack(pady=25, fill=X)
brapports.pack(pady=25, fill=X)
bquitter.pack(pady=25, fill=X)


# Afficher la fenêtre
window.mainloop()
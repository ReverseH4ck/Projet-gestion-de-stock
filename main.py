from tkinter import *
from tkinter import ttk
import webbrowser
from PIL import Image, ImageTk

# Options de la fenêtre principale
window = Tk()
window.title("Projet")
window.geometry("1920x1080")
window.iconbitmap("logo.ico")
window.config(background='#212122')



# Limiter l'utilisateur à la réduction de taille de la fenêtre
window.minsize(480, 360)

#Création d'un frame(conteneur)
frame = Frame(window, bg='#212122')
# Ajout de texte 
label_title = Label(frame, text="APPLICATION", font=("Impact", 60), bg='#212122', fg='#c75402')
label_title.pack(expand=YES)

# Afficher le frame 
frame.pack(expand=YES)

label_title = Label(frame, text="Bienvenue sur l'application", font=("Courier", 20), bg='#212122', fg='white')

label_title.pack(expand=YES)

# Boutons - Fonctionnalité
def open_github():
    webbrowser.open_new("https://github.com/ReverseH4ck/Projet-gestion-de-stock")

def quit():
    window.destroy()


# Boutons - Apparence
bproduits = Button(frame, text="📦 Produits", font=("Impact", 40), bg='#c75402', fg='white')
bfournisseurs = Button(frame, text="🚚 Fournisseurs", font=("Impact", 40), bg='#c75402', fg='white')
bventes = Button(frame, text="🛒 Ventes", font=("Impact", 40), bg='#c75402', fg='white')
brapports = Button(frame, text="📊 Rapports", font=("Impact", 40), bg='#c75402', fg='white')
bquitter = Button(frame, text="❌ Quitter", font=("Impact", 40), bg='#c75402', fg='white', command=quit)
bgithub = Button(frame, text="🔗 Github", font=("Impact", 40), bg='#c75402', fg='white', command=open_github)


# Boutons - Affichage 
bproduits.pack(pady=25, fill=X)
bfournisseurs.pack(pady=25, fill=X)
bventes.pack(pady=25, fill=X)
brapports.pack(pady=25, fill=X)
bgithub.pack(pady=25, fill=X)
bquitter.pack(pady=25, fill=X)


# Afficher la fenêtre
window.mainloop()
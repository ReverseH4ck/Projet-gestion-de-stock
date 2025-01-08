from tkinter import *
from tkinter import ttk

# Options de la fenêtre principale
window = Tk()
window.title("Projet")
window.geometry("1920x1080")
window.iconbitmap("logo.ico")
window.config(background='#044e80')
# Limiter l'utilisateur à la réduction de taille de la fenêtre
window.minsize(480, 360)

label_title = Label(window, text="Bienvenue sur l'application", font=("Arial", 40), bg='#044e80', fg='white')
label_title.pack()








# Afficher la fenêtre
window.mainloop()
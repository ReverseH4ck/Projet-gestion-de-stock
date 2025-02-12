from tkinter import Tk
from model import Model
from view import View
from controller import Controller

def main():
    window = Tk()
    model = Model()
    view = View(window)
    controller = Controller(model, view)
    window.mainloop()

if __name__ == "__main__":
    main()

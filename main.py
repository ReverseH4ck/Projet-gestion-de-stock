from interface.model import Model
from interface.view import View
from interface.controller import Controller
from tkinter import Tk

def main():
    window = Tk()
    model = Model()
    view = View(window)
    controller = Controller(model, view)
    view.set_controller(controller)  # ← C’est ici que ça lie la view au controller
    window.mainloop()

if __name__ == "__main__":
    main()
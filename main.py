import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from tkinter import Tk
from interface.model import Model
from interface.view import View
from interface.controller import Controller



def main():
    window = Tk()
    model = Model()
    view = View(window)
    controller = Controller(model, view)
    window.mainloop()

if __name__ == "__main__":
    main()

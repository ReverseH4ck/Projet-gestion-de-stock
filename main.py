import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from tkinter import Tk
from Interface.model import Model
from Interface.view import View
from Interface.controller import Controller






def main():
    window = Tk()
    model = Model()
    view = View(window)
    controller = Controller(model, view)
    window.mainloop()

if __name__ == "__main__":
    main()

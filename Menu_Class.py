from tkinter import *

# Class to config the menu


class show_window():
    def __init__(self,option="Menu"):
        root = Tk()
        app = Window(root)
        if option == "Menu":
            app.init_menu()
        root.mainloop()


# Main Window class with visual settings


class Window(Frame):

    def __init__(self, master= None ):
        Frame.__init__(self, master)
        self.master = master

    def init_menu(self):
        self.master.title("Menu")


show_window()






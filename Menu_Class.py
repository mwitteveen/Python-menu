from tkinter import *
import os
from PIL import ImageTk, Image

# @desc: Class to config the menu
# @param: Choice of window options (string)
class show_window():
    def __init__(self,sOption="Menu"):
        root = Tk()
        app = Window(root)
        if sOption == "Menu":
            app.init_menu()
        elif sOption=="Input":
            app.init_input()

        root.mainloop()


# @desc: Main Window class with visual settings
# @param: frame object from tk (TK object)
# @param: master frame for editing existing frames (TK object)
class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.master.resizable(width=False, height=False)

    # @desc: initialise menu
    # @param: give function name that gets activated by clicking start
    def init_menu(self, start=None):

        # Set size
        self.master.geometry("600x400")
        self.master.wm_attributes('-transparentcolor',self.master['bg'])
        self.master.configure(background='snow')

        # Change Title of master widget
        self.master.title("Menu")

        # allowing widget to take full space of root window
        self.pack(fill=BOTH, expand=1)

        # create menu bar
        self.init_menu_bar()

        # create grid
        rows = 0
        while rows < 50:
            self.master.rowconfigure(rows, weight=1)
            self.master.columnconfigure(rows, weight=1)
            rows += 1

        # Setting background image
        img = Image.open(str(os.getcwd()) + "\\Config images\\Shared logo.gif")
        img = img.resize((470, 120),Image.ANTIALIAS).convert("RGBA")
        bg_img = Image.open((str(os.getcwd()) + "\\Config images\\bg_menu.gif"))
        bg_img.paste(img, (230, 220), img)

        background_image = ImageTk.PhotoImage(bg_img)
        background_label = Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # creating quit button
        quitButton = Button(self, text="Quit", command=self.client_exit,height=2, width=15, bg="white")
        quitButton.place(x=20,y=340)

        # creating start button
        startButton = Button(self, text="Start", command=start, height=2, width=15, bg="white")
        startButton.place(x=470, y=340)

    # @desc: initialise menu bar
    def init_menu_bar(self):

        # create bar
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create menu for in the bar
        file = Menu(menu, tearoff=False)
        file.add_command(label="Exit", command=self.client_exit)

        # add menu to the bar
        menu.add_cascade(label="File", menu=file)

        # create menu for the bar
        info = Menu(menu, tearoff=False)
        info.add_command(label="Contact", command=self.show_Contact)
        info.add_command(label="About", command=self.show_About)

        # add menu to bar
        menu.add_cascade(label="Info", menu= info)

    def show_About(self):
        frame = Window(Toplevel())
        frame.init_About()

    def show_Contact(self):
        frame = Window(Toplevel())
        frame.init_Contact()

    def init_About(self):

        self.master.title("About")
        self.init_menu_bar()
        self.master.geometry("500x300")

        # logo = Image.open((str(os.getcwd()) + "\\Config images\\Shared logo.gif"))
        # logo = logo.resize((400, 120), Image.ANTIALIAS).convert("RGBA")
        # logo = ImageTk.PhotoImage(logo)
        # logo_Label = Label(self.master, image=logo)
        # logo_Label.image = logo
        # logo_Label.place(x=0,y=0)

        canvas = Canvas(self.master, bg="snow", width=500, height=300)
        canvas.pack()

        img = ImageTk.PhotoImage(file=(str(os.getcwd()) + "\\About info\\Logo.png"))
        canvas.create_image(0, 0, image=img)



    def init_Contact(self):

        self.master.title("Contact")
        self.init_menu_bar()
        self.master.geometry("500x300")

    def client_exit(self):
        exit()

show_window()






from tkinter import *
from PIL import Image, ImageTk

class Window(Frame):

    #Constructor
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("GUI")
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        file.add_cascade(label="File", menu=file)
        edit = Menu(menu)
        edit.add_command(label='Undo')
        menu.add_cascade(label='Edit', menu=edit)

    def showImg(self):
        load = Image.open("icon.png")
        render = ImageTk.PhotoImage(load)
        #labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
    
    def showText(self):
        text = Label(self, text='Blistering Barnacles!')
        text.pack()

    #event handling
    def client_exit(self):
        exit()

root = Tk()
root.geometry("400x300")
app = Window(root)
#Infinite loop
root.mainloop()

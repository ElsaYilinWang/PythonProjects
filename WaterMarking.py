from tkinter import *
from tkinter import ttk
from PIL import *


class WaterMarking:
    def __init__(self, root):
        # set up the main application window and title
        root = Tk()
        root.title("WaterMarking!")

        # create a frame widget to hold UI contents
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.label = Label(root, text="Upload an Image")
        self.label.pack(pady=10)

        self.upload_button = Button(root, text="Upload", command=self.upload)
        self.upload_button.pack(pady=10)

        self.watermark_button = Button(root, text="Add Watermark", command=self.add_watermark)
        self.watermark_button.pack(pady=10)

    def upload(self):
        # start the event loop
        # root.mainloop()
        pass

    def add_watermark(self):
        #
        pass


root = Tk()
WaterMarking(root)
root.mainloop()

import os
import source.visualization.main_CTkWindow as mainCTk
import source.xml as mainXML
import customtkinter as CTkinter
from PIL import Image, ImageTk

class App(CTkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("EXAM REPORT RESULT COMPARATOR")
        self.geometry("1500x800")

        # set grid layout
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=2)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
    
        # load images with light and dark mode image
        self.image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'source', 'visualization', 'icons')
        self.icon = Image.open(os.path.join(self.image_path, 'comparison_512x512.png'))

        # set windows icon next to the title
        icon_image = ImageTk.PhotoImage(self.icon.convert("RGBA"))
        self.iconphoto(True, icon_image)
        self.iconbitmap(os.path.join(self.image_path, 'comparison_48x48.ico')) # TO CHECK ON WINDOWS TO HAVE ICON VISIBLE AS ICO OR PNG

        # add widgets to app
        self.Frame2 = mainCTk.ReportSelectionFrame(master=self)
        self.Frame2.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky='nesw')
        self.Frame1 = mainCTk.OptionFrame(self, self.Frame2)
        self.Frame1.grid(row=0, rowspan=2, column=0, padx=10, pady=10, sticky='nsw')
        self.Frame3 = mainCTk.MetadataFrame(master=self)
        self.Frame3.grid(row=1, column=1, padx=10, pady=10, sticky='nesw')
        self.Frame3 = mainCTk.DetailsFrame(master=self)
        self.Frame3.grid(row=1, column=2, padx=10, pady=10, sticky='nesw')
        
        self.mainloop()

        return

app = App()
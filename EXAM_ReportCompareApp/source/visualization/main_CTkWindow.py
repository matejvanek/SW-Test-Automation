import os
import customtkinter as CTkinter
from PIL import Image, ImageTk

# Global variables
directory = '' # selected directory by user
reportResultFilter = {} # to get a value of switches
testsTypeFilter = {} # to get a value of switches

class ReportFilterFrame(CTkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        global reportResultFilter

        # set grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)

        self.Label = CTkinter.CTkLabel(master=self, text='Report Filter', fg_color='gray', corner_radius=5)
        self.Label.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

        resultList = ['ERROR', 'FAILED', 'PASSED', 'OPEN', 'INFO']
        for i, result in enumerate(resultList):
            switch_var = CTkinter.BooleanVar(value=True)
            reportResultFilter[result] = switch_var

            self.widget = CTkinter.CTkSwitch(master=self, text=result, variable=switch_var, onvalue=True, offvalue=False)
            #self.widget.select(True) # set switch to requested value
            self.widget.grid(row=i+1, column=0, padx=0, pady=0, sticky='ew')
        
        return

class TestsFilterFrame(CTkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # set grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)

        self.Label = CTkinter.CTkLabel(master=self, text='Tests Filter', fg_color='gray', corner_radius=5)
        self.Label.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

        testsList = ['TEST GROUP', 'ADMIN CASE', 'TESTCASE', 'SUB-TEST', 'ERROR', 'FAILED', 'PASSED', 'OPEN', 'INFO']
        for i, type in enumerate(testsList):
            switch_var = CTkinter.BooleanVar(value=True)
            testsTypeFilter[type] = switch_var

            self.widget = CTkinter.CTkSwitch(master=self, text=type, variable=switch_var, onvalue=True, offvalue=False)
            #self.widget.select(True) # set switch to requested value
            self.widget.grid(row=i+1, column=0, padx=0, pady=0, sticky='ew')

class OptionFrame(CTkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        def browse_directory():
            global directory

            directory = CTkinter.filedialog.askdirectory()
            if directory:
                entry_directory.delete(0, CTkinter.END)  # Clear any existing text
                entry_directory.configure(True, border_color=original_border_color)
                entry_directory.insert(0, directory)  # Insert the selected directory path

            return
        
        def on_enter(event):
            global directory

            user_input = entry_directory.get()
            if(os.path.exists(user_input)):
                entry_directory.configure(True, border_color=original_border_color)
                directory = user_input
            else:
                entry_directory.configure(True, border_color='red')
                
            return

        def show_about():

            return
        
        def appearance_mode(mode):
            CTkinter.set_appearance_mode(mode)

            return

        # set grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        entry_directory = CTkinter.CTkEntry(master=self, placeholder_text='Select a directory or enter path', textvariable=directory, width=200, justify='left', state='normal')
        button_browse = CTkinter.CTkButton(master=self, text='🔍', width=50, command=browse_directory)
        self.Frame_ReportFilter = ReportFilterFrame(master=self, fg_color='transparent')
        self.Frame_TestsFilter = TestsFilterFrame(master=self, fg_color='transparent')
        button_about = CTkinter.CTkButton(master=self, text='ABOUT', command=show_about)
        theme_comboBox = CTkinter.CTkComboBox(master=self, values=['system', 'dark', 'light'], justify='center', state='normal', command=appearance_mode)

        elementsList = [[entry_directory, button_browse], self.Frame_ReportFilter, self.Frame_TestsFilter, button_about, theme_comboBox]
        for i, input in enumerate(elementsList):
            if(isinstance(input, list)):
                for j, widget in enumerate(input):
                    widget.grid(row=i, column=j, padx=5, pady=5, sticky='nesw')
            else:
                input.grid(row=i, column=0, columnspan=2, padx=5, pady=5, sticky='nesw')
            

        # Bind the Enter key to the on_enter function
        original_border_color = entry_directory.cget("border_color")
        entry_directory.bind("<Return>", on_enter)

        return
    
class ReportSelectionFrame(CTkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # set grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        return

class MetadataFrame(CTkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # set grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        return

class DetailsFrame(CTkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # set grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        return

class App(CTkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("EXAM REPORT RESULT COMPARATOR")
        self.geometry("1500x800")

        # set grid layout
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
    
        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'icons')
        icon = Image.open(os.path.join(image_path, 'comparison_512x512.png'))

        # set windows icon next to the title
        icon_image = ImageTk.PhotoImage(icon.convert("RGBA"))
        self.iconphoto(True, icon_image)
        self.iconbitmap(os.path.join(image_path, 'comparison_48x48.ico')) # TO CHECK ON WINDOWS TO HAVE ICON VISIBLE AS ICO OR PNG

        # add widgets to app
        self.Frame1 = OptionFrame(master=self)
        self.Frame1.grid(row=0, rowspan=2, column=0, padx=10, pady=10, sticky='nsw')
        self.Frame2 = ReportSelectionFrame(master=self)
        self.Frame2.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky='nesw')
        self.Frame3 = MetadataFrame(master=self)
        self.Frame3.grid(row=1, column=1, padx=10, pady=10, sticky='nesw')
        self.Frame3 = DetailsFrame(master=self)
        self.Frame3.grid(row=1, column=2, padx=10, pady=10, sticky='nesw')
        
        return

app = App()
app.mainloop()
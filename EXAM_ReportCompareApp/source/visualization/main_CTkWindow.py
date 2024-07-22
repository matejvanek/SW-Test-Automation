import os
from datetime import datetime
import tkinter as tk
import source.visualization.widgets.CTkTreeview as CTkTreeview
import source.xml.xml_parser as xml_parser
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
    def __init__(self, master, treeview_frame, **kwargs):
        super().__init__(master, **kwargs)
        self.treeview_frame = treeview_frame
        
        def browse_directory():
            global directory

            directory = CTkinter.filedialog.askdirectory()
            if directory:
                entry_directory.delete(0, CTkinter.END)  # Clear any existing text
                entry_directory.configure(True, border_color=original_border_color)
                entry_directory.insert(0, directory)  # Insert the selected directory path
                ReportSelectionFrame.update_report_tree(self.treeview_frame)

            return
        
        def on_enter(event):
            global directory

            user_input = entry_directory.get()
            if(os.path.exists(user_input)):
                entry_directory.configure(True, border_color=original_border_color)
                directory = user_input
                ReportSelectionFrame.update_report_tree(self.treeview_frame)
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

        columns_definition = ('Name', 'Path', 'Date', 'Result', 'Test Suite')
        self.Reporttree = CTkTreeview.CTkTreeview(self, columns=columns_definition, show='tree headings') 
        self.Reporttree.pack(expand=True, fill='both')
        
        # columns definition
        self.Reporttree["columns"] = columns_definition
        self.Reporttree.column("#0", width=50, minwidth=35, stretch=tk.NO, anchor='center')
        for column in columns_definition:
            self.Reporttree.column(column, width=200, minwidth=100, stretch=tk.YES, anchor='w')

        # headings definition
        self.Reporttree.heading("#0", text='', anchor='center')
        for heading in columns_definition:
            self.Reporttree.heading(heading, text=heading, anchor='w')

        return

    def fill_with_report_data(self, matching_files):
        # icons directory
        self.image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'icons')
        # load images
        self.icon = Image.open(os.path.join(self.image_path, 'python-icon_256x256.png'))
        self.icon = self.icon.resize((24,24), 0) # Use Image.Resampling.NEAREST (0), Image.Resampling.LANCZOS (1), Image.Resampling.BILINEAR (2), Image.Resampling.BICUBIC (3), Image.Resampling.BOX (4) or Image.Resampling.HAMMING (5)

        # set windows icon next to the title
        self.icon_image = ImageTk.PhotoImage(self.icon.convert("RGBA"))

        for file in matching_files:
            path, name = os.path.split(file)

            self.Reporttree.insert('', "end", image=self.icon_image, values=(name, path, datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y-%m-%d %H:%M:%S'), self.icon_image, "none", "none"))

        return

    def update_report_tree(self):
        # Load the reports into the tree view
        #self.load_reports("path_to_your_directory")
        # Add data to the treeview
        if(directory):
            self.Reporttree.delete(*self.Reporttree.get_children())
            matching_files = []
            for root, dirs, files in os.walk(directory):
                # Get the name of the current directory
                parent_folder_name = os.path.basename(root)
                for file in files:
                    # Check if the file is an XML and has the same name as the parent folder
                    if file == parent_folder_name + ".xml":
                        # Get the full absolute path
                        full_path = os.path.join(root, file)
                        matching_files.append(full_path)

            ReportSelectionFrame.fill_with_report_data(self, matching_files)

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
import tkinter as tk
from tkinter import ttk
import customtkinter as CTkinter

class CTkTreeview(ttk.Treeview):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        #self.custom_style()

        return

    def custom_style(self):
        self.tree = ttk.Treeview(self)
        self.tree.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, ipadx=20, ipady=20)

        # Add a vertical scrollbar
        self.scrollbar = CTkinter.CTkScrollbar(self, orientation="vertical", command=self.tree.yview, fg_color='transparent', button_color=("gray55", "gray41"), button_hover_color=("gray40", "gray53"))
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.configure(yscrollcommand=self.scrollbar.set)

        ###Treeview Customisation (theme colors are selected)
        bg_color = ["gray86", "gray17"]# CTkinter.CTkFrame._apply_appearance_mode(CTkinter, CTkinter.ThemeManager.theme["CTkFrame"]["fg_color"])
        text_color = ["gray10", "#DCE4EE"] # CTkinter.CTkFrame._apply_appearance_mode(CTkinter, CTkinter.ThemeManager.theme["CTkLabel"]["text_color"])
        selected_color = ["#3B8ED0", "#1F6AA5"] # CTkinter.CTkFrame._apply_appearance_mode(CTkinter, CTkinter.ThemeManager.theme["CTkButton"]["fg_color"])
        scrollbar_fg_color = None
        scrollbar_button_color = None
        scrollbar_button_hover_color = None

        treestyle = ttk.Style()
        treestyle.theme_use('default')
        treestyle.configure("Treeview", background=bg_color, foreground=text_color, fieldbackground=bg_color, borderwidth=0)
        treestyle.configure("Treeview.Heading", background=("gray55", "gray41"), foreground=text_color, fieldbackground=("gray55", "gray41"), borderwidth=0)
        treestyle.map('Treeview', background=[('selected', bg_color)], foreground=[('selected', selected_color)])
        self.bind("<<TreeviewSelect>>", lambda event: self.focus_set())

        return
    
'''
##Treeview widget data
        self.tree.insert('', '0', 'i1', text ='Python')
        self.tree.insert('', '1', 'i2', text ='Customtkinter')
        self.tree.insert('', '2', 'i3', text ='Tkinter')
        self.tree.insert('i2', 'end', 'Frame', text ='Frame')
        self.tree.insert('i2', 'end', 'Label', text ='Label')
        self.tree.insert('i3', 'end', 'Treeview', text ='Treeview')
        self.tree.move('i2', 'i1', 'end')
        self.tree.move('i3', 'i1', 'end')
        self.tree.insert('', '3', 'i4', text ='Python')
        self.tree.insert('', '4', 'i5', text ='Customtkinter')
        self.tree.insert('', '5', 'i6', text ='Tkinter')
        self.tree.insert('', '6', 'i7', text ='Python')
        self.tree.insert('', '7', 'i8', text ='Customtkinter')
        self.tree.insert('', '8', 'i9', text ='Tkinter')
        self.tree.insert('', '9', 'i10', text ='Python')
        self.tree.insert('', '10', 'i11', text ='Customtkinter')
        self.tree.insert('', '11', 'i12', text ='Tkinter')
        self.tree.insert('', '12', 'i13', text ='Python')
        self.tree.insert('', '13', 'i14', text ='Customtkinter')
        self.tree.insert('', '14', 'i15', text ='Tkinter')



class CustomTreeview(ttk.Treeview):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.custom_style()
        self._sort_column = None

    def custom_style(self):
        style = ttk.Style()
        # Example custom style configuration
        style.configure("Custom.Treeview",
                        background="lightblue",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="lightgrey")
        style.map("Custom.Treeview",
                  background=[("selected", "blue")],
                  foreground=[("selected", "white")])
        self.configure(style="Custom.Treeview")

    def heading(self, column, **kwargs):
        # Add sorting functionality
        if "command" not in kwargs:
            kwargs["command"] = lambda c=column: self.sort_column(c, False)
        super().heading(column, **kwargs)

    def sort_column(self, column, reverse):
        l = [(self.set(k, column), k) for k in self.get_children('')]
        l.sort(reverse=reverse)

        # Rearrange items in sorted positions
        for index, (val, k) in enumerate(l):
            self.move(k, '', index)

        # Reverse sort next time
        self.heading(column, command=lambda: self.sort_column(column, not reverse))

'''
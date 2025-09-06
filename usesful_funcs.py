import tkinter as tk
from tkinter.ttk import Combobox

def clear_widgets(widgets:list):
    for widget in widgets:
        if isinstance(widget, tk.Entry): widget.delete(0, tk.END)
        if isinstance(widget, Combobox): widget.current(0)
        elif isinstance(widget, tk.Label): widget.config(text=' ')

def disable_widgets(widgets:list):
    for widget in widgets:
        widget.config(state='disabled')

def enable_widgets(widgets:list):
    for widget in widgets:
        if isinstance(widget, Combobox): widget.config(state='readonly') #para que no escriban en el combo
        else: widget.config(state='normal')

def return_main(mainroot, principal_frame): mainroot.change_frame(principal_frame)
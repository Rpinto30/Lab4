import tkinter as tk
from tkinter.ttk import Combobox


def pack_create_line(master:tk.Frame, left_widget, right_widget, _padx=0, _pady=0, width=0,height=0):
    row = tk.Frame(master,bg='green', width=width+5, height=height)
    left_widget.pack(in_=row, side='left', anchor='center', padx=_padx)
    right_widget.pack(in_=row, side='right', anchor='center', padx=_padx)
    row.pack_propagate(False)
    row.pack(pady=_pady)
    return row


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
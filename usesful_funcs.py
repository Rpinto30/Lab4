import tkinter as tk
from tkinter.ttk import Combobox

def pack_create_line(master:tk.Frame, left_widget, right_widget, _padx=0, _pady=0, width=0,height=0, bg='#f0f0f0'):
    row = tk.Frame(master, width=width+5, height=height, bg=bg)
    left_widget.pack(in_=row, side='left', padx=_padx, anchor='w')
    right_widget.pack(in_=row, side='right', padx=_padx, anchor='e')

    if width != 0 and height != 0: row.pack_propagate(False)
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

class Tabla: #tabla es inspirada de imagen de Google
    def __init__(self, master, total_rows, total_columns, lst_, ancho = 11, alto=14, border_width=2):
        self.__table = []
        for i in range(total_rows):
            row = []
            for j in range(total_columns):
                e = tk.Entry(master, width=ancho, fg='black', font = ("Arial", alto), borderwidth=border_width, relief="solid")
                if i == 0: e.config(readonlybackground='#A9B1D1')
                else: e.config(readonlybackground='#D5D9E8')
                e.grid(row=i, column=j)
                e.insert(tk.END, lst_[i][j])
                e.config(state='readonly')
                row.append(e)
            self.__table.append(row)

    def confi_colum(self, index, width_=1):
        for fila in self.__table:
            if index < len(fila):
                fila[index].config(width=width_)

    def destroy_table(self):
        for fila in self.__table:
            for cell in fila:
                cell.destroy()
        self.__table.clear()
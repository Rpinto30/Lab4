from usesful_funcs import *
from tkinter.ttk import Combobox

def rate_form(mainroot, rate_frame, main_frame):
    mainroot.change_frame(rate_frame)
    f_combo_select = tk.Frame(rate_frame, width=500, height=75)
    f_combo_select.pack_propagate(False)
    f_combo_select.pack(anchor='center', fill='x')

    bands = [band for band in mainroot.concurso.bandas.values()]
    l_header = tk.Label(f_combo_select, text= 'Calificar Banda', font=('Arial',20))
    l_header.pack()
    c_list_bands = Combobox(f_combo_select, state='readonly',values=[b.nombre for b in bands], width=30, font=('Arial', 15))
    c_list_bands.pack(expand=True, anchor="center")


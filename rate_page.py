from usesful_funcs import *
from tkinter.ttk import Combobox

def rate_form(mainroot, rate_frame, main_frame):
    mainroot.change_frame(rate_frame)
    f_combo_select = tk.Frame(rate_frame, width=500, height=100)
    f_combo_select.pack_propagate(False)
    f_combo_select.pack()

    c_list_bands = Combobox(f_combo_select, state='readonly',values=['a','b'])
    c_list_bands.pack()
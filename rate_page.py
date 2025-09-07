from usesful_funcs import *
from tkinter.ttk import Combobox, Scale
from tkinter.ttk import Scale

def rate_form(mainroot, rate_frame, main_frame):
    mainroot.change_frame(rate_frame)
    f_combo_select = tk.Frame(rate_frame, height=75)
    f_combo_select.pack_propagate(False)
    f_combo_select.pack(anchor='center', fill='x')

    bands = [band for band in mainroot.concurso.bandas.values()]
    l_header = tk.Label(f_combo_select, text= 'Calificar Banda', font=('Arial',20))
    l_header.pack()
    c_list_bands = Combobox(f_combo_select, state='readonly',values=[b.nombre for b in bands], width=30, font=('Arial', 15))
    c_list_bands.pack(expand=True, anchor="center")

    def pack_rate_forms(event):
        c_list_bands.config(state='disable')
        f_rate = tk.Frame(rate_frame, width=750, height=425)
        f_rate.pack_propagate(False)
        f_rate.pack(anchor='n', expand=1)

        l_header_rate = tk.Label(f_rate, text= f'Califica a {c_list_bands.get()} según cada criterio', font=('Arial',12))
        l_header_rate.pack(pady=15)
        #LABELS
        font_labels = ('Arial', 15, 'bold')
        l_ritmo = tk.Label(text='Ritmo', font=font_labels)
        l_uniformidad = tk.Label(text='Uniformidad', font=font_labels)
        l_coreografia = tk.Label(text='Coreografia', font=font_labels)
        l_alineacion = tk.Label(text='Alineacion', font=font_labels)
        l_puntualidad = tk.Label(text='Puntualidad', font=font_labels)
        #https://python--course-eu.translate.goog/tkinter/sliders-in-tkinter.php?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc
        a = Scale(f_rate,from_=1, to=10, orient='horizontal')
        a.pack()
        #pack_create_line()
    pack_rate_forms(None)
    #https://python-course.eu/tkinter/events-and-binds-in-tkinter.php
    c_list_bands.bind("<<ComboboxSelected>>", lambda event: pack_rate_forms(event))

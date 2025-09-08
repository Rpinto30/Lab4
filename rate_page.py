from usesful_funcs import *
from tkinter.ttk import Combobox
from tkinter import PhotoImage
from tkinter import messagebox

from save_data import save_data

def rate_form(mainroot, rate_frame, main_frame):
    mainroot.change_frame(rate_frame)
    BG_COMBO_SELECT = '#7E90CC'
    f_combo_select = tk.Frame(rate_frame, height=160, bg=BG_COMBO_SELECT)
    f_combo_select.pack_propagate(False)
    f_combo_select.pack(anchor='center', fill='x')

    photo = PhotoImage(file=r'imagenes/prueba_rate.gif', width=370, height=480)
    l_photo = tk.Label(rate_frame, image=photo)
    l_photo.image = photo
    l_photo.pack()

    bands = [band for band in mainroot.concurso.bandas.values()]
    l_header = tk.Label(f_combo_select, text= 'Calificar Banda', font=('Arial',30), bg=BG_COMBO_SELECT)
    l_header.pack()

    l_select_info = tk.Label(f_combo_select, text= 'Selecciona una banda previamente registrada', font=('Arial',12), bg=BG_COMBO_SELECT)
    l_select_info.pack()

    c_list_bands = Combobox(f_combo_select, state='readonly',values=[b.nombre for b in bands], width=30, font=('Arial', 15))
    c_list_bands.pack(expand=True, anchor="center")

    b_cancel_header = tk.Button(f_combo_select, text='Salir', width=10, font=('Arial', 10), command=lambda:return_main(mainroot, main_frame),
                                bg=B_COLOR_CANCEL, activebackground=B_COLOR_CANCEL_SEL, fg=B_BUTTON_TEXT)
    b_cancel_header.pack(pady=5)

    def pack_rate_forms(is_new):
        c_list_bands.config(state='disabled')
        l_photo.pack_forget()
        l_select_info.pack_forget()
        b_cancel_header.pack_forget()
        f_combo_select.config(height=75)

        f_rate = tk.Frame(rate_frame, width=750, height=320)
        f_rate.pack_propagate(False)
        f_rate.pack(anchor='n', expand=1)

        f_acept = tk.Frame(rate_frame, width=750, height=105, bg='#CAD6E0')
        f_acept.pack_propagate(False)
        f_acept.pack(anchor='s', expand=1)

        l_info_rate = tk.Label(f_rate, text= f'Califica a {c_list_bands.get()} según cada criterio', font=('Arial',12))
        l_info_rate.pack(pady=5)
        #LABELS
        font_labels = ('Arial', 16, 'bold')
        l_ritmo = tk.Label(text='Ritmo', font=font_labels)
        l_uniformidad = tk.Label(text='Uniformidad', font=font_labels)
        l_coreografia = tk.Label(text='Coreografia', font=font_labels)
        l_alineacion = tk.Label(text='Alineacion', font=font_labels)
        l_puntualidad = tk.Label(text='Puntualidad', font=font_labels)

        #https://python--course-eu.translate.goog/tkinter/sliders-in-tkinter.php?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc
        s_ritmo = tk.Scale(from_=0, to=10, orient='horizontal', length=300, width=10)
        s_uniformidad = tk.Scale(from_=0, to=10, orient='horizontal', length=300, width=10)
        s_coreografia = tk.Scale(from_=0, to=10, orient='horizontal', length=300, width=10)
        s_alineacion = tk.Scale(from_=0, to=10, orient='horizontal', length=300, width=10)
        s_puntualidad = tk.Scale(from_=0, to=10, orient='horizontal', length=300, width=10)
        scalers = [s_ritmo, s_uniformidad, s_coreografia, s_alineacion, s_puntualidad]
        #PACK
        pack_create_line(f_rate, l_ritmo, s_ritmo, _pady=10, width=500, height=35)
        pack_create_line(f_rate, l_uniformidad, s_uniformidad, _pady=10, width=500, height=35)
        pack_create_line(f_rate, l_coreografia, s_coreografia,_pady=10, width=500, height=35)
        pack_create_line(f_rate, l_alineacion, s_alineacion,_pady=10, width=500, height=35)
        pack_create_line(f_rate, l_puntualidad, s_puntualidad,_pady=10, width=500, height=35)

        #BOTONES
        b_acept = tk.Button(f_acept,text='Aceptar', width=10, font=('Arial',14))
        b_mod = tk.Button(f_acept,text='Cambiar Banda', width=15, font=('Arial',14))
        b_cancel = tk.Button(f_acept,text='Salir', width=10, font=('Arial',14))

        def exit_frame():
            m_end = messagebox.showinfo("Guardado de datos",
                                        f'Se ha guardado correctamente el puntaje de {c_list_bands.get()}')
            return_main(mainroot, main_frame)

        def cancel():
            if b_cancel.cget('text') == 'Salir':
                b_mod.config(state='disabled')
                for sc in scalers:sc.config(state='disabled')
                l_info_rate.config(text='¿Estas seguro que deseas salir?')
                b_cancel.config(text='No')
                b_acept.config(text='Sí')
            else:
                for sc in scalers: sc.config(state='normal')
                l_info_rate.config(text=f'Califica a {c_list_bands.get()} según cada criterio')
                b_mod.config(state='normal')
                b_cancel.config(text='Salir')
                b_acept.config(text='Aceptar')

        def acept():
            if b_acept.cget('text') == 'Aceptar':
                for band in bands:
                    if band.nombre == str(c_list_bands.get()):
                        b_acept.config(state='disabled')
                        b_mod.config(state='disabled')
                        b_cancel.config(state='disabled')
                        for sc in scalers: sc.config(state='disabled')
                        l_info_rate.config(text='GUARDANDO...')

                        mainroot.concurso.bandas[band.codigo].registrar_puntajes(int(s_ritmo.get()),'ritmo')
                        mainroot.concurso.bandas[band.codigo].registrar_puntajes(int(s_uniformidad.get()),'uniformidad')
                        mainroot.concurso.bandas[band.codigo].registrar_puntajes(int(s_coreografia.get()),'coreografia')
                        mainroot.concurso.bandas[band.codigo].registrar_puntajes(int(s_alineacion.get()),'alineacion')
                        mainroot.concurso.bandas[band.codigo].registrar_puntajes(int(s_puntualidad.get()),'puntualidad')
                        mainroot.concurso.bandas[band.codigo].suma_total()
                        break
                save_data(mainroot.concurso.bandas)
                mainroot.after(ms=1000, func=exit_frame)
            else:
                return_main(mainroot, main_frame)

        def modiffy():
            c_list_bands.pack_forget()
            l_select_info.pack()
            c_list_bands.config(state='readonly')
            c_list_bands.set('')
            c_list_bands.pack(expand=True, anchor="center")
            f_combo_select.config(height=160)
            b_cancel_header.pack(pady=5)

            f_acept.destroy()
            f_rate.destroy()
            l_photo.pack()

        b_acept.config(command=acept)
        b_mod.config(command=modiffy)
        b_cancel.config(command=cancel)

        b_acept.pack(anchor='center', side="left", padx=65)
        b_mod.pack(anchor='center', side="left", padx=65)
        b_cancel.pack(anchor='center', side="left", padx=65)

        # MODIFICAR
        if is_new:
            for band in bands:
                if band.nombre == str(c_list_bands.get()):
                    print("Homero chino")
                    scalers[0].set(mainroot.concurso.bandas[band.codigo].puntaje['ritmo'])
                    scalers[1].set(mainroot.concurso.bandas[band.codigo].puntaje['uniformidad'])
                    scalers[2].set(mainroot.concurso.bandas[band.codigo].puntaje['coreografia'])
                    scalers[3].set(mainroot.concurso.bandas[band.codigo].puntaje['alineacion'])
                    scalers[4].set(mainroot.concurso.bandas[band.codigo].puntaje['puntualidad'])
                    break

    def check_modiffy_band():
        m_question_entry, modify = True, False
        for band in bands:
            if band.nombre == str(c_list_bands.get()):
                if band.puntaje_total != 0:
                    m_question_entry = messagebox.askyesno('Modificar calificación de banda',
                                            '¿Deseas modificar la calificacion de esta banda?')
                    if not m_question_entry: c_list_bands.set('')
                    else: modify = True
                    break
                else:
                    modify = False
                    break
        if m_question_entry: pack_rate_forms(modify)

    #https://python-course.eu/tkinter/events-and-binds-in-tkinter.php
    c_list_bands.bind("<<ComboboxSelected>>", lambda event: check_modiffy_band())

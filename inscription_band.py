from usesful_funcs import *

def insc_form(mainroot, inscription_frame, main_frame):

    mainroot.change_frame(inscription_frame)

    f_ib_op = tk.Frame(inscription_frame) #PARA LAS OPCIONES
    f_ib_acept = tk.Frame(inscription_frame, bg='red')

    f_ib_op.pack(expand=1, fill='y')
    f_ib_acept.pack(expand=1, fill='y')

    l_ib_title = tk.Label(f_ib_op, text='Inscribir banda', font=('Arial',25))
    pad_options = (20,40)

    #LABELS
    l_ib_name = tk.Label(f_ib_op, text= 'Ingresa el nombre de tu banda', anchor="w")
    l_ib_code = tk.Label(f_ib_op, text='Ingresa un codigo para tu banda', anchor="w")
    l_ib_institution = tk.Label(f_ib_op, text='Ingresa el nombre de la instutición para tu banda')
    l_ib_category = tk.Label(f_ib_op, text='Ingresa una categoria para tu banda')
    #ENTRY
    e_ib_name = tk.Entry(f_ib_op, width=25, font=('Arial', 12), state='normal')
    e_ib_code = tk.Entry(f_ib_op, width=25, font=('Arial', 12))
    e_ib_code.delete(0, tk.END)
    e_ib_institution = tk.Entry(f_ib_op, width=25, font=('Arial', 12))
    e_ib_institution.delete(0, tk.END)
    #COMBOBOX
    c_ib_category = Combobox(f_ib_op, width=23, state='readonly', font=('Arial', 12),
                             values=['Primaria','Básico', 'Bachillerato'])
    c_ib_category.current(0) #PRIMARIA POR DEFECTO

    #FUNCIONES
    def validar_inscripcion():
        print( b_ib_acept.cget('text'))
        if b_ib_acept.cget('text') == 'Aceptar':
            valid = mainroot.concurso.inscribir_banda(
                e_ib_name.get(), e_ib_institution.get(), e_ib_code.get(), c_ib_category.get()
            )
            if valid == 0:
                l_ib_info.config(text=f'Se agregó correctamente\nLa banda {e_ib_name.get()} ({e_ib_code.get()})')
                disable_widgets([e_ib_name, e_ib_institution, e_ib_code, c_ib_category, b_ib_acept, b_ib_cancel])
                mainroot.after(ms=2500, func= exit_form)

            else:
                l_ib_info.config(text=valid)
        else:
            disable_widgets([e_ib_name, e_ib_institution, e_ib_code, c_ib_category, b_ib_acept, b_ib_cancel])
            mainroot.after(ms=2500, func=exit_form)
    def exit_form():
        b_ib_acept.config(text='Aceptar')
        b_ib_cancel.config(text='Cancelar')
        return_main(mainroot, main_frame)

    def verify_cancel():
        l_ib_info.config(text='¿Estás seguro que deseas cancelar?')
        b_ib_acept.config(text='Sí')
        b_ib_cancel.config(text='No')

    #BOTONES
    l_ib_info = tk.Label(f_ib_op, text=' ', font=('Arial', 12))
    b_ib_acept = tk.Button(f_ib_acept, text='Aceptar', font=('Arial', 12), width=15,
                           command=validar_inscripcion)
    b_ib_cancel = tk.Button(f_ib_acept, text='Cancelar', font=('Arial', 12), width=15,
                           command=verify_cancel)
    # GRID
    l_ib_title.grid(column=1, row=0, sticky='nsew', columnspan=4, pady=40)
    l_ib_name.grid(column=1, row=1, padx=pad_options[0])
    e_ib_name.grid(column=2, row=1, padx=pad_options[0])
    l_ib_code.grid(column=1, row=2, padx=pad_options[0], pady=pad_options[1])
    e_ib_code.grid(column=2, row=2, padx=pad_options[0])
    l_ib_category.grid(column=1, row=3, padx=pad_options[0], pady=pad_options[1] - pad_options[1] // 1.1)
    c_ib_category.grid(column=2, row=3, padx=pad_options[0])
    l_ib_institution.grid(column=1, row=4, padx=pad_options[0], pady=pad_options[1])
    e_ib_institution.grid(column=2, row=4, padx=pad_options[0])

    l_ib_info.grid(column=1, row=5, columnspan=2, pady=5)

    #Encontré esta solución de evitar el frame no cambie con pack_propagate y usar update_idletast para que se calcule
    #el tamaño del frame anterior y se aplique al otro frame
    mainroot.update_idletasks()
    print(l_ib_title.winfo_width())
    f_ib_acept.config(width=f_ib_op.winfo_width())
    f_ib_acept.pack_propagate(False)
    b_ib_acept.pack(side='left', padx=100)
    b_ib_cancel.pack(side='left')


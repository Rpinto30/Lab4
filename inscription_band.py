from tkinter import PhotoImage

from usesful_funcs import *

def insc_form(mainroot, inscription_frame, main_frame):
    mainroot.change_frame(inscription_frame)

    f_ib_op = tk.Frame(inscription_frame, width=550, height=420) #PARA LAS OPCIONES
    f_ib_acept = tk.Frame(inscription_frame, width=550, height=80, bg='red')

    img_borrar = PhotoImage(file=r"C:\Users\rodri\PycharmProjects\Lab4\borrar.gif", height=500, width=321)
    l_img_borrar = tk.Label(inscription_frame, image=img_borrar)
    l_img_borrar.image = img_borrar

    f_ib_op.pack_propagate(False)
    f_ib_acept.pack_propagate(False)

    l_img_borrar.pack(side='left')
    f_ib_op.pack(side='top')
    f_ib_acept.pack(side="top")


    l_ib_title = tk.Label(f_ib_op, text='Inscribir banda', font=('Arial',25))
    pad_options = (10,15)

    #LABELS
    l_font, e_font = ('Arial', 12, 'bold'), ('Arial',14)
    l_ib_name = tk.Label(text= 'Nombre de tu banda', font=l_font)
    l_ib_code = tk.Label(text='Codigo para tu banda', font=l_font)
    l_ib_institution = tk.Label(text='Instutición de tu banda', font=l_font)
    l_ib_category = tk.Label(text='Categoria para tu banda', font=l_font)
    #ENTRY
    e_ib_name = tk.Entry(width=25, font=e_font, state='normal')
    e_ib_code = tk.Entry(width=25, font=e_font)
    e_ib_institution = tk.Entry(width=25, font=e_font)
    #COMBOBOX
    c_ib_category = Combobox(width=23, state='readonly', font=e_font,
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
                l_ib_info.config(text=f'Se agregó correctamente\nLa banda {e_ib_name.get()} ({e_ib_code.get()})', fg='black')
                disable_widgets([e_ib_name, e_ib_institution, e_ib_code, c_ib_category, b_ib_acept, b_ib_cancel])
                mainroot.after(ms=2500, func= exit_form)

            else:
                l_ib_info.config(text=valid, fg='red')
        else:
            disable_widgets([e_ib_name, e_ib_institution, e_ib_code, c_ib_category, b_ib_acept, b_ib_cancel])
            mainroot.after(ms=1200, func=exit_form)
    def exit_form():
        b_ib_acept.config(text='Aceptar')
        b_ib_cancel.config(text='Cancelar')
        return_main(mainroot, main_frame)

    def verify_cancel():
        if b_ib_cancel.cget('text') == 'Cancelar':
            l_ib_info.config(text='¿Estás seguro que deseas cancelar?', fg='black')
            b_ib_acept.config(text='Sí')
            b_ib_cancel.config(text='No')
        else:
            l_ib_info.config(text=' ', fg='black')
            b_ib_acept.config(text='Aceptar')
            b_ib_cancel.config(text='Cancelar')

    #BOTONES
    l_ib_info = tk.Label(f_ib_op, text=' ', font=('Arial', 12), fg='black')
    b_ib_acept = tk.Button(text='Aceptar', font=('Arial', 12), width=15,
                           command=validar_inscripcion)
    b_ib_cancel = tk.Button(text='Cancelar', font=('Arial', 12), width=15,
                           command=verify_cancel)
    # PACK
    l_ib_title.pack(pady=30)
    pack_create_line(f_ib_op,l_ib_name, e_ib_name, pad_options[0], pad_options[1], 460,30) #NOMBRE
    pack_create_line(f_ib_op,l_ib_code, e_ib_code, pad_options[0], pad_options[1], 460,30) #CODIGO
    pack_create_line(f_ib_op,l_ib_institution, e_ib_institution, pad_options[0], pad_options[1], 460,30) #INSTITUCION
    pack_create_line(f_ib_op,l_ib_category, c_ib_category, pad_options[0], pad_options[1], 460,30) #CATEGORIA

    l_ib_info.pack(pady=5)
    pack_create_line(f_ib_acept, b_ib_acept, b_ib_cancel, width=460, height=40, _pady=20, bg='red')



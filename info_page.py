from usesful_funcs import *
from tkinter.ttk import Scrollbar
from tkinter import PhotoImage

#USO DE BIND PARA DECTECTAR EVENTOS EN TKINTER
def page_show_info(mainroot, list_frame, main_frame):
    mainroot.change_frame(list_frame)
    #https://stackoverflow.com/questions/7727804/tkinter-using-scrollbars-on-a-canvas
    #izquierdo
    f_izq = tk.Frame(list_frame, width=600, height=500, bg='gray')
    f_izq.pack_propagate(False)
    f_izq.pack(side="left")
    #------------------------CANVAS Y SCROLL
    c_tabla = tk.Canvas(f_izq)
    c_tabla.pack_propagate(False)
    vbar = Scrollbar(f_izq, orient="vertical") #VERTICAL BAR
    vbar.pack(side="left", fill="y")
    vbar.config(command=c_tabla.yview)
    hbar = Scrollbar(f_izq, orient="horizontal") #HORIZONTAL BAR
    hbar.pack(side="bottom", fill="x")
    hbar.config(command=c_tabla.xview)
    #CONFIG AND PACK TABLE
    c_tabla.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    c_tabla.pack(side="left", fill="both", expand=True)
    f_canvas_table = tk.Frame(c_tabla) #Frame dentro del canvas para mover y meter widgets
    c_tabla.create_window((0, 0), window=f_canvas_table, anchor="nw")
    #Usado para modificar el tamaño del scroll cuando se actualice la tabla, uso lambda para no crear otra función más xd
    f_canvas_table.bind("<Configure>",
                        lambda event: c_tabla.configure(scrollregion=c_tabla.bbox("all")))

    #derecha
    f_der = tk.Frame(list_frame, width=500, height=500, bg='gray')
    f_der.pack_propagate(False)
    f_der.pack(side="right")

    bandas = [band for band in mainroot.concurso.bandas.values()]
    tabla_bands = [["Codigo", "Nombre", "Institucion", "Categoria", "Puntaje"]]

    for iterar in bandas:
        tabla_bands.append([iterar.codigo, iterar.nombre, iterar.institucion, iterar.categoria, iterar.puntaje_total])

    f_tabla = Tabla(f_canvas_table, len(tabla_bands), len(tabla_bands[0]), tabla_bands, border_width=2)
    c_tabla.config(scrollregion=c_tabla.bbox("all")) #Configurar el tamaño de la tabla

    #botones
    photo = PhotoImage(file=r'imagenes/prueba_imagen.png', width=500, height=170)
    l_photo = tk.Label(f_der, image=photo)
    l_photo.image = photo
    l_photo.pack()

    bg_frame = 'gray'
    bg_buttons = 'black'
    fg_buttons = 'white'
    f_buttons = tk.Frame(f_der, bg=bg_frame)
    f_buttons.pack(anchor='center', expand=1, fill='y')

    l_men_info = tk.Label(f_der, text='Filtrar por Categoria', bg=bg_frame,  font=('Arial', 20, 'bold'), fg='black')
    front_l = ('Arial', 15, 'bold')
    width_b = 25

    b_gen = tk.Button(f_buttons, text='General', width=width_b, font=front_l, fg=fg_buttons, bg=bg_buttons, cursor='hand2')
    b_primaria = tk.Button(f_buttons, text='Primaria', width=width_b, font=front_l, fg=fg_buttons, bg=bg_buttons, cursor='hand2')
    b_basico = tk.Button(f_buttons, text='Basico', width=width_b, font=front_l, fg=fg_buttons, bg=bg_buttons, cursor='hand2')
    b_bach = tk.Button(f_buttons, text='Bachillerato', width=width_b, font=front_l, fg=fg_buttons, bg=bg_buttons, cursor='hand2')
    b_salir = tk.Button(f_buttons, text='Salir', width=width_b, font=front_l, command=lambda:return_main(mainroot,main_frame), fg='red', cursor='x_cursor')

    l_men_info.pack(pady=5)
    b_gen.pack(pady=5, padx=50)
    b_primaria.pack(pady=5, padx=50)
    b_basico.pack(pady=5, padx=50)
    b_bach.pack(pady=5, padx=50)
    b_salir.pack(pady=5, padx=50)

    bandas_primaria = []
    bandas_basico = []
    bandas_bach = []
    for band in bandas:
        if band.categoria == 'Primaria':
            bandas_primaria.append(band)
        elif band.categoria == 'Básico':
            bandas_basico.append(band)
        elif band.categoria == 'Bachillerato':
            bandas_bach.append(band)

    if len(bandas) == 0:
        b_gen.config(state='disabled')
    if len(bandas_primaria) == 0: b_primaria.config(state='disabled')
    if len(bandas_basico) == 0: b_basico.config(state='disabled')
    if len(bandas_bach) == 0: b_bach.config(state='disabled')

    def filter_table(table, list_band, gen=False):
        nonlocal f_tabla, tabla_bands
        table.destroy_table()
        for celda in f_canvas_table.winfo_children(): celda.destroy()

        if gen:
            tabla_bands = [["Codigo", "Nombre", "Institucion", "Categoria", "Puntaje"]]
            for itera in list_band:
                tabla_bands.append([ itera.codigo,itera.nombre, itera.institucion, itera.categoria, itera.puntaje_total])
        else:
            tabla_bands = [["Codigo", "Nombre", "Institucion", "Puntaje"]]
            for  itera in list_band:
                tabla_bands.append([itera.codigo,itera.nombre, itera.institucion, itera.puntaje_total])

        table = Tabla(f_canvas_table, len(tabla_bands), len(tabla_bands[0]), tabla_bands, border_width=1)
        table.confi_colum(0, 7)  # Configurar tamaño columnas
        table.confi_colum(1, 15)
        table.confi_colum(2, 15)
        table.confi_colum(3, 11)

    b_gen.config(command=lambda: filter_table(f_tabla, bandas, True))
    b_primaria.config(command=lambda: filter_table(f_tabla, bandas_primaria))
    b_basico.config(command=lambda: filter_table(f_tabla, bandas_basico))
    b_bach.config(command=lambda: filter_table(f_tabla, bandas_bach))






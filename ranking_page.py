from usesful_funcs import *
from tkinter.ttk import Scrollbar
from tkinter import PhotoImage

def page_show_ranking(mainroot, ranking_frame, main_frame):
    mainroot.change_frame(ranking_frame)
    # https://stackoverflow.com/questions/7727804/tkinter-using-scrollbars-on-a-canvas
    f_table = tk.Frame(ranking_frame, width=570, height=500)
    f_table.pack_propagate(False)

    f_options = tk.Frame(ranking_frame, width=430, height=500, bg='#3C473B')
    f_options.pack_propagate(False)
    f_table.pack(anchor="center", side='right')
    f_options.pack(anchor='center', side='right')

    # ------------------------CANVAS Y SCROLL
    c_tabla = tk.Canvas(f_table)
    c_tabla.pack_propagate(False)
    vbar = Scrollbar(f_table, orient="vertical")  # VERTICAL BAR
    vbar.pack(side="left", fill="y")
    vbar.config(command=c_tabla.yview)
    hbar = Scrollbar(f_table, orient="horizontal")  # HORIZONTAL BAR
    hbar.pack(side="bottom", fill="x")
    hbar.config(command=c_tabla.xview)
    # CONFIG AND PACK TABLE
    c_tabla.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    c_tabla.pack(side="right", fill="both", expand=True)
    f_canvas_table = tk.Frame(c_tabla)  # Frame dentro del canvas para mover y meter widgets
    c_tabla.create_window((0, 0), window=f_canvas_table, anchor="nw")
    # Usado para modificar el tamaño del scroll cuando se actualice la tabla, uso lambda para no crear otra función más xd
    f_canvas_table.bind("<Configure>",
                        lambda event: c_tabla.configure(scrollregion=c_tabla.bbox("all")))


    bandas = [band for band in mainroot.concurso.bandas.values()]
    tabla_bands = [["Puesto","Nombre", "Institución", "Puntaje Final"]]

    sorted_bands = list(sorted(bandas, key=lambda point: point.puntaje_total, reverse=True))
    for n,iterar in enumerate(sorted_bands, 1):
        tabla_bands.append([n,iterar.nombre, iterar.institucion, iterar.puntaje_total])

    f_tabla_in_canvas = Tabla(f_canvas_table, len(tabla_bands), len(tabla_bands[0]), tabla_bands, border_width=1)
    c_tabla.config(scrollregion=c_tabla.bbox("all"))
    f_tabla_in_canvas.confi_colum(0, 7)#Configurar tamaño columnas
    f_tabla_in_canvas.confi_colum(1, 15)
    f_tabla_in_canvas.confi_colum(2, 15)
    f_tabla_in_canvas.confi_colum(3, 11)

    #BOTONES
    photo = PhotoImage(file=r'imagenes/prueba_ranking.gif', width=430, height=170)
    l_photo = tk.Label(f_options, image=photo)
    l_photo.image = photo
    l_photo.pack()

    bg_frame = '#726899'
    f_buttons = tk.Frame(f_options, bg=bg_frame)
    f_buttons.pack(anchor='center', expand=1, fill='y')

    l_info = tk.Label(f_buttons, text='Selecciona para generar un ranking', bg=bg_frame, font=('Arial', 12))
    font_l = ('Arial', 15)
    width_b = 18

    b_gen = tk.Button(f_buttons, text='General', width=width_b, font=font_l)

    b_primaria = tk.Button(f_buttons, text='Primaria', width=width_b, font=font_l)
    b_basico = tk.Button(f_buttons, text='Básico', width=width_b,font=font_l)
    b_bachillerato = tk.Button(f_buttons, text='Bachillerato', width=width_b,font=font_l)
    b_salir = tk.Button(f_buttons, text='Salir', width=width_b,font=font_l, command=lambda:return_main(mainroot,main_frame))

    l_info.pack(pady=5)
    b_gen.pack(pady=5, padx=50)
    b_primaria.pack(pady=5)
    b_basico.pack(pady=5)
    b_bachillerato.pack(pady=5)
    b_salir.pack(pady=25)

    bandas_primaria = []
    bandas_basico = []
    bandas_bach = []
    for band in bandas:
        if band.categoria == 'Primaria': bandas_primaria.append(band)
        elif band.categoria == 'Básico': bandas_basico.append(band)
        elif band.categoria == 'Bachillerato': bandas_bach.append(band)

    if len(bandas) == 0:
        l_info.config(text='No hay bandas registradas')
        b_gen.config(state='disabled')
    if len(bandas_primaria) == 0: b_primaria.config(state='disabled')
    if len(bandas_basico) == 0: b_basico.config(state='disabled')
    if len(bandas_bach) == 0: b_bachillerato.config(state='disabled')

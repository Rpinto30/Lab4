from usesful_funcs import *
from tkinter.ttk import Scrollbar

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
    tabla_bands = [["Posición","Nombre", "Institución", "Puntaje Final"]]

    sorted_bands = list(sorted(bandas, key=lambda point: point.puntaje_total, reverse=True))
    for n,iterar in enumerate(sorted_bands, 1):
        tabla_bands.append([n,iterar.nombre, iterar.institucion, iterar.puntaje_total])

    f_tabla_in_canvas = Tabla(f_canvas_table, len(tabla_bands), len(tabla_bands[0]), tabla_bands, border_width=1)
    c_tabla.config(scrollregion=c_tabla.bbox("all"))
    f_tabla_in_canvas.confi_colum() #Configurar tamaño columnas


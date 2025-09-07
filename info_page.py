import tkinter

from usesful_funcs import *
from tkinter.ttk import Scrollbar

#USO DE BIND PARA DECTECTAR EVENTOS EN TKINTER

def page_show_info(mainroot, list_frame, main_frame):
    mainroot.change_frame(list_frame)
    #https://stackoverflow.com/questions/7727804/tkinter-using-scrollbars-on-a-canvas
    #izquierdo
    f_izq = tk.Frame(list_frame, width=600, height=500)
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
    f_der = tk.Frame(list_frame, width=500, height=500, bg='red')
    f_der.pack_propagate(False)
    f_der.pack(side="right")

    bandas = [band for band in mainroot.concurso.bandas.values()]
    tabla_bands = [["Codigo", "Nombre", "Institucion", "Categoria", "Puntaje"]]

    for iterar in bandas:
        tabla_bands.append([iterar.codigo, iterar.nombre, iterar.institucion, iterar.categoria, iterar.puntaje_total])

    f_tabla = Tabla(f_canvas_table, len(tabla_bands), len(tabla_bands[0]), tabla_bands, border_width=2)
    c_tabla.config(scrollregion=c_tabla.bbox("all")) #Configurar el tamaño de la tabla




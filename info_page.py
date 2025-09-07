from usesful_funcs import *
from tkinter.ttk import Scrollbar

def page_show_info(mainroot, list_frame, main_frame):
    mainroot.change_frame(list_frame) #izquierdo
    f_izq = tk.Frame(list_frame, width=600, height=500)
    f_izq.pack_propagate(False)
    f_izq.pack(side="left")
    tabla_canvas = tk.Canvas(f_izq, scrollregion=(0, 0, 800, 800))
    tabla_canvas.pack_propagate(False)
    vbar = Scrollbar(f_izq, orient="vertical")
    vbar.pack(side="left", fill="y")
    vbar.config(command=tabla_canvas.yview)
    hbar = Scrollbar(f_izq, orient="horizontal")
    hbar.pack(side="bottom", fill="x")
    hbar.config(command=tabla_canvas.xview)
    tabla_canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    tabla_canvas.pack(side="left", fill="both", expand=True)


     #derecha
    f_der = tk.Frame(list_frame, width=500, height=500, bg='red')
    f_der.pack_propagate(False)
    f_der.pack(side="right")

    bandas = [band for band in mainroot.concurso.bandas.values()]
    tabla_bands = [["Codigo", "Nombre", "Institucion", "Categoria", "Puntaje"]]

    for iterar in bandas:
        tabla_bands.append([iterar.codigo, iterar.nombre, iterar.institucion, iterar.categoria, iterar.puntaje_total])

    f_tabla = Tabla(tabla_canvas, len(tabla_bands ), 5, tabla_bands )




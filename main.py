import tkinter as tk
from tkinter import PhotoImage

#IMPORTACION DE CLASES
from Clases import Concurso
from inscription_band import insc_form
from info_page import page_show_info
from rate_page import rate_form
from ranking_page import page_show_ranking

def show():
    for i,j in root.concurso.bandas.items():
        print(f'code:{i} banda:{j.nombre}, {j.categoria}')

def salir():
    if root.CURRENT_FRAME == principal_frame: root.quit()
    else: root.change_frame(principal_frame)

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Concurso de Bandas - Quetzaltenango")
        self.geometry("1000x500")
        self.resizable(False,False)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.concurso = Concurso()

        self.CURRENT_FRAME = None
        self.protocol("WM_DELETE_WINDOW", salir)
        #Concurso()

    def change_frame(self, frame):
        if self.CURRENT_FRAME is not None and self.CURRENT_FRAME != principal_frame:
            for widget in self.CURRENT_FRAME.winfo_children(): widget.destroy()

        self.CURRENT_FRAME = frame
        self.CURRENT_FRAME.grid(row=0, column=0, sticky='nsew')
        self.CURRENT_FRAME.tkraise()

BUTTONS_PRINCIPAL_MENU = []
IMAGES_BUTTONS_PRINCIPAL_MENU = []
BACKGROUND_PRINCIPAL = "#ffffff"

root = Window()
#APARTADO PARA LA CREACION DE LOS FRAMES PRINCIPALES
principal_frame = tk.Frame(root)
root.change_frame(principal_frame)
principal_frame.config(bg=BACKGROUND_PRINCIPAL, width=1000, height=500)

inscribe_frame = tk.Frame(root)
inscribe_frame.config(bg='#ad3e3e',width=1000, height=500)

rate_frame = tk.Frame(root)
rate_frame.config(bg='#449147', width=1000, height=500)

list_frame = tk.Frame(root)
list_frame.config(bg='#6C74B8',width=1000, height=500)

ranking_frame = tk.Frame(root)
ranking_frame.config(bg='#B8B76C',width=1000, height=500)
#-----------------------PRINCIPAL------------------
img_header = PhotoImage(file=r'imagenes\header.png', width=1000, height=131)
etiqueta = tk.Label(principal_frame,image=img_header)
etiqueta.pack(pady=5)
IMAGES_BUTTONS_PRINCIPAL_MENU.extend([
    PhotoImage(file = r"imagenes\btt_inscrb.png",height=60, width=600),
    PhotoImage(file=r"imagenes\btt_rate.png", height=60, width=600),
    PhotoImage(file=r"imagenes\prubea boton.png", height=60, width=600),
    PhotoImage(file=r"imagenes\prubea boton.png", height=60, width=600)
])

buttons_frame = tk.Frame(principal_frame, bg = BACKGROUND_PRINCIPAL)
buttons_frame.pack(pady=15)

button_inscr_bad = tk.Button(buttons_frame,
                             command=lambda:insc_form(root, inscribe_frame,principal_frame))
button_rate = tk.Button(buttons_frame,
                        command=lambda:rate_form(root, rate_frame, principal_frame))
button_list_bands = tk.Button(buttons_frame,
                              command=lambda: page_show_info(root, list_frame, principal_frame))
button_gen_rank = tk.Button(buttons_frame,
                            command=lambda: page_show_ranking(root, ranking_frame, principal_frame))
#AGREGAR BOTONES A FRAME DE BOTONES EN EL MENÚ PRINCIPAL
BUTTONS_PRINCIPAL_MENU.extend([button_inscr_bad, button_rate, button_list_bands, button_gen_rank])
for n,i in enumerate(BUTTONS_PRINCIPAL_MENU):
    i.configure(bg=BACKGROUND_PRINCIPAL, borderwidth=1,highlightthickness=0,relief="flat",
                image=IMAGES_BUTTONS_PRINCIPAL_MENU[n], cursor='hand2' )
    i.pack(pady=10)

try:
    root.mainloop()
except Exception as e: print(e)
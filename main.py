import tkinter as tk
from tkinter import PhotoImage


#IMPORTACION DE CLASES
from Clases import Concurso
from inscription_band import insc_form

def salir():
    if root.CURRENT_FRAME == principal_frame: root.quit()
    else: root.change_frame(principal_frame)

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Concurso de Bandas - Quetzaltenango")
        self.geometry("1000x500")
        #self.resizable(False,False)
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
principal_frame = tk.Frame(root)
root.change_frame(principal_frame)

principal_frame.config(bg=BACKGROUND_PRINCIPAL, width=800, height=500)

inscribe_frame = tk.Frame(root)
inscribe_frame.config(bg='#ad3e3e',width=1000, height=500)

register_frame = tk.Frame(root)
register_frame.config(bg='#449147',width=1000, height=500)

#-----------------------PRINCIPAL------------------
etiqueta = tk.Label(
    principal_frame,
    text="Sistema de Inscripción y Evaluación de Bandas Escolares\nDesfile 15 de Septiembre - Quetzaltenango",
    font=("Arial", 20, "bold"),
    justify="center"
)
etiqueta.pack(pady=50)#377 42
IMAGES_BUTTONS_PRINCIPAL_MENU.extend([
    PhotoImage(file = r"prubea boton.png",height=42, width=380),
    PhotoImage(file=r"prubea boton.png", height=42, width=380),
    PhotoImage(file=r"prubea boton.png", height=42, width=380),
    PhotoImage(file=r"prubea boton.png", height=42, width=380)
])
button_inscr_bad = tk.Button(principal_frame, command=lambda:insc_form(root, inscribe_frame,principal_frame))
button_register = tk.Button(principal_frame)
button_list_bands = tk.Button(principal_frame)
button_gen_rank = tk.Button(principal_frame)
BUTTONS_PRINCIPAL_MENU.extend([button_inscr_bad, button_register, button_list_bands, button_gen_rank])
for n,i in enumerate(BUTTONS_PRINCIPAL_MENU):
    i.configure(bg=BACKGROUND_PRINCIPAL, borderwidth=1,highlightthickness=0,relief="flat",
                image=IMAGES_BUTTONS_PRINCIPAL_MENU[0], cursor='hand2' )
    i.pack(pady=10)

#-----------------------INSCRIB BAND------------------


#------------------------REGISTER NOTE--------------
lb = tk.Label(register_frame,
    text="HOLAAA",
    font=("Arial", 20, "bold"),
    justify="center")
lb.pack()
root.mainloop()
import tkinter as tk
from tkinter import messagebox


def inscribir_banda():
    messagebox.showinfo("Inscripción", "Aquí se inscribiría una banda")

def registrar_evaluacion():
    root.change_frame(register_frame)

def listar_bandas():
    messagebox.showinfo("Listado", "Aquí se mostraría el listado de bandas")

def ver_ranking():
    messagebox.showinfo("Ranking", "Aquí se mostraría el ranking final")

def salir():
    root.quit()

class Window(tk.Tk):
    def __init__(self, frame:tk.Frame):
        super().__init__()
        self.title("Concurso de Bandas - Quetzaltenango")
        self.geometry("800x500")
        self.frames = frame
        self.CURRENT_FRAME = frame
        self.change_frame(self.CURRENT_FRAME)

    def change_frame(self, frame):
        self.CURRENT_FRAME = frame
        self.CURRENT_FRAME.grid(row=0, column=0, sticky='nsew')
        self.CURRENT_FRAME.tkraise()

BUTTONS_PRINCIPAL_MENU = []
principal_frame = tk.Frame()
principal_frame.config(bg='#4287f5', width=800, height=500)

inscribe_frame = tk.Frame()

register_frame = tk.Frame()
register_frame.config(bg='#449147',width=1000, height=500)

#-----------------------INSCRIBE------------------
etiqueta = tk.Label(
    principal_frame,
    text="Sistema de Inscripción y Evaluación de Bandas Escolares\nDesfile 15 de Septiembre - Quetzaltenango",
    font=("Arial", 20, "bold"),
    justify="center"
)
etiqueta.pack(pady=50)
button_inscr_bad = tk.Button(principal_frame, text='Inscribir bandas por categoria')
button_register = tk.Button(principal_frame, text='Registrar puntajes por criterios', command=registrar_evaluacion)
button_list_bands = tk.Button(principal_frame, text='Listar bandas inscritas')
button_gen_rank = tk.Button(principal_frame, text='Generar ranking')
BUTTONS_PRINCIPAL_MENU.extend([button_inscr_bad, button_register, button_list_bands, button_gen_rank])
for i in BUTTONS_PRINCIPAL_MENU:
    i.config(width=30, font=('Arial', 15))
    i.pack(pady=10)


#------------------------REGISTER--------------
lb = tk.Label(register_frame,
    text="HOLAAA",
    font=("Arial", 20, "bold"),
    justify="center")
lb.pack()
root = Window(principal_frame)
root.mainloop()
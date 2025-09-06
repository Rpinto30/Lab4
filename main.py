import tkinter as tk
from tkinter import messagebox


def inscribir_banda():
    root.change_frame(inscribe_frame)
    f_ib = tk.Frame(inscribe_frame)
    f_ib.pack()
    #inscribe_frame.grid_columnconfigure(0, weight=1)

    l_ib_title = tk.Label(f_ib, text='Inscribir banda', font=('Arial',20))

    #LABELS
    l_ib_name = tk.Label(f_ib, text= 'Ingresa el nombre de tu banda')

    l_ib_code = tk.Label(f_ib, text='Ingresa un codigo para tu banda')
    l_ib_institution = tk.Label(f_ib, text='Ingresa un codigo para tu banda')
    #ENTRIES
    e_ib_name = tk.Entry(f_ib, width=25, font=('Arial', 15))
    e_ib_code = tk.Entry(f_ib, width=25, font=('Arial', 15))
    e_ib_institution = tk.Entry(f_ib, width=25, font=('Arial', 15))
    e_ib_category = tk.Entry(f_ib, width=25, font=('Arial', 15))

    b_ib_exit = tk.Button(f_ib, text='Cancelar', font=('Arial',12), command=return_main)


    l_ib_title.grid(column=1, row=0, pady=20, sticky='nsew',columnspan=4)
    l_ib_name.grid(column=1, row=1, padx=20)
    e_ib_name.grid(column=2, row=1, padx=20)
    l_ib_code.grid(column=1, row=2, padx=20, pady=10)
    e_ib_code.grid(column=2, row=2, padx=20)
    l_ib_code.grid(column=1, row=2, padx=20, pady=10)
    e_ib_code.grid(column=2, row=2, padx=20)


def registrar_evaluacion():
    root.change_frame(register_frame)

def listar_bandas():
    messagebox.showinfo("Listado", "Aquí se mostraría el listado de bandas")

def ver_ranking():
    messagebox.showinfo("Ranking", "Aquí se mostraría el ranking final")


def return_main(): root.change_frame(principal_frame)
def salir(): root.quit()

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Concurso de Bandas - Quetzaltenango")
        self.geometry("800x500")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.CURRENT_FRAME = None

    def change_frame(self, frame):

        self.CURRENT_FRAME = frame
        self.CURRENT_FRAME.grid(row=0, column=0, sticky='nsew')
        self.CURRENT_FRAME.tkraise()

BUTTONS_PRINCIPAL_MENU = []

root = Window()
principal_frame = tk.Frame(root)
root.change_frame(principal_frame)

principal_frame.config(bg='#4287f5', width=800, height=500)

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
etiqueta.pack(pady=50)
button_inscr_bad = tk.Button(principal_frame, text='Inscribir bandas por categoria', command=inscribir_banda)
button_register = tk.Button(principal_frame, text='Registrar puntajes por criterios', command=registrar_evaluacion)
button_list_bands = tk.Button(principal_frame, text='Listar bandas inscritas')
button_gen_rank = tk.Button(principal_frame, text='Generar ranking')
BUTTONS_PRINCIPAL_MENU.extend([button_inscr_bad, button_register, button_list_bands, button_gen_rank])
for i in BUTTONS_PRINCIPAL_MENU:
    i.config(width=30, font=('Arial', 15))
    i.pack(pady=10)


#-----------------------INSCRIB BAND------------------


#------------------------REGISTER NOTE--------------
lb = tk.Label(register_frame,
    text="HOLAAA",
    font=("Arial", 20, "bold"),
    justify="center")
lb.pack()
root.mainloop()
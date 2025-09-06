import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter.ttk import Combobox #Para el menú deslplegable

def inscribir_banda():
    root.change_frame(inscribe_frame)
    f_ib_op = tk.Frame(inscribe_frame) #PARA LAS OPCIONES
    f_ib_op.pack()
    f_ib_acept = tk.Frame(inscribe_frame)
    f_ib_acept.pack()

    l_ib_title = tk.Label(f_ib_op, text='Inscribir banda', font=('Arial',35))
    pady_options = 30
    #LABELS
    l_ib_name = tk.Label(f_ib_op, text= 'Ingresa el nombre de tu banda', anchor="w")
    l_ib_code = tk.Label(f_ib_op, text='Ingresa un codigo para tu banda', anchor="w")
    l_ib_institution = tk.Label(f_ib_op, text='Ingresa el nombre de la instutición para tu banda')
    l_ib_category = tk.Label(f_ib_op, text='Ingresa una categoria para tu banda')
    #ENTRY
    global e_ib_name
    e_ib_name = tk.Entry(f_ib_op, width=25, font=('Arial', 12))
    e_ib_code = tk.Entry(f_ib_op, width=25, font=('Arial', 12))
    e_ib_code.delete(0, tk.END)
    e_ib_institution = tk.Entry(f_ib_op, width=25, font=('Arial', 12))
    e_ib_institution.delete(0, tk.END)
    #COMBOBOX
    c_ib_category = Combobox(f_ib_op, width=23, state='readonly', font=('Arial', 12),
                             values=['Primaria','Básico', 'Bachillerato'])
    #BUTTONS
    b_ib_acept = tk.Button(f_ib_acept, text='Cancelar', font=('Arial',12), command=return_main)
    l_ib_error = tk.Label(f_ib_op, text=' ', font=('Arial',12))
    #GRID
    l_ib_title.grid(column=1, row=0, sticky='nsew',columnspan=4, pady=55)
    l_ib_name.grid(column=1, row=1, padx=20)
    e_ib_name.grid(column=2, row=1, padx=20)
    l_ib_code.grid(column=1, row=2, padx=20, pady=pady_options)
    e_ib_code.grid(column=2, row=2, padx=20)
    l_ib_category.grid(column=1, row=3, padx=20, pady=pady_options-pady_options//1.1)
    c_ib_category.grid(column=2, row=3, padx=20)
    l_ib_institution.grid(column=1, row=4, padx=20, pady=pady_options)
    e_ib_institution.grid(column=2, row=4, padx=20)

    l_ib_error.grid(column=1, row=5, columnspan=2, pady=15)
    b_ib_acept.pack(pady=20, padx=253)


#def inscrib_banda(e_name, e_codigo...) Herman:
    #Concurso.inscribir(e_ib_name.get(), ...)
    #    -> Si name no está vacio  (if e_name != '')
    #    -> Si codigo no está registrado
    #    -> Si institucion no vacia
    #           Dentro del diccionario de concurso, creas banda()
                #Return 0
    #       Sino
    #           return 1

def registrar_evaluacion():
    root.change_frame(register_frame)

def listar_bandas():
    messagebox.showinfo("Listado", "Aquí se mostraría el listado de bandas")

def ver_ranking():
    messagebox.showinfo("Ranking", "Aquí se mostraría el ranking final")


def return_main(): root.change_frame(principal_frame)
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

        self.CURRENT_FRAME = None
        self.protocol("WM_DELETE_WINDOW", salir)
        #Concurso()

    def change_frame(self, frame):

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
button_inscr_bad = tk.Button(principal_frame, command=inscribir_banda)
button_register = tk.Button(principal_frame, command=registrar_evaluacion)
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
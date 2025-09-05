import tkinter as tk
from tkinter import messagebox

def inscribir_banda():
    messagebox.showinfo("Inscripción", "Aquí se inscribiría una banda")

def registrar_evaluacion():
    messagebox.showinfo("Evaluación", "Aquí se registrarían los puntajes")

def listar_bandas():
    messagebox.showinfo("Listado", "Aquí se mostraría el listado de bandas")

def ver_ranking():
    messagebox.showinfo("Ranking", "Aquí se mostraría el ranking final")

def salir():
    root.quit()

BUTTONS_PRINCIPAL_MENU = []

root = tk.Tk()
root.title("Concurso de Bandas - Quetzaltenango")
root.geometry("800x500")

barra_menu = tk.Menu(root)
principal_frame = tk.Frame(root)
principal_frame.config(bg='#4287f5', width=800, height=500)
principal_frame.pack(expand=True, fill='both')
#principal_frame.grid(column=0, row=0, sticky='nsew', rowspan=10)

#BASE MENU PRINCIAPL
etiqueta = tk.Label(
    principal_frame,
    text="Sistema de Inscripción y Evaluación de Bandas Escolares\nDesfile 15 de Septiembre - Quetzaltenango",
    font=("Arial", 20, "bold"),
    justify="center"
)
etiqueta.pack(pady=50)
button_inscr_bad = tk.Button(principal_frame, text='Inscribir bandas por categoria')
button_register = tk.Button(principal_frame, text='Registrar puntajes por criterios')
button_list_bands = tk.Button(principal_frame, text='Listar bandas inscritas')
button_gen_rank = tk.Button(principal_frame, text='Generar ranking')
BUTTONS_PRINCIPAL_MENU.extend([button_inscr_bad, button_register, button_list_bands, button_gen_rank])
for i in BUTTONS_PRINCIPAL_MENU:
    i.config(width=30, font=('Arial', 15))
    i.pack(pady=10)


menu_opciones = tk.Menu(barra_menu, tearoff=0)
menu_opciones.add_command(label="Inscribir Banda", command=inscribir_banda)
menu_opciones.add_command(label="Registrar Evaluación", command=registrar_evaluacion)
menu_opciones.add_command(label="Listar Bandas", command=listar_bandas)
menu_opciones.add_command(label="Ver Ranking", command=ver_ranking)
menu_opciones.add_separator()
menu_opciones.add_command(label="Salir", command=salir)

barra_menu.add_cascade(label="Opciones", menu=menu_opciones)

root.config(menu=barra_menu)



root.mainloop()
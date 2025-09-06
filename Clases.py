import tkinter as tk


class BandaParticipante:
    def __init__(self, nombre, institucion, codigo):
        self.nombre = nombre
        self._institucion = institucion
        self._codigo = codigo

    def mostrar_info(self):
        return f"Nombre de la banda {self.nombre} | Institucion {self._institucion} | Codigo {self._codigo}"

categorias = ["primaria","basico", "bachillerato"]
class BandaEscolar(BandaParticipante):
    def __init__(self, nombre, institucion, codigo, categoria, puntaje):
        super().__init__(nombre, institucion, codigo)
        self._categoria = categoria
        self._puntaje = 0

    @property
    def categoria(self):
        return categorias

    def set_categoria(self, categori):
        if categori in categorias:
            self._categoria = categori

    def registrar_puntajes(self, puntos):
        if  0 <= puntos <= 10:
            self._puntaje = puntos

    def mostrar_info(self):
        pass

class Concurso:
    def __init__(self):
        self.bandas = {}

    def inscribir_banda(self, entry_nombre:str, entry_institucion:str, entry_codigo:str, entry_categoria:str ):
        error = ''
        if entry_codigo in self.bandas:
            if error != '' : error += ','
            error += " Codigo de banda ya utilizado"
        elif entry_codigo.strip() == "":
            if error != '': error += ','
            error += " Codigo de banda vacío"
        if entry_nombre.strip() == "":
            if error != '': error += ','
            error += " Nombre vacío"
        if entry_institucion.strip() == "":
            if error != '': error += ','
            error += " Institución vacía"
        if entry_categoria.strip() == "":
            if error != '': error += ','
            error += " Categoria vacia"

        if error == '':
            self.bandas[entry_codigo] = BandaEscolar(entry_nombre, entry_institucion, entry_codigo, entry_categoria, 0)
            return 0
        else:
            error = "Error: " + error
            return error

    def registrar_puntaje(self, search_codigo:tk.Entry, entry_puntaje:tk.Entry):
        search_codigo = tk.Entry(search_codigo)
        if search_codigo in self.bandas:
            pass

    def listar_bandas(self):
        for banda in self.bandas.values():
            banda.mostrar_info()






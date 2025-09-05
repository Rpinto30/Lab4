import tkinter as tk


class BandaParticipante:
    def __init__(self, nombre, institucion, codigo):
        self.nombre = nombre
        self.institucion = institucion
        self.codigo = codigo

    def mostrar_info(self):
        return f"Nombre de la banda {self.nombre} | Institucion {self.institucion} | Codigo {self.codigo}"

categorias = ["primaria","basico", "bachillerato"]
class BandaEscolar(BandaParticipante):
    def __init__(self, nombre, institucion, codigo, categoria, puntajes):
        super().__init__(nombre, institucion, codigo)
        self._categoria = categoria
        self._puntajes = {}

    def get_categoria(self):
        return categorias

    def set_categoria(self, categori):
        if self._categoria in categorias:
            self._categoria = categori
            return  True
        else:
            return "Debe ser una de las categorias indicadas"

    def registrar_puntajes(self, puntos):
        if puntos >= 0 and puntos <= 10:
            self._puntajes = puntos
            return True
        else:
            return "Debe ser uno de los puntajes dentro del rango"

    def mostrar_info(self):
        return f"Categoria {self._categoria} | Puntaje {self._puntajes}"

be = BandaEscolar
class Concurso:
    def __init__(self):
        self.bandas = {}

    def inscribir_banda(self, entry_nombre:tk.Entry, entry_institucion:tk.Entry, entry_codigo:tk.Entry ):
        while True:
            entry_codigo = tk.Entry(entry_codigo)
            if entry_codigo not in self.bandas:
                break
            else:
                pass

        entry_nombre = tk.Entry(entry_nombre)
        entry_institucion = tk.Entry(entry_institucion)
        self.bandas[entry_codigo.get()] = BandaEscolar

    def registrar_puntaje(self, search_codigo:tk.Entry, entry_puntaje:tk.Entry):
        search_codigo = tk.Entry(search_codigo)
        if search_codigo in self.bandas:
            pass

    def listar_bandas(self):
        for codigo, valor in self.bandas.items():
            return (f"Codigo {codigo} | Nombre {valor.entry_nombre} | puntajes {valor.puntajes}")







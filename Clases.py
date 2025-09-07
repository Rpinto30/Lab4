class BandaParticipante:
    def __init__(self, nombre, institucion, codigo):
        self.nombre = nombre
        self._institucion = institucion
        self._codigo = codigo

    @property
    def codigo(self):
        return self._codigo

    @property
    def institucion(self):
        return self._institucion

    def mostrar_info(self):
        return f"Nombre de la banda {self.nombre} | Institucion {self._institucion} | Codigo {self._codigo}"


class BandaEscolar(BandaParticipante):
    def __init__(self, nombre, institucion, codigo, categoria, puntaje):
        super().__init__(nombre, institucion, codigo)
        self._categoria = categoria
        self._puntaje = {"ritmo": 0, "uniformidad": 0, "coreografia": 0, "alineacion": 0, "puntualidad": 0}
        self.__puntaje_total = 0

    @property
    def categoria(self):
        return self._categoria

    def set_categoria(self, categori):
        if categori in ["Primaria", "Básico", "Bachillerato"]:
            self._categoria = categori

    def registrar_puntajes(self, puntos, criterio):
        try:
            if  0 <= puntos <= 10:
                self._puntaje [criterio] = puntos
                return 0
        except ValueError:
            return "Error debe ser un numero"

    def suma_total(self):
        self.__puntaje_total = 0
        for suma in self._puntaje.values():
            self.__puntaje_total += suma

    @property
    def puntaje_total(self):
        return self.__puntaje_total

    @property
    def puntaje(self): return self._puntaje

    def mostrar_info(self):
        valores = [self.nombre, self._institucion, self._codigo, self._categoria, self.__puntaje_total]
        return valores

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

    def listar_bandas(self):
        for banda in self.bandas.values():
            banda.mostrar_info()






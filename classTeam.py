class Equipo:
    def __init__(self, nombre, puntaje = 0 ):
        self.nombre = nombre
        self.puntaje = puntaje

    def set_puntaje(self, valor):
        self.puntaje = self.puntaje + valor

    def get_nombre(self):
        return self.nombre

    def get_puntaje(self):
        return self.puntaje
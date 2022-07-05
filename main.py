from sqlite3 import *
import os
from unicodedata import name
from cffi import VerificationError
from peewee import *

os.system('cls')

db = SqliteDatabase('teams.db')


# Creo base de datos
class Equipos(Model):
    name = CharField(unique=True)
    points = IntegerField()

    class Meta:
        database = db


db.connect()
db.create_tables([Equipos])


# Creo las funciones
class Functions():
    # Añade equipos a la base de datos (Máximo 4 y no se puede repetir el nombre)
    def nuevo_equipo(self):
        if (Equipos.select().count()) == 4:
            print('Ya existen 4 equipos en la base de datos, elija otra opción')
        else:
            pass
        while(Equipos.select().count()) < 4:
            nombre_equipo = input(
                "\nIngrese el nombre del equipo: ").capitalize()
            try:
                data = Equipos(name=nombre_equipo, points=0)
                data.save()
            except:
                print('El equipo ingresado ya existe, por favor ingrese otro')
    
    #Realizo enfrentamientos entre equipos
    def agregar_resultado(self):
        
        equipo_uno = input("\nIngrese el equipo uno: ").capitalize()
        while Equipos.get_or_none(Equipos.name == equipo_uno) is None:
            print('Equipo no existente')
            equipo_uno = input("\nIngrese el equipo uno: ").capitalize()
        
        equipo_dos = input("\nIngrese el equipo dos: ").capitalize()
        while Equipos.get_or_none(Equipos.name == equipo_dos) is None:
            print('Equipo no existente')
            equipo_dos = input("\nIngrese el equipo dos: ").capitalize()

        while True:
            opcion = input(f"""
            Indique la opcion correcta:
            1. {equipo_uno} le gano a {equipo_dos}
            2. {equipo_dos} le gano a {equipo_uno}
            3. {equipo_uno} empato con {equipo_dos}
            Opcion: """)
            #Gana equipo 1
            if opcion == "1":
                query = Equipos.select(Equipos.points).where(Equipos.name == equipo_uno)
                for equipo in query:
                    puntaje = equipo.points + 3
                Equipos.update(points=puntaje).where(Equipos.name == equipo_uno).execute()
                print("Resultado agregado con exito!!!")
                return
            #Gana equipo 2
            elif opcion == "2":
                query = Equipos.select(Equipos.points).where(Equipos.name == equipo_dos)
                for equipo in query:
                    puntaje = equipo.points + 3
                Equipos.update(points=puntaje).where(Equipos.name == equipo_dos).execute()
                print("Resultado agregado con exito!!!")
                return
            #Empatan
            elif opcion == "3":
                query = Equipos.select(Equipos.points).where(Equipos.name == equipo_uno)
                for equipo in query:
                    puntaje = equipo.points + 1
                Equipos.update(points=puntaje).where(Equipos.name == equipo_uno).execute()

                query_1 = Equipos.select(Equipos.points).where(Equipos.name == equipo_dos)
                for equipo in query_1:
                    puntaje = equipo.points + 1
                Equipos.update(points=puntaje).where(Equipos.name == equipo_dos).execute()
                print("Resultado agregado con exito!!!")
                return
            else:
                print("Reintentar, valor incorrecto")
    #Muestro los equipos en orden descendente
    def mostrar_posicion(self):
        rows=Equipos.select().order_by(Equipos.points.desc())
        print ("Equipos: ")
        for row in rows:
            print ("{} con {} puntos".format(row.name,row.points))

#Funcion menu
funcion = Functions()
def menu():
    while True:
        opcion = input("""\nIngrese una opcion
        1. Agregar equipo
        2. Agregar resultado
        3. Mostrar posiciones
        4. Salir

        Opcion: """)
        if opcion == "1":
            funcion.nuevo_equipo()
        if opcion == "2":
            funcion.agregar_resultado()
        if opcion == "3":
            funcion.mostrar_posicion()
        if opcion == "4":
            break


menu()
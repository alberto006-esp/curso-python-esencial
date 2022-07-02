from re import T
from typing import Type


class Persona:
    atributo = 123                      # Ejemplo de atributo, se crean fuera del constructor
    def __init__(self, nombre, edad):   # self: esta variable representa la instancia de la clase y a 
         self.nombre = nombre           # traves de ella se pueden acceder a las propiedades y funciones de la clase
         self.edad = edad

    def cumplir_anios(self):            # Ejemplo de metodo del objeto
        self.edad += 1
        print(f"Feliz cumpleaños #{self.edad} {self.nombre}")

paco = Persona("Paco", 20)
print(paco.nombre)
print(paco.edad)

print(paco.atributo)

paco.cumplir_anios()

class Empleado(Persona):                                # Ejemplo de clase hija de persona
    def __init__(self, horas_totales, nombre, edad):    # Al crear un nuevo constructor de la clase hija perdera los atributos de la clase padre
        super(Empleado, self).__init__(nombre, edad)    # Esto nos permitira heredar los atributos de la clase padre
        self.horas_totales = horas_totales

    def trabajar(self, horas_trabajadas):
        self.horas_totales += horas_trabajadas
        print(f"Usted ha trabajado {horas_trabajadas} horas")
        print(f"Horas totales: {self.horas_totales}")

paco = Empleado(nombre="Paco", edad=20, horas_totales=30)
paco.trabajar(horas_trabajadas=8)
paco.cumplir_anios()


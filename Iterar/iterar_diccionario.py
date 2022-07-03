from wsgiref.validate import validator


lenguaje = {
    "nombre": "Python",
    "creador": "Guido van Rossum"
}

for llave in lenguaje: # el indice seran las llaves del diccionario
    print("llave:", llave)
    print("valor", lenguaje[llave])

for elemento in lenguaje.keys():
    print(elemento)

for elemento in lenguaje.values():
    print(elemento)

for llave, valor in lenguaje.items():
    print(llave, valor)

for elemento in lenguaje.items():
    print(elemento)

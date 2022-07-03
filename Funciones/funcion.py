# Funcion sin parámetros
APELLIDO = "Pinto" # variable global podrá ser ejecutada en cualquier parte del código

def funcion():
    print("mi primera función")
    nombre = "Ana" # variable local solo podrá ejecutarse dentro de la función.
    print(nombre , APELLIDO)

funcion()

#Funcion con parámetros
def perimetro_cuadrado(Lado, unidades):
    perimetro = Lado * 4
    print(f"El perimetro es {perimetro} {unidades}")

#Dos maneras de pasar los parámetros a una función
perimetro_cuadrado(25, "metros")
perimetro_cuadrado(Lado=25, unidades="metros")

#Funciones con return
def perimetro_cuadrado(Lado):
    perimetro = Lado * 4
    return perimetro

def area_cuadrado(Lado):
    area = Lado * Lado
    return area

perimetro = perimetro_cuadrado(Lado=5)
area = area_cuadrado(Lado=5)

print(f"Area: {area}, Perímetro: {perimetro}")

def calcular_cuadrado(Lado):# Ejemplo de función que devuelve mas de un valor.
    perimetro = Lado * 4
    area = Lado * Lado
    return perimetro, area

area, perimetro = calcular_cuadrado(Lado=5)# Al devolver más de un valor podremos usar varias variables o una tupla.
resultado = calcular_cuadrado(Lado=5)
print(resultado)

print(f"Area: {area}, Perímetro: {perimetro}")
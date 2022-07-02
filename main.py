from figuras.cuadrado import area_cuadrado, perimetro_cuadrado
from figuras.circulo import area_circulo, perimetro_circulo

lado = 4
cuadrado = {
    "lado": lado,
    "area": area_cuadrado(lado), #Al importar nos permite ejecutar las funciones que contienen
    "perimetro": perimetro_cuadrado(lado)
}

print("cuadrado:", cuadrado)

perimetro = perimetro_cuadrado(lado)
print(perimetro)

radio = 5
circulo = {
    "radio": radio,
    "area": area_circulo(radio),
    "perimetro": perimetro_circulo(radio)
}
print("circulo:", circulo)
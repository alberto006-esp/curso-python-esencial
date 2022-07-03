def calcular_promedio(lista):
    assert len(lista) > 0, "La lista esta vacía" # si no cumple con la condicion el assert provocará una excepción
    return sum(lista) / len(lista)

promedio = calcular_promedio(lista=[1, 3, 5])
print(promedio)
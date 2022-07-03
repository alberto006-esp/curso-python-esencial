from shutil import ExecError


def calcular_promedio(lista):
    assert len(lista) > 0, "La lista esta vacía"
    return sum(lista) / len(lista)

try:
    promedio = calcular_promedio(lista=["texto"])
    print(promedio)
except AssertionError as assert_error:
    print(assert_error)
except Exception as e:
    print("La función no calculó el promedio")
    print(e)
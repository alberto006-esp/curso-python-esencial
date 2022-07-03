for letra in "Texto": # El ciclo for puede recoger un String
    print(letra)

lenguajes = ["python", "java", "golang"]

for elemento in lenguajes: # También sirve para recoger una lista 
    print(elemento)
    if elemento == "java":
        break # Rompe el flujo del ciclo / termina el ciclo for
    

for elemento in lenguajes:
    if elemento == "java":
        continue # Permite saltarse el resto del codigo para pasar al siguiente elemento en la lista
    print(elemento) # solo se imprimiran python y goland
    
for elemento in range(5): # Tambien permite iterar un conjunto de numeros consecutivos con range.
    print(elemento)

for elemento in range(1, 5): # También puede recibir dos números (se imprimiran del 1 al 4, el ultimo numero no se incluye)
    print(elemento)
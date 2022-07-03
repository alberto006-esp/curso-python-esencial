from operator import le


lenguajes = ["python", "java", "golang"]
for elemento in lenguajes: # parecido al for each en java
    print(elemento)

for index in range(len(lenguajes)): # similar al for en java
    print("indice", index) 
    print("elemento", lenguajes[index])

i = 0
while i< len(lenguajes):
    print(lenguajes[i])
    i += 1
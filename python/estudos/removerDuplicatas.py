#Remover duplicados mantendo a ordem original

numeros = [4,2,4,1,2,5,1]
vistos = set()
final = []

for numero in numeros:
    if numero not in vistos:
        vistos.add(numero)
        final.append(numero)

print(final)    
    
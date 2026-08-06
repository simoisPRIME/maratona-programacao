#Encontre o primeiro caracter nao repetido

palavra = "paralelepipedo"

frequencia = {}

for letra in palavra:
    frequencia[letra] = frequencia.get(letra, 0) + 1

for letra in palavra:
    if frequencia[letra] == 1:
        print(letra)
        break


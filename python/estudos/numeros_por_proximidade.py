#Ordene os numeros conforme a distancia ate o valor 10

numeros = [12, 4, 18, 9, 15, 2]
alvo = 10

numeros.sort(key = lambda numero: abs(numero - alvo))

print(numeros)



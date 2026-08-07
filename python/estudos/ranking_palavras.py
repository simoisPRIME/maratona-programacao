# Crie uma lista com as palavras distintas e ordene usando estas regras:
# maior frequência primeiro;
# em caso de empate, menor palavra primeiro;
# persistindo o empate, ordem alfabética.

texto = "python java python c++ java python go c++ rust java python java go go rust c++ python java "
lista = texto.split()
ordenadas = {}

for palavra in lista:
    ordenadas[palavra] = ordenadas.get(palavra, 0) + 1

lista_ordenada = list(ordenadas.items())
lista_ordenada.sort(key=lambda palavra: (-palavra[1], len(palavra[0]), palavra[0]))

print(lista_ordenada)


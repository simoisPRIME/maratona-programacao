# Faça uma matriz que encontre e mostre:
# o maior número;
# o menor número;
# a posição (linha, coluna) de cada um.

matriz = [
    [3,8,4],
    [7,2,1],
    [6,9,5]
]

maior_numero = matriz[0][0] #assumi que o primeiro numero e o menor e maior, depois o for vai corrigindo os valores
menor_numero = matriz[0][0]
endereco_maior = [0, 0]
endereco_menor = [0 ,0]

for i in range(len(matriz)):

    for j in range(len(matriz[i])):

        if matriz[i][j] > maior_numero:
            maior_numero = matriz[i][j]
            endereco_maior = [i, j]
            
        if matriz[i][j] < menor_numero:
            menor_numero = matriz[i][j]
            endereco_menor = [i,j]

print(f"Maior numero da matriz: {maior_numero}")
print(f"Encontrado na posicao ({endereco_maior[0]}, {endereco_maior[1]})")

print(f"\nMenor numero da matriz: {menor_numero}")
print(f"Encontrado na posicao ({endereco_menor[0]}, {endereco_menor[1]})")

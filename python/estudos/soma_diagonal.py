#Na mesma matriz (matriz.py), encontre a soma de todos os elementos da diagonal principal

matriz = [
    [3,8,4],
    [7,2,1],
    [6,9,9]
]

soma = 0

for i in range(len(matriz)): #toda diagonal vai ter as posicoes iguais (0,0) = 3; (1,1) = 2
    j = i
    soma += matriz[i][j]

print(f"Soma da diagonal principal: {soma}")
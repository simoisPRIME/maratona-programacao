#Exercicio onde voce escolhe algum numero da matriz e o sistema retorna os 
# numeros abaixo, acima, a esquerda e a direita do numero digitado

def possivel(matriz, i, j):
    if (i < 0 or i >= len(matriz)) or (j < 0 or j >= len(matriz[i])):
        return False
    
    return True

direcoes = [
    ("Acima", -1, 0),
    ("Abaixo", 1, 0),
    ("Esquerda", 0, -1),
    ("Direita", 0, 1)
]

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("--MATRIZ--\n")
for linha in matriz:
    print(linha)

encontrado = False

while not encontrado:

    numero = int(input("\nDigite um numero da matriz: "))

    for i in range(len(matriz)):

        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:

                encontrado = True
                
                print(f"Valor atual: {numero}")
                for nome, di, dj in direcoes:
                    novo_i = i + di
                    novo_j = j + dj

                    if possivel(matriz, novo_i, novo_j):
                        print(f"{nome}: {matriz[novo_i][novo_j]}")
                    else:
                        print(f"{nome}: -")

                break
        break

    if not encontrado:
        print("Numero nao esta na matriz, digite novamente: ")



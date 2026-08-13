def busca_binaria(alvo, lista):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if alvo == lista[meio]:
            print(f"Alvo encontrado! Valor {alvo} esta no indice {meio}")
            return meio

        elif alvo > lista[meio]: #alvo esta a direita do meio
            inicio = meio + 1

        else: #alvo esta a esquerda do meio
            fim = meio - 1

    print("Alvo nao encontrado!")
    return -1

numeros = [3, 7, 11, 18, 24, 31, 40]
busca_binaria(31, numeros) #retornara "Alvo encontrado! Valor 31 esta no indice 5"
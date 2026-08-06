#Encontrar os valores em comuns presentes nas duas lista
#Usei 2 formas, uma usando 2 for, outra com conjuntos

listaA = [1,2,3,4,5]
listaB = [4,5,6,7,8]
comum = []

for i in listaA:
    for j in listaB:
        if i == j:
            comum.append(i)

print(comum)

conjuntoA = set(listaA)
conjuntoB = set(listaB)

print(conjuntoA & conjuntoB)

#Nos conjuntos poderia usar tambem:
#comumm = set(listaA) & set(listaB)
#print(comumm)
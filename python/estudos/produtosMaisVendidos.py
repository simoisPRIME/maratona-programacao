# Contar quantas vezes cada produto aparece
# Mostrar o produto mais vendido
# Mostrar quantos produtos diferentes foram vendidos

vendas = [
    "Teclado",
    "Mouse",
    "Teclado",
    "Monitor",
    "Mouse",
    "Teclado"
]

vendas_com_quantidade = {}
maior_quantidade = 0
mais_vendido = ""

for produto in vendas:
    vendas_com_quantidade[produto] = vendas_com_quantidade.get(produto, 0) + 1
    if vendas_com_quantidade[produto] > maior_quantidade:
        maior = vendas_com_quantidade[produto]
        mais_vendido = produto

for produto in vendas_com_quantidade:
    print(f"{produto}: {vendas_com_quantidade[produto]}")

print("\nMais vendido: " + mais_vendido)
print("Produtos diferentes: " + str(len(vendas_com_quantidade)))
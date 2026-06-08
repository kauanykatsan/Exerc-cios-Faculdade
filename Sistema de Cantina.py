def calcular_total(preco, quantidade):
    return preco * quantidade

def aplicar_desconto(total):
    return total * 0.9   # 10% de desconto

# programa principal
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade: "))

total = calcular_total(preco, quantidade)
total_com_desconto = aplicar_desconto(total)

print(f"Total: {total}")
print(f"Total com desconto: {total_com_desconto}")
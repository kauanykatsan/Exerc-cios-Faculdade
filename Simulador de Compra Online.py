def calcular_total(preco, quantidade):
    total = preco * quantidade
    return total

def aplicar_desconto(total):
    desconto = total * 0.05
    valor_final = total - desconto
    return valor_final


preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade: "))

total = calcular_total(preco, quantidade)
final = aplicar_desconto(total)

print("Valor final da compra:", final)
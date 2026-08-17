print("=====Bem-vindo ao Calcular de Gorjeta=====")

valor_consumido = float(input("Digite o valor consumido:  "))
taxa = valor_consumido * 0.10

gorjeta = valor_consumido * taxa /100

total=valor_consumido + gorjeta
taxa = valor_consumido + gorjeta

print("Valor Consumido: ", valor_consumido)
print("Total da gorjeta: ", gorjeta)
print("Valor total: ", total)
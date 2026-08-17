def conversao(valor, cotacao, tipo):
    if tipo == 1:
        return valor*cotacao
    else:
        return valor/cotacao


print("Escolha uma opção: ")
print("1-Converter para dólar")
print("2-Converter para Reais")

opcao = int(input("Digite o número da sua escolha:"))
cotacao = 5.40

if opcao == 1:
    valor = float(input("Digite o valor em reais: "))
    resultado = conversao(valor, cotacao,conversao)
    print(f"Valor em dólares: {resultado: .2f}")

elif opcao ==2:
    valor = float(input("Digite o valor em dólares:"))
    resultado = conversao(valor, cotacao, conversao)
    print(f"Valor em reais: {resultado: .2f}")



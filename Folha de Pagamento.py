def salario_liquido(bruto, desconto):
    return bruto - desconto
horas = float(input("Digite todas as horas trabalhadas: "))

valor_hora = float(input("Digite o valor da hora: "))

bruto = salario_bruto(horas, valor_hora)
desconto = calcular_desconto(bruto)
liquido = salario_liquido(bruto, desconto)

print(f"Salário Bruto: {bruto}")
print(f"Desconto: {desconto}")
print(f"Salário Líquido: {liquido}")
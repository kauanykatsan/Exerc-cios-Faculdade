soma = 0

numero = int(input("Digite um número (0 para sair): "))

while numero != 0:
    soma = soma + numero
    numero = int(input("Digite um número (0 para sair): "))

print(f"Soma total: {soma}")
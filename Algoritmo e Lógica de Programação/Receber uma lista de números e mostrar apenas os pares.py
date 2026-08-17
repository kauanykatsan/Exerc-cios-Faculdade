numero = []
pares = []

for tabela in range(7):
    n = int(input("Digite um número: "))
    numero.append(n)

    if n % 2 == 0:
        pares.append(n)

print("Números selecionados:", numero)
print("Números Pares:", pares)

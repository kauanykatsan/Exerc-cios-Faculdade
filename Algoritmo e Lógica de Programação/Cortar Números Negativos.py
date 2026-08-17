n = int(input("Quantos números? "))
numeros = []

for i in range(n):
    num = int(input(f"Digite o número {i+1}: "))
    numeros.append(num)

contador = 0

for numero in numeros:
    if numero < 0:
        contador += 1

print(f"Quantidade de negativos: {contador}")

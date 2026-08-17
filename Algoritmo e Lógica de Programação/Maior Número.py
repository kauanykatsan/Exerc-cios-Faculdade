n = int(input("Quantos números? "))
numeros = []

for i in range(n):
    num = int(input(f"Digite o número {i+1}: "))
    numeros.append(num)

maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero

print(f"O maior valor é: {maior}")

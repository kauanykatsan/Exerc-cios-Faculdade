def par_ou_impar(numero):
    if numero % 2 ==0:
        return "PAR"
    else:
        return"IMPAR"

numero = float(input("Digite um número: "))

resultado = par_ou_impar(numero)

print(f"O número {numero} é {resultado}!")

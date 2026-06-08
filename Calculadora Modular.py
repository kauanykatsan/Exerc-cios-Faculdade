def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b


n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print("Soma:", soma(n1, n2))
print("Subtração:", subtracao(n1, n2))
print("Multiplicação:", multiplicacao(n1, n2))
print("Divisão:", divisao(n1, n2))
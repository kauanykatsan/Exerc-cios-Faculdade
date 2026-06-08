def calcular_media(n1, n2, n3, n4):
    media = (n1 + n2 + n3 + n4) / 4
    return media

def verificar_aprovacao(media):
    if media >= 8:
        return "Aprovado"
    else:
        return "Reprovado"


nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = calcular_media(nota1, nota2, nota3, nota4)
situacao = verificar_aprovacao(media)

print("Nome:", nome)
print("Média:", media)
print("Situação:", situacao)
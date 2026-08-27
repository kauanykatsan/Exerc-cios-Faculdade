tam = 10  #definir o tamanho da lista 

#Cadastrar os valores
def CadastrarVetor(V, N):  
    for i in range(N):   # se N vale 10 o I assumira que terá 10 posições
        V[i] = int(input(f"Digite o valor da posição {i}: "))   # o número vai ser colocado em V{i}

#vai mostrar as posições o os valores
def MostrarVetor(V, N):
    for i in range(N):
        print(f"Posição {i}: {V[i]}")  #i mostra a posição  - {v[i]} mostra o valor da posição

#vai procurar e substituir valores
def AlterarVetor(V, N, procurado, novo):
    alteracoes = 0  #contara quantas substituições foram realizadas

    for i in range(N):
        if V[i]== procurado:    #compara valores
            V[i]=novo
            alteracoes = alteracoes + 1
    return alteracoes


while True:
    #cria a lista com as 10 posições
    vet = [0] * tam

    #cadastra
    CadastrarVetor(vet, tam)

    #mostrar
    print("Vetor Cadastrado: ")
    MostrarVetor(vet, tam)

    #pedir valores
    procurado = int(input("Digite o valor que deseja procurar: "))
    novo= int(input("Digite o novo valor: "))

    #altarar a lista
    quantidade = AlterarVetor(vet, tam, procurado, novo)


    #mostrar mensagem correspondente
    if quantidade > 0:
        print(f"Foram alterados {quantidade} posições")
    else:
        print(f"O valor não foi encontrado. Nenhma posição alterada")

    #mostrar lista alterada
    print("Vetor após as alterações: ")
    MostrarVetor(vet, tam)

    #continuar rodando o programa
    continuar = input("Deseja executar novamente? (S/N): ")

    if continuar == "N" or continuar == "n":
        print("Encerrando programa...")
        break

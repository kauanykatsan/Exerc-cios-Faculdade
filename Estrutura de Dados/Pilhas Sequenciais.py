# ===========================================================
# Atividade - Pilha Sequencial (baseada em vetor)
# Esqueleto de codigo em Python - ClassePilha
#
# Assim como fizemos com a ClasseLista, os dados (Pilha e Topo)
# ficam DENTRO do objeto (atributos self.Pilha e self.Topo), e
# os metodos NAO precisam receber Pilha/Topo por parametro -
# cada metodo ja enxerga os atributos do proprio objeto (via
# self).
#
# Regras (lembrete da apostila):
# - A pilha tem tamanho fixo de 10 posicoes (TAMANHO): mesmo em
#   Python, trate-a como um vetor de tamanho fixo, controlando
#   manualmente self.Topo. Nao deixe a lista crescer sozinha.
# - Proibido usar recursao.
# - Proibido usar metodos prontos de lista (append, pop, insert,
#   remove, del, extend, sort, etc.) - a logica deve ser escrita
#   manualmente, com self.Pilha[indice] = valor.
# - So se acessa o TOPO da pilha - nao existe "inserir/remover
#   do meio" aqui (essa e a diferenca para a ClasseLista).
# - Os metodos abaixo devem seguir exatamente as assinaturas e
#   o comportamento descritos nos comentarios.
# - O bloco "while opcao" ja esta pronto com o menu interativo -
#   voce so precisa completar o corpo de cada metodo (onde esta
#   escrito "TODO"). Nao altere as chamadas dentro do menu.
# ===========================================================

TAMANHO = 10


class ClassePilha:
    # -----------------------------------------------------------
    # Construtor
    #
    # Roda automaticamente quando um objeto ClassePilha e criado
    # (ex: "pilha = ClassePilha()"). Sem essa instanciacao,
    # nenhum metodo abaixo poderia ser chamado - nao existiria
    # "pilha" para chamar pilha.Empilha(...), por exemplo.
    #
    # Ja faz o papel do InicializaPilha() da apostila.
    # -----------------------------------------------------------
    def __init__(self):
        self.Pilha = [0] * TAMANHO
        self.Topo = -1

    # -----------------------------------------------------------
    # PilhaVazia
    # Entradas: nenhuma (usa o self.Topo do proprio objeto)
    # Retorno: 1 se a pilha estiver vazia (self.Topo == -1),
    #          senao 0
    #
    # TODO: implemente a verificacao acima.
    # -----------------------------------------------------------
    def PilhaVazia(self):
        if self.Topo == -1:
            return 1
        else:
            return 0


    # -----------------------------------------------------------
    # PilhaCheia
    # Entradas: nenhuma (usa o self.Topo do proprio objeto)
    # Retorno: 1 se a pilha estiver cheia
    #          (self.Topo == TAMANHO - 1), senao 0
    #
    # TODO: implemente a verificacao acima.
    # -----------------------------------------------------------
    def PilhaCheia(self):
        if self.Topo == TAMANHO -1:
            return 1
        else: 
            return 0
    # -----------------------------------------------------------
    # Empilha (push)
    # Entradas: VALOR a inserir
    # Efeito: incrementa self.Topo em 1 e escreve VALOR na
    #         posicao self.Topo da self.Pilha
    # Retorno: nada
    #
    # Lembrete: use self.PilhaCheia() antes de empilhar. Se nao
    # houver espaco, nao insira nada (apenas avise o erro).
    # Repare que, diferente da ClasseLista, aqui NENHUM outro
    # elemento precisa ser deslocado.
    #
    # TODO: implemente a insercao.
    # -----------------------------------------------------------
    def Empilha(self, VALOR):
        if self.PilhaCheia():
            print("Pilha Cheia!")
        else:
            self.Topo = self.Topo+1
            self.Pilha[self.Topo] = VALOR

    # -----------------------------------------------------------
    # Desempilha (pop)
    # Entradas: nenhuma
    # Efeito: le o valor da posicao self.Topo e decrementa
    #         self.Topo em 1
    # Retorno: o VALOR que foi removido
    #
    # Lembrete: use self.PilhaVazia() antes de desempilhar. Se
    # a pilha estiver vazia, nao remova nada (apenas avise o
    # erro) - defina o que o metodo retorna nesse caso.
    # Repare que, diferente da ClasseLista, aqui NENHUM outro
    # elemento precisa ser deslocado.
    #
    # TODO: implemente a remocao.
    # -----------------------------------------------------------
    def Desempilha(self):
        if self.PilhaVazia():
            print("Pilha Vazia!")
            return -111

        else: 
            VALOR =self.Pilha[self.Topo]
            self.Topo = self.Topo -1
            return VALOR

    # -----------------------------------------------------------
    # TopoPilha
    # Entradas: nenhuma
    # Efeito: nenhum - APENAS consulta, nao remove nada
    # Retorno: o VALOR que esta na posicao self.Topo
    #
    # Lembrete: use self.PilhaVazia() antes de consultar. Se a
    # pilha estiver vazia, nao ha topo para retornar - defina o
    # que o metodo retorna nesse caso.
    #
    # TODO: implemente a consulta.
    # -----------------------------------------------------------
    def TopoPilha(self):
        if self.PilhaVazia():
            print("Pilha Vazia!")
        else:
            return self.Pilha[self.Topo]
            
        return -1

    # -----------------------------------------------------------
    # MostrarPilha
    # Entradas: nenhuma
    # Efeito: exibe na tela os valores ocupados da self.Pilha,
    #         do indice 0 ate self.Topo
    # Retorno: nada
    #
    # Lembrete: se a pilha estiver vazia, exiba uma mensagem
    # adequada em vez de uma pilha vazia entre colchetes. Dica:
    # ao exibir, deixe claro qual elemento e o topo (ex.: uma
    # seta ou um texto ao lado do ultimo valor impresso).
    #
    # TODO: implemente a exibicao.
    # -----------------------------------------------------------
    def MostrarPilha(self):
        if self.PilhaVazia():
            print("Sua Pilha está vazia.")
        else:
            for i in range(self.Topo +1):
             if i == self.Topo:
                print(self.Pilha[i], "<---Topo")
            else:
                print(self.Pilha[i])
       


# ===========================================================
# Programa principal - menu interativo
#
# Em vez de um roteiro de teste fixo, o programa apresenta um
# menu de opcoes e repete a pergunta ate o usuario escolher
# sair (opcao 0). Cada opcao chama um metodo do objeto "pilha".
#
# Repare que este bloco NAO esta dentro de uma funcao (sem
# "def main"): e codigo direto, executado de cima para baixo
# assim que o arquivo roda - o mesmo estilo usado na atividade
# de listas.
#
# NAO ALTERE a estrutura do menu abaixo. Complete apenas os
# metodos da classe (onde esta escrito "TODO").
#
# Repare que nenhuma chamada precisa passar Pilha ou Topo: o
# objeto "pilha" ja guarda esses dados internamente.
# ===========================================================

# Instanciacao do objeto: e aqui que o construtor (__init__)
# roda e cria a pilha vazia (Topo = -1). Sem esta linha, nao
# haveria "pilha" para chamar os metodos abaixo.
pilha = ClassePilha()

opcao = -1

while opcao != 0:
    print("\n===== MENU =====")
    print("1 - Empilhar (push)")
    print("2 - Desempilhar (pop)")
    print("3 - Consultar o topo (sem remover)")
    print("4 - Mostrar pilha")
    print("0 - Sair")
    opcao = int(input("Escolha uma opcao: "))


    if opcao == 1:
        valor = int(input("Digite o valor a empilhar: "))
        pilha.Empilha(valor)
        pilha.MostrarPilha()
    elif opcao == 2:
        valorRemovido = pilha.Desempilha()
        print("Valor desempilhado: %d" % valorRemovido)
        pilha.MostrarPilha()
    elif opcao == 3:
        print("Valor do topo: %d" % pilha.TopoPilha())
    elif opcao == 4:
        pilha.MostrarPilha()
    elif opcao == 0:
        print("Encerrando programa...")
    elif opcao !=0:
        print("Opcao invalida")
        
        
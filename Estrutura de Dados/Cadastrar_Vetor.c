/*Nunca programei em C então tentei fazer
 de um jeito que ficaria mias facil para
  eu entendenter*/

///EXERCÍCIO 
#include <stdio.h> ///Avisa o C que vai usar comandos de entrada e saída: prinf, scanf
#define TAM 10 ///sempre que aparecer TAM ele substitui por 10
/*
CadastrarVetor(V, N) — lê do teclado os N valores do vetor.
Não possui return.
*/

void cadastrarVetor(int V[], int N) 
{
    int i; ///cria a variável i
    for (i=0; i < N; i++)///laço de repetição
    {
        printf("Digite o valor da posição %d: ", i);
        scanf("%d", &V[i]);
    }
}


/*
MostrarVetor(V, N)
exibe o conteúdo do vetor, indicando a posição e o valor.
 Não possui return.
*/

void mostrarVetor(int V[], int N)
{
    int i;
    for(i=0; i < N; i++) ///\n quebra de linha - %d valores - 
        printf("V[%d] = %d\n", i, V[i]);
}

/*
AlterarVetor(V, N, procurado, novo) 
Percorre o vetor procurando o valor procurado e, em cada 
posição onde encontrar, substitui pelo valor novo. 
A função retorna a quantidade de alterações realizadas.
*/

int alterarVetor(int V[], int N, int procurando, int novo )
{
    int i;
    int contador=0; ///variavel para contar quantas x trocamos algo(começando do 0)
    for(i=0; i<N; i++)
    {
        if (V[i] ==procurando) ///comparação de valores (== comparação)
        {
            V[i] = novo; ///se v[i]=novo, troca o valor aquela posição
            contador++; ///soma 1 no cantador
        }
    }
    return(contador);
}

int main() ///onde o programa começa a rodae
{
    int VET[TAM]; ///cria o vetor de verdade, 10 posições vazias
    int N = TAM; ///guarda o tamanho em uma variável N
    int procurando, novo, quantidade; ///3 variáveis inteiras declaradas de uma vez
    /*toda variavel precisa ser declarada antes de ser usada, para o computador saber:
    quanto espaçço precisa ser reservado na memória e que tipo de dado que é */

    ///Cadastrar
    printf("Cadastro de Vetor: \n");
    cadastrarVetor(VET, N); /*a funçao vai receber o endereço de VET
    então quando escrever em V[I] lá dentro, na vdd está escrevendo direto no VET do main
    */


    ///Mostrar
    printf("Vetor cadastrado \n");
    mostrarVetor(VET, N);


    ///Solicitar ao usuário o valor a ser procurado e o valor novo
    printf("\nDigie o valor a ser procurando: ");
    scanf("%d", &procurando); /// le dois numeros simples digitados pelo usuario
    printf("Digite o valor novo: ");
    scanf("%d", &novo);

/*  chamar a função de alteração e,
     com base no que ela retornou, 
     exibir uma das duas mensagens abaixo */

    quantidade= alterarVetor(VET, N, procurando, novo); /*chama a variável de alterar,
     e guarda quantas trocas form feitar na variável: quantidade*/
    if(quantidade == 0)
        printf(" \nO valor nao foi encontrado. Nenhuma posicao foi alterada \n");
    else
        printf("\nForam alteradas %d posições \n", quantidade);
                    /*Decide qual mensagem mostrar*/

    ///Em seguida, mostrar o vetor novamente
    printf("\nVetor após alterações: \n");
    mostrarVetor(VET, N);

    return(0);  ///todo main termina com isso. Diz: o programa terminou sem erro
}
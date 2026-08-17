#include <stdio.h>

float Conversao(int tipo, float valor, float cotacao)
{
    if(tipo == 1)
    {
        return valor * cotacao;
    }
    else
    {
        return valor / cotacao;
    }
}

int main()
{
    int tipo;
    float valor, cotacao, resultado;

    printf("Digite a cotação de hoje: ");
    scanf("%f", &cotacao);

    printf("\nEscolha uma opção: \n");
    printf("1-Converter dólar para reais\n");
    printf("2-Converter reais para dólares\n");
    scanf("%d", &tipo);
    if (tipo == 1)
    {
        printf("Digite o valor em dólares: ");
        scanf("%f", &valor);

        resultado = Conversao(tipo, valor, cotacao);

    
        printf("Valor em reais: %.2f\n", resultado);
    }
    else if(tipo ==2)
    {
        printf("Digte o valor de reais: ");
        scanf("%f", &valor);

        resultado = Conversao(tipo, valor, cotacao);

        printf("Valor em dólares: %.2f\n", resultado);
    }
    
    return 0;
}
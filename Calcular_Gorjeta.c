#include <stdio.h>

void CalcularGorjeta (float valor, float taxa) 
 //void mostra o resultado dentro dela 
{
    float gorjeta, total;

    gorjeta = valor * taxa;
    total = valor + gorjeta;

    printf("Valor consumido: %.2f\n", valor);
    printf("Taxa da Gorjeta: %.0f%%\n", taxa *100);
    printf("Valor da gorjeta: , %.2f\n", gorjeta);
    printf("Valor Total: %.2f\n", total);
}
int main()
{
    float valor; 
    float taxa = 0.10;

    printf("Digite o valor consumido: ");
    scanf("%f", &valor);

    CalcularGorjeta(valor, taxa);

    return 0;
}
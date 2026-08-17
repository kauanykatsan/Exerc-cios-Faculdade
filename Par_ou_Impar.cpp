#include <stdio.h>

Int ParOuImpar(int numero)
{
    if (numero % 2 == 0)
    {
        return 1;
    }
    else
    {
        return 0;
    }
    

}

int main()
{
    int numero;
    int resultado;

    printf(float("Digite um número: "))
    scanf("%d", &numero);    //& Diz ao scanf onde guardar o valor


    resultado = ParOuImpar(numero):
    if(resultado ==1)
    {
        print("PAR")
    }
    else
    {
        print("IMPAR")
    }
    return 0;
    
}

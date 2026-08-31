#include <stdio.h>

struct Cliente {
    int codigo;
    char nome[50];
};

int main() {
    struct Cliente clientes[10];
    int i;

    // Cadastro dos 10 clientes
    for (i = 0; i < 10; i++) {
        printf("\nCliente %d\n", i + 1);

        printf("Digite o codigo: ");
        scanf("%d", &clientes[i].codigo);

        printf("Digite o nome: ");
        scanf(" %49[^\n]", clientes[i].nome);
    }

    // Exibição dos clientes
    printf("\nCODIGO\tNOME\n");

    for (i = 0; i < 10; i++) {
        printf("%d\t%s\n",
               clientes[i].codigo,
               clientes[i].nome);
    }

    return 0;
}
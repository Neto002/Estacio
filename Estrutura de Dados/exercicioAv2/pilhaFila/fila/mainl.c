#include <stdio.h>
#include <stdlib.h>
#include "oL.h"

int main() {
    node *FILA = (node*)malloc(sizeof(node));
    FILA->prox = NULL;
    tam = 0;

    int escolha;
    int valor = 0;

    while (1==1) {
        printf("-----------------------------------------------------------\n");
        printf("Digite a opcao desejada:\n1 - Inserir\n2 - Remover\n3 - Imprimir\n4 - Buscar valor\n5 - Esvaziar fila\n6 - Maior valor\n0 - Sair\nSua escolha: ");
        scanf("%d", &escolha);

        if (escolha == 0) {
            printf("Encerrando...\n");
            break;
        }

        switch(escolha) {
            case 1:
                printf("Digite o valor a ser inserido: ");
                scanf("%d", &valor);
                ENQUEUE(FILA, valor);
                valor = 0;
                break;
            case 2:
                DEQUEUE(FILA);
                break;
            case 3:
                IMPRIME(FILA);
                break;
            case 4:
                printf("Digite o valor que deseja BUSCA: ");
                scanf("%d", &valor);
                BUSCA(FILA, valor);
                valor = 0;
                break;
            case 5:
                esvaziar(FILA);
                printf("Fila esvaziada\n");
                break;
            case 6:
                printf("Maior valor da pilha: %d\n", MAIOR(FILA));
                break;
            default:
                printf("Opcao invalida!\n\n");
        }
    }

    free(FILA);
    return 0;
}
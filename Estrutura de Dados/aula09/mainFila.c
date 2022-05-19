#include <stdio.h>
#include <stdlib.h>
#include "operacoesFila.h"

int main() {
    no *fila;
    inicializar(fila);

    int escolha;
    int valor = 0;

    while (escolha != 0) {
        printf("-----------------------------------------------------------\n");
        printf("Digite a opcao desejada:\n1 - Inserir\n2 - Remover\n3 - Imprimir\n4 - Buscar valor\n5 - Esvaziar fila\n0 - Sair\nSua escolha: ");
        scanf("%d", &escolha);
        
        switch(escolha) {
            case 0:
                printf("Encerrando...\n");
                break;
            case 1:
                printf("Digite o valor a ser inserido: ");
                scanf("%d", &valor);
                enqueue(fila, valor);
                valor = 0;
                break;
            case 2:
                dequeue(fila);
                break;
            case 3:
                imprimir(fila);
                break;
            case 4:
                printf("Digite o valor que deseja buscar: ");
                scanf("%d", &valor);
                buscar(fila, valor);
                valor = 0;
                break;
            case 5:
                esvaziar(fila);
                printf("Fila esvaziada\n");
                break;
            default:
                printf("Opcao invalida!\n\n");
        }
    }

    return 0;
}
#include <stdio.h>
#include <stdlib.h>

int fila[];
int tamanho;
int *inicio;
int *final;

int vazia(int fila[]) {
    if (fila == NULL) {
        return 1;
    } else {
        return 0;
    }
}

void enqueue(int fila[], int valor) {
    if (fila == NULL) {
        inicio = valor;
    } else {
        for (int i = 0; i < tamanho; i++) {
            if (fila[i] == NULL) {
                fila[i] = valor;
                break;
            }
        }
    }
}

void dequeue(int fila[]) {
    if (fila == NULL) {
        printf("Fila vazia\n");
    } else {
        for (int i = 0; i < tamanho; i++) {
            *inicio = NULL;
            inicio = fila[i+1];
            break;
        }
    }
}

void imprimir(int fila[]) {
    for (int i = 0; i < tamanho; i++) {
        if (fila[i] != NULL) {
            printf("%3d", fila[i]);
        }
    }
    printf("\nTamanho da fila: %d\n", tamanho);
}

void buscar(int fila[], int valor) {
    for (int i = 0; i < tamanho; i++) {
        if (fila[i] == valor) {
            printf("%d encontrado\n", valor);
            break;
        } else if (fila[i] != valor && i == 4) {
            printf("%d nao encontrado\n", valor);
        }
    }
}

void esvaziar(int fila[]) {
    for (int i = 0; i < tamanho; i++) {
        fila[i] = NULL;
    }
}

void menu() {
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
                break;
            case 5:
                esvaziar(fila);
                printf("Fila esvaziada\n");
                break;
            default:
                printf("Opcao invalida!\n\n");
        }
    }
}

int main () {


    printf("Tamanho desejado da fila: ");
    scanf("%d", &tamanho);
    

    fila[tamanho];
    inicio = &fila[0];
    final = &fila[tamanho-1];
    
    for (int i = 0; i < tamanho; i++) {
        fila[i] = NULL;
    }

    menu();

    return 0;
}
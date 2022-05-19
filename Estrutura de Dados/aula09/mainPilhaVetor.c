#include <stdio.h>
#include <stdlib.h>

int pilha[];
int tamanho;
int *fundo = &pilha[0];

int vazia(int pilha[]) {
    if (pilha == NULL) {
        return 1;
    } else {
        return 0;
    }
}

void push(int pilha[], int valor) {
    if (pilha == NULL) {
        fundo = valor;
    } else {
        for (int i = 0; i < tamanho; i++) {
            if (pilha[i] == NULL) {
                pilha[i] = valor;
                break;
            }
        }
    }
}

void pop(int pilha[]) {
    if (pilha == NULL) {
        printf("Pilha vazia\n");
    } else {
        for (int i = 0; i < tamanho; i++) {
            if (pilha[i+1] == NULL) {
                pilha[i] = NULL;
                break;
            }
        }
    }
}

void imprimir(int pilha[]) {
    for (int i = 0; i < tamanho; i++) {
        if (pilha[i] != NULL) {
            printf("%3d", pilha[i]);
        }
    }
    printf("\nTamanho da pilha: %d\n", tamanho);
}

void buscar(int pilha[], int valor) {
    for (int i = 0; i < tamanho; i++) {
        if (pilha[i] == valor) {
            printf("%d encontrado\n", valor);
            break;
        } else if (pilha[i] != valor && i == 4) {
            printf("%d nao encontrado\n", valor);
        }
    }
}

void esvaziar(int pilha[]) {
    for (int i = 0; i < tamanho; i++) {
        pilha[i] = NULL;
    }
}

void menu() {
    int escolha;
    int valor = 0;
    while (escolha != 0) {
        printf("-----------------------------------------------------------\n");
        printf("Digite a opcao desejada:\n1 - Inserir\n2 - Remover\n3 - Imprimir\n4 - Buscar valor\n5 - Esvaziar pilha\n0 - Sair\nSua escolha: ");
        scanf("%d", &escolha);
        
        switch(escolha) {
            case 0:
                printf("Encerrando...\n");
                break;
            case 1:
                printf("Digite o valor a ser inserido: ");
                scanf("%d", &valor);
                push(pilha, valor);
                break;
            case 2:
                pop(pilha);
                break;
            case 3:
                imprimir(pilha);
                break;
            case 4:
                printf("Digite o valor que deseja buscar: ");
                scanf("%d", &valor);
                buscar(pilha, valor);
                break;
            case 5:
                esvaziar(pilha);
                printf("Pilha esvaziada\n");
                break;
            default:
                printf("Opcao invalida!\n\n");
        }
    }
}

int main () {

    printf("Tamanho desejado da pilha: ");
    scanf("%d", &tamanho);

    pilha[tamanho];
    
    for (int i = 0; i < tamanho; i++) {
        pilha[i] = NULL;
    }
    
    menu();

    return 0;
}
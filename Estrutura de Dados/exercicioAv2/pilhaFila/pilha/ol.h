#include <stdio.h>
#include <stdlib.h>

struct Node {
    int conteudo;
    struct Node *prox;
};
typedef struct Node node;

int tam;

int vazia(node *PILHA) {
    if(PILHA->prox == NULL) {
        return 1;
    } else {
        return 0;
    }
}

void PUSH(node *PILHA) {
    node *novo = (node*)malloc(sizeof(node));
    novo->prox = NULL;
    
    printf("Novo item: ");
    scanf("%d", &novo->conteudo);
    
    if(vazia(PILHA)) {
        PILHA->prox = novo;
    } else {
        node *tmp = PILHA->prox;
        while(tmp->prox != NULL) {
            tmp = tmp->prox;
        }
        tmp->prox = novo;
    }
    tam++;
}

void POP(node *PILHA) {
    if (vazia(PILHA)) {
        printf("PILHA ja vazia!\n\n");
        return;
    } else {
        node *ultimo = PILHA->prox;
        node *penultimo = PILHA;
        
        while(ultimo->prox != NULL) {
            penultimo = ultimo;
            ultimo = ultimo->prox;
        }
        free(ultimo);
        penultimo->prox = NULL;
        tam--;
    }
}

void IMPRIME(node *PILHA) {
    if (vazia(PILHA)) {
        printf("PILHA vazia!\n\n");
        return;
    }
    node *tmp;
    tmp = PILHA->prox;
    printf("\nPILHA:");
    while(tmp != NULL) {
        printf("%3d", tmp->conteudo);
        tmp = tmp->prox;
    }
    printf("\nQtde itens PILHA: %d", tam);
    printf("\n");
}

void IMPRIMETOPO(node *PILHA) {
    if (vazia(PILHA)) {
        printf("Pilha vazia!\n\n");
        return;
    }
    node *tmp;
    tmp = PILHA->prox;
    while (tmp->prox != NULL) {
        tmp = tmp->prox;
    }
    printf("\nTopo da PILHA: %d\n", tmp->conteudo);
}

void BUSCA(node *PILHA, int itemBusca) {
    if (vazia(PILHA)) {
        printf("Pilha vazia!\n\n");
        return;
    }
    
    node *tmp;
    tmp = PILHA->prox;
    
    while(tmp != NULL) {
            
        if (tmp->conteudo == itemBusca) {
            printf("\nO numero %d existe na PILHA\n", itemBusca);
            return;
        }
        tmp = tmp->prox;
    }
    printf("\nO numero %d nao existe na PILHA\n", itemBusca);
}

void ESVAZIA(node *PILHA) {
    if (vazia(PILHA)) {
        printf("A PILHA ja esta vazia!\n\n");
        return;
    }

    node *aux;
    aux = PILHA->prox;

    while(aux != NULL) {
        node *noRemove = aux;
        aux = aux->prox;
        free(noRemove);
    }
}
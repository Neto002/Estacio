#include <stdio.h>
#include <stdlib.h>

struct Node {
    int conteudo;
    struct Node *prox;
};

typedef struct Node node;
int tam;

int EMPTY(node *FILA) {
    if(FILA->prox == NULL) {
        return 1;
    } else {
        return 0;
    }
}

void ENQUEUE(node *FILA) {
    node *novo = (node*)malloc(sizeof(node));
    novo->prox = NULL;

    printf("Novo item da Fila: ");
    scanf("%d", &novo->conteudo);

    if (EMPTY(FILA)) {
        FILA->prox = novo;
    } else {
        node *tmp = FILA->prox;
        while(tmp->prox != NULL) {
            tmp = tmp->prox;
        }
        tmp->prox = novo;
    }
    tam++;
}

void DEQUEUE(node *FILA) {
    if (EMPTY(FILA)) {
        printf("Fila esta vazia\n");
        return;
    } else {
        node *tmp = FILA->prox;
        FILA->prox = tmp->prox;
        tam--;
        free(tmp);
    }
}

void IMPRIME(node *FILA) {
    if (EMPTY(FILA)) {
        printf("Fila vazia!\n\n");
        return;
    } else {
        node *tmp;
        tmp = FILA->prox;
        printf("\nFILA:");
        while(tmp != NULL) {
            printf("%3d", tmp->conteudo);
            tmp = tmp->prox;
        }
        printf("\nQuantidade de itens da FILA: %d\n", tam);
    }
}

void BUSCA(node *FILA, int item) {
    if (EMPTY(FILA)) {
        printf("Fila vazia!\n\n");
        return;
    } else {
        node *tmp;
        tmp = FILA->prox;
        while(tmp != NULL) {
            if (tmp->conteudo == item) {
                printf("\nO numero %d existe na FILA\n", item);
                return;
            }
            tmp = tmp->prox;
        }
        printf("\nO numero %d nao existe na FILA\n", item);
    }
}

node* MAIOR(node *FILA) {
    node *maior = FILA->prox;

    if (EMPTY(FILA)) {
        printf("Fila vazia!\n\n");
        return;
    } else {
        node *tmp;
        tmp = FILA->prox;
        while(tmp != NULL) {
            if (tmp->conteudo > maior->conteudo) {
                maior = tmp;
            }
            tmp = tmp->prox;
        }
    }
    return maior->conteudo;
}

void esvaziar(node *FILA) {
    if (EMPTY(FILA)) {
        printf("A FILA ja esta vazia!\n\n");
        return;
    } else {
        node *atual;
        node *proxNo;
        atual = FILA->prox;

        while(atual != NULL) {
            proxNo = atual->prox;
            free(atual);
            atual = proxNo;
        }
    }
}
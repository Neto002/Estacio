#include <stdio.h>
#include <stdlib.h>

typedef struct no {
    int item;
    struct no *esquerda, *direita;
} No;

typedef struct {
    No *raiz;
    int tamanho;
} ArvB;

No* inserir(No *raiz, int valor) {
    if (raiz == NULL) {
        No *novo = (No*) malloc(sizeof(No));
        novo->item = valor;
        novo->esquerda = NULL;
        novo->direita = NULL;
        return novo;
    } else {
        if (valor < raiz->item)
            raiz->esquerda = inserir(raiz->esquerda, valor);
        if (valor > raiz->item)
            raiz->direita = inserir(raiz->direita, valor);
        return raiz;
    }
}

void imprimirInOrdem(No *raiz) {
    if (raiz != NULL) {
        imprimirInOrdem(raiz->esquerda);
        printf("%d ", raiz->item);
        imprimirInOrdem(raiz->direita);
    }
}

void imprimirPreOrdem(No *raiz) {
    if (raiz != NULL) {
        imprimirPreOrdem(raiz->direita);
        printf("%d ", raiz->item);
        imprimirPreOrdem(raiz->esquerda);
    }
}

// 1 para valor existente e 0 para valor inexistente na Árvore
int buscar(No *raiz, int item) {
    if (raiz == NULL) {
        return 0;
    } else {
        if (raiz->item == item) {
            return 1;
        } else {
            if (item < raiz->item) {
                buscar(raiz->esquerda, item);
            } else if (item > raiz->item) {
                buscar(raiz->direita, item);
            }
        }
    }
}

No* remover(No *raiz, int item) {
    if (raiz == NULL) {
        printf("Valor nao encontrado!");
        return NULL;
    } else {
        if (raiz->item == item) {
            if(raiz->esquerda == NULL && raiz->direita == NULL) {
                free(raiz);
                return NULL;
            } else {
                if (raiz->esquerda == NULL || raiz->direita == NULL) {
                    No *aux;
                    if (raiz->esquerda != NULL) {
                        aux = raiz->esquerda;
                    } else {
                        aux = raiz->direita;
                    }
                    free(raiz);
                    return aux;
                } else {
                    No *aux = raiz->esquerda;
                    while (aux->direita != NULL) {
                        aux = aux->direita;
                    }
                    raiz->item = aux->item;
                    aux->item = item;
                    raiz->esquerda = remover(raiz->esquerda, item);
                    return raiz;
                }
            }
        } else {
            if (item < raiz->item) {
                raiz->esquerda = remover(raiz->esquerda, item);
            } else {
                raiz->direita = remover(raiz->direita, item);
            }
            return raiz;
        }
    }
}
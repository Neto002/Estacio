#include <stdio.h>
#include <stdlib.h>

#define TAMANHO 5

typedef struct Fila {
    int itens[TAMANHO];
    int final;
} Fila;

void inicializar(Fila *fila) {
    for (int i = 0; i < TAMANHO; i++) {
        fila->itens[i] = 0;
    }
    fila->final = 0;
}

void enqueue(Fila *fila, int valor) {
    if (fila->final == TAMANHO) {
        printf("Fila cheia!\n\n");
        return;
    } else {
        fila->itens[fila->final] = valor;
        fila->final++;
    }
}

void dequeue(Fila *fila) {
    if (fila->final == 0) {
        printf("Fila vazia!\n\n");
        return;
    } else {
        for (int i = 0; i < TAMANHO; i++) {
            fila->itens[i] = fila->itens[i+1];
            fila->final--;
        }
    }
}

void imprimir(Fila *fila) {
    printf("\nFila:\n");
    for (int i = 0; i < TAMANHO; i++) {
        printf("%3d", fila->itens[i]);
    }
    printf("\n\n");
}

void buscar(Fila *fila, int valor) {

}

void maiorValor(Fila *fila) {

}

void esvaziar(Fila *fila) {

}

int main() {
    Fila *fila;
    enqueue(&fila, 1);
    enqueue(&fila, 2);
    enqueue(&fila, 3);
    enqueue(&fila, 4);
    enqueue(&fila, 5);
    imprimir(&fila);

    return 0;
}
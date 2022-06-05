#include <stdio.h>
#include <stdlib.h>

int main() {
    int tam, *v;
    int temp = 0;

    printf("Tamanho do vetor: ");
    scanf("%d", &tam);
    v = (int*)malloc(tam * sizeof(int));

    for (int i = 0; i < tam; i++) {
        printf("Digite um valor para o vetor: ");
        scanf("%d", &v[i]);
    }

    for (int j = tam-1; j > 1; j--) {
        for (int i = 0; i < tam-1; i++) {
            if (v[i] > v[i+1]) {
                temp = v[i];
                v[i] = v[i+1];
                v[i+1] = temp;
            }
        }
    }

    printf("Vetor apos ordenacao: ");
    for (int i = 0; i < tam; i++) {
        printf("%d ", v[i]);
    }
    printf("\n");

    return 0;
}
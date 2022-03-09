#include <stdio.h>
#include <stdlib.h>

void exercicio1() {
    printf("Crie um programa que le 10 valores inteiros, insere em um vetor e mostre na tela os valores lidos.\n");
    
    int *vetor;
    vetor = (int*)malloc(sizeof(int)*10);
    
    for (int i = 0; i < 10; i++) {
        printf("Digite um valor: ");
        scanf("%d", &vetor[i]);
    }
    
    for (int i = 0; i < 10; i++) {
        printf("Valor da posição %d: %d\n", i, vetor[i]);
    }
}

void exercicio2() {
    printf("Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das componentes deste vetor,");
    printf(" armazenando o resultado em outro vetor. Os conjuntos possuem 10 elementos cada. Imprimir todos os conjuntos.\n");
    
    float *vetor, *vetorQuadrado;
    vetor = (float*)malloc(sizeof(float)*10);
    vetorQuadrado = (float*)malloc(sizeof(float)*10);
    
    for (int i = 0; i < 10; i++) {
        printf("Digite um numero: ");
        scanf("%f", &vetor[i]);
        vetorQuadrado[i] = vetor[i]*vetor[i];
    }
    
    printf("Valores do primeiro vetor: ") ;  
    for (int i = 0; i < 10; i++) {
        printf("%.1f, ", vetor[i]);
    }
    
    printf("\nValores do segundo vetor: ");
    for (int i = 0; i < 10; i++) {
        printf("%.1f, ", vetorQuadrado[i]);
    }
}

void exercicio3() {
    printf("\nLeia um vetor de 10 posicoes. Contar e escrever quantos valores pares ele possui.\n");
    
    int *vetor;
    vetor = (int*)malloc(sizeof(int)*10);
    
    int qtdPar = 0;
    
    for (int i = 0; i < 10; i++) {
        printf("Digite um valor: ");
        scanf("%d", &vetor[i]);
        
        if (vetor[i] % 2 ==0) {
            qtdPar++;
        }
    }
    
    printf("\nO vetor tem %d valores pares.\n", qtdPar);
}

void exercicio4() {
    printf("Faça um programa que receba do usuário um vetor com 10 posições. Em seguida deverá ser impresso o maior e o menor elemento do vetor.\n");
    
    int *vetor;
    vetor = (int*)malloc(sizeof(int)*10);
    
    int maior = 0;
    int menor = 0;
    
    for (int i = 0; i < 10; i++) {
        printf("Digite um valor: ");
        scanf("%d", &vetor[i]);
        
        if (i == 0) {
            maior = vetor[i];
            menor = vetor[i];
        } else {
            if (vetor[i] > maior) {
                maior = vetor[i];
            } else if(vetor[i] < menor) {
                menor = vetor[i];
            }
        }
    }
    printf("O maior valor do vetor e: %d\n", maior);
    printf("O menor valor do vetor e: %d\n", menor);
}

void exercicio5() {
    printf("Escreva um programa que leia 10 números inteiros e os armazene em um vetor. Imprima o vetor, o maior elemento e a posição que ele");
    printf(" se encontra.\n");
    
    int *vetor;
    vetor = (int*)malloc(sizeof(int)*10);
    
    int maior = 0;
    int indexMaior = 0;
    
    for (int i = 0; i < 10; i++) {
        printf("Digite um valor: ");
        scanf("%d", &vetor[i]);
        if (vetor[i] > maior) {
            maior = vetor[i];
            indexMaior = i;
        }
    }
    
    for (int i = 0; i < 10; i++) {
        printf("Valor da posicao %d do vetor: %d\n", i, vetor[i]);
    }
    
    printf("O maior valor do vetor e %d, ocupando a posicao %d\n", maior, indexMaior);
}

void exercicio6() {
    printf("Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a quantidade de números");
    printf(" negativos e a soma dos números positivos desse vetor.\n");
    
    
}

void exercicio7() {
    
}

void exercicio8() {
    
}

void exercicio9() {
    
}

void exercicio10() {
    
}

void exercicio11() {
    
}

void exercicio12() {
    
}

void exercicio13() {
    
}

void exercicio14() {
    
}

int main()
{
    //exercicio1();
    //exercicio2();
    //exercicio3();
    //exercicio4();
    //exercicio5();
    exercicio6();
    exercicio7();
    exercicio8();
    exercicio9();
    exercicio10();
    exercicio11();
    exercicio12();
    exercicio13();
    exercicio14();

    return 0;
}

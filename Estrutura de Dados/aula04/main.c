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
    printf("Faca um programa que preencha um vetor com 10 numeros reais, calcule e mostre a quantidade de numeros");
    printf(" negativos e a soma dos numeros positivos desse vetor.\n");
    
    float *vetor;
    vetor = (float*)malloc(sizeof(float)*10);
    
    int qtdNegativo = 0;
    int somaPositivo = 0;
    
    for (int i = 0; i < 10; i++) {
        printf("Digite um valor: ");
        scanf("%f", &vetor[i]);
        if (vetor[i] < 0) {
            qtdNegativo++;
        }
        if (vetor[i] > 0) {
            somaPositivo += vetor[i];
        }
    }
    
    printf("Quantidade de valores negativos: %d\nSoma dos valores positivos: %d\n", qtdNegativo, somaPositivo);
}

void exercicio7() {
    printf("Faca um programa que leia um vetor de 10 numeros. Leia um numero x. Conte os multiplos de x do vetor e mostre-os na tela.\n");
    
    int *vetor;
    vetor = (int*)malloc(sizeof(int)*10);
    
    int x;
    
    printf("Digite um valor a ser comparado: ");
    scanf("%d", &x);
    
    for (int i = 0; i < 10; i++) {
        printf("Digite um valor: ");
        scanf("%d", &vetor[i]);
    }
    
    for (int i = 0; i < 10; i++) {
        if (vetor[i] % x == 0) {
            printf("O valor %d e multiplo de %d\n", vetor[i], x);   
        }
    }
}

void exercicio8() {
    printf("Faca um vetor de tamanho 10 preenchido com o seguinte valor: (i + 5 * i) * (i + 1), sendo i posicao do elemento no vetor."); 
    printf("Em seguida imprima o vetor na tela.\n");
    
    int *vetor;
    vetor = (int*)malloc(sizeof(int)*10);
    
    for (int i = 0; i < 10; i++) {
        vetor[i] = (i+5*i) * (i+1);
    }
    
    for (int i = 0; i < 10; i++) {
        printf("Valor da posicao %d do vetor: %d\n", i, vetor[i]);
    }
}

void exercicio9() {
    printf("Faca um programa que leia um vetor de 5 posicoes para numeros reais e, depois, um codigo inteiro. Se o codigo for zero,"); 
    printf(" finalize o programa; se for 1, mostre o vetor na ordem em que foi preenchido; se for 2, mostre o vetor na ordem inversa.");
    printf(" Caso o codigo for diferente de 1 e 2 escreva uma mensagem informando que o código é inválido.\n");
    
    float *vetor;
    vetor = (float*)malloc(sizeof(float)*5);
    
    int codigo;
    
    for (int i = 0; i < 5; i++) {
        printf("Digite um valor: ");
        scanf("%f", &vetor[i]);
    }
    
    printf("Digite o codigo (0, 1 ou 2): ");
    scanf("%d", &codigo);
    
    if (codigo == 0) {
        printf("Finalizando programa...\n");
        exit;
    } else if (codigo == 1) {
        printf("Vetor na ordem preenchida: ");
        for (int i = 0; i < 5; i++) {
            printf("%.1f, ", vetor[i]);
        }
    } else if (codigo == 2) {
        for (int i = 4; i >= 0; i--) {
            printf("%.1f, ", vetor[i]);
        }
    } else {
        printf("Codigo invalido.\n");
    }
}

void exercicio10() {
    printf("Elabore um algoritmo em linguagem C que ordene os elementos de um vetor da forma crescente.\n");

    int *vetor, aux;
    vetor = (int*)malloc(sizeof(int)*5);

    for (int i = 0; i < 5; i++) {
        printf("Digite um valor: ");
        scanf("%d", &vetor[i]);
    }
    
    for (int i = 0; i < 5; i++) {
        for (int j = i+1; j < 5; j++) {
            if (vetor[j] < vetor[i]) {
                aux = vetor[i];
                vetor[i] = vetor[j];
                vetor[j] = aux;
            }
        }
    }

    printf("Vetor: ");
    for (int i = 0; i < 5; i++)
    {
        printf("%d ", vetor[i]);
    }
    
}

void exercicio11() {
    printf("\nDesenvolva um codigo em C que leia dois vetores inteiros de tamanho iguais e calcule a distancia de Hamming. A distancia de Hamming e dada peloo numero de posicoes nas quais elas diferem entre si. Exemplo: 1011 e 1111 possuem distancia de Hamming 1 pois se diferem em apenas 1 posicao.\n");

    int *vetor1, *vetor2;
    vetor1 = (int*)malloc(sizeof(int)*5);
    vetor2 = (int*)malloc(sizeof(int)*5);

    int distanciaHamming = 0;
    int aux = 0;

    printf("----------Coleta de Dados do Vetor 1-----------\n");
    for (int i = 0; i < 5; i++) {
        printf("Digite um valor: ");
        scanf("%d", &vetor1[i]);
    }
    printf("----------Coleta de Dados do Vetor 2-----------\n");
    for (int i = 0; i < 5; i++) {
        printf("Digite um valor: ");
        scanf("%d", &vetor2[i]);
    }

    for (int i = 0; i < 5; i++) {
        for (int j = i+1; j < 5; j++) {
            if (vetor1[j] < vetor1[i]) {
                aux = vetor1[i];
                vetor1[i] = vetor1[j];
                vetor1[j] = aux;
            }
            if (vetor2[j] < vetor2[i]) {
                aux = vetor2[i];
                vetor2[i] = vetor2[j];
                vetor2[j] = aux;
            }
        }
    }

    printf("Vetor 1:\n");
    for (int i = 0; i < 5; i++)
    {
        printf("%d ", vetor1[i]);
    }
    
    printf("\nVetor 2:\n");
    for (int i = 0; i < 5; i++)
    {
        printf("%d ", vetor2[i]);
    }

    for (int i = 0; i < 5; i++) {
        if (vetor1[i] != vetor2[i]) {
            distanciaHamming++;
        }
    }
    

    printf("\nA distancia de Hamming entre os dois vetores e de %d posicoes.", distanciaHamming);
}

void exercicio12() {
    
}

void exercicio13() {
    
}

void exercicio14() {
    
}

void exercicio15() {
    printf("Leia uma matriz 3 x 3. Leia também um valor X. O programa deverá fazer uma busca desse valor na matriz e, ao final, escrever a ");
    printf("localização (linha e coluna) ou uma mensagem de “não encontrado”.\n");
    
    int matriz[3][3];
    int x;
    int linhaX, colunaX;
    
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("Digite um valor para a linha %d coluna %d: ", i, j);
            scanf("%d", &matriz[i][j]);
        }
    }
    
    printf("Digite um valor para buscar na matriz: ");
    scanf("%d", &x);
    
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (matriz[i][j] == x) {
                linhaX = i;
                colunaX = j;
            } else {
                printf("Valor não encontrado\n");
            }
        }
    }
}

void exercicio16() {
    
}

void exercicio17() {
    
}

void exercicio18() {
    
}

void exercicio19() {
    
}

void exercicio20() {
    
}

void exercicio21() {
    
}

void exercicio22() {
    
}

void exercicio23() {
    
}

int main()
{
    //exercicio1();
    //exercicio2();
    //exercicio3();
    //exercicio4();
    //exercicio5();
    //exercicio6();
    //exercicio7();
    //exercicio8();
    //exercicio9();
    //exercicio10();
    exercicio11();
    exercicio12();
    exercicio13();
    exercicio14();
    //exercicio15();
    exercicio16();
    exercicio17();
    exercicio18();
    exercicio19();
    exercicio20();
    exercicio21();
    exercicio22();
    exercicio23();

    return 0;
}

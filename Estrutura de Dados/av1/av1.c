#include <stdio.h>
#include <stdlib.h>

void alocaNome(char *nome) {
    nome = (char*)malloc(8 * sizeof(char));

    printf("Digite o nome: ");
    scanf("%s", nome);

    printf("Nome: %s\n", nome);
}

typedef struct {
    int matricula;
    char nome[30];
    float nota1;
    float nota2;
} Aluno;

int main() {

    // Questão 1
    int matriz[4][4];
    int somaLinha[4] = {0, 0, 0, 0};

    // Preenche a matriz
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            printf("Digite um valor para a linha %d coluna %d: ", i, j);
            scanf("%d", &matriz[i][j]);
        }
    }

    // Imprime a matriz
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (matriz[i][j] >= 10) {
                printf("%d ", matriz[i][j]);
            } else {
                printf("%d  ", matriz[i][j]);
            }
        }
        printf("\n");
    }

    // Soma a linha
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            somaLinha[i] += matriz[i][j];
        }
    }

    for (int i = 0; i < 4; i++) {
        printf("Soma da linha %d: %d\n", i, somaLinha[i]);
    }

    //Questão 2
    char *cadeiaCaracteres;
    int quantidadeCaracteres = 0;

    printf("Digite a quantidade de caracteres que deseja preencher: ");
    scanf("%d", &quantidadeCaracteres);

    cadeiaCaracteres = (char *) malloc(quantidadeCaracteres * sizeof(char));

    printf("Digite a cadeia de caracteres desejada: ");
    scanf("%s", cadeiaCaracteres);

    printf("Cadeia de caracteres: %s\n", cadeiaCaracteres);

    //Questão 3
    char *nome;

    alocaNome(&nome);

    //Questão 4
    
    int *vetor;
    int tamanhoVetor;

    printf("Digite o tamanho do vetor: ");
    scanf("%d", &tamanhoVetor);

    // Alocando dinamicamente o vetor
    vetor = (int*)malloc(tamanhoVetor * sizeof(int));

    // Preenchendo o vetor
    for (int i = 0; i < tamanhoVetor; i++) {
        printf("Digite um valor para o vetor: ");
        scanf("%d", &vetor[i]);
    }

    // Imprimindo o vetor em ordem inversa
    for (int i = tamanhoVetor; i > 0; i--) {
        printf("%d ", vetor[i-1]);
    }

    // Questão 5
    Aluno aluno[5];
    float media[5] = {0, 0, 0, 0, 0};

    // Preenchendo os dados dos alunos
    for (int i = 0; i < 5; i++) {
        printf("Digite a matricula do aluno %d: ", i+1);
        scanf("%d", &aluno[i].matricula);
        printf("Digite o nome do aluno %d: ", i+1);
        scanf("%s", aluno[i].nome);
        printf("Digite a nota 1 do aluno %d: ", i+1);
        scanf("%f", &aluno[i].nota1);
        printf("Digite a nota 2 do aluno %d: ", i+1);
        scanf("%f", &aluno[i].nota2);
    }

    // Calculando a média de cada aluno
    for (int i = 0; i < 5; i++) {
        media[i] = (aluno[i].nota1 + aluno[i].nota2) / 2;
    }

    // Imprimindo os dados dos alunos
    for (int i = 0; i < 5; i++) {
        printf("Matricula: %d\n", aluno[i].matricula);
        printf("Nome: %s\n", aluno[i].nome);
        printf("Media: %.2f\n", media[i]);
    }

    return 0;
}
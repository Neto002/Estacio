#include <stdio.h>
#include <stdlib.h>

CRT_SECURE_NO_WARNINGS;

int exercicio1() {
    printf("Escreva um algoritmo para ler um valor (do teclado) e escrever (na tela) o seu antecessor\n");
    int valor;

    printf("Digite um valor: ");
    scanf_s("%d", &valor);

    int antecessor = valor - 1;

    printf("Antecessor do numero digitado: %d\n", antecessor);
}

int exercicio2() {
    printf("Escreva um algoritmo para ler as dimensoes de um retangulo (base e altura), calcular e escrever a area do retangulo.\n");
    float base;
    float altura;
    float areaRetangulo;

    printf("Digite o valor da base: ");
    scanf_s("%f", &base);

    printf("Digite o valor da altura: ");
    scanf_s("%f", &altura);

    areaRetangulo = base * altura;

    printf("A area do retangulo e: %0.2f\n", areaRetangulo);
}

int exercicio3() {
    printf("Faca um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mes com 30 dias\n");
    int idadeAnos;
    int idadeMeses;
    int idadeDias;

    printf("Digite sua idade em anos: ");
    scanf_s("%d", &idadeAnos);

    printf("%d anos e quantos meses: ", idadeAnos);
    scanf_s("%d", &idadeMeses);

    printf("%d anos, %d meses e quantos dias: ", idadeAnos, idadeMeses);
    scanf_s("%d", &idadeDias);

    idadeDias = idadeDias + (idadeAnos * 365) + (idadeMeses * 30);

    printf("A sua idade somente em dias e: %d\n", idadeDias);
}

int exercicio4() {
    printf("Escreva um algoritmo para ler o numero total de eleitores de um municipio, o numero de votos brancos, nulos e validos. Calcular e escrever o percentual que cada um representa em relacao ao total de eleitores.\n");
    float totalEleitores;
    float votoBranco;
    float votoNulo;
    float votoValido;

    printf("Digite o total de eleitores do municipio: ");
    scanf_s("%d", &totalEleitores);

    printf("Digite o total de votos brancos: ");
    scanf_s("%d", &votoBranco);

    printf("Digite o total de votos nulos: ");
    scanf_s("%d", &votoNulo);

    printf("Digite o total de votos validos: ");
    scanf_s("%d", &votoValido);

    float porcentoBranco = (votoBranco/totalEleitores) * 100;
    float porcentoNulo = (votoNulo / totalEleitores) * 100;
    float porcentoValido = (votoValido / totalEleitores) * 100;

    printf("Porcentagens: \nVotos Brancos: %.2f%%\nVotos Nulos: %.2f%%\nVotos Validos: %.2f%%\n", porcentoBranco, porcentoNulo, porcentoValido);
}

float calculaSalario(float salario, float reajuste) {
    float salarioReajustado = salario + (salario * (reajuste / 100));
    return salarioReajustado;
}

int exercicio5() {
    printf("Escreva um algoritmo para ler o salario mensal atual de um funcionario e o percentual de reajuste. Calcular e escrever o valor do novo salario. Faca os calculos usando função.\n");
    float salario;
    float percentualReajuste;

    printf("Digite seu salario mensal: ");
    scanf_s("%f", &salario);

    printf("Digite o percentual de reajuste: ");
    scanf_s("%f", &percentualReajuste);

    float salarioReajustado = calculaSalario(salario, percentualReajuste);

    printf("Valor do salario reajustado: R$%.2f\n", salarioReajustado);

}

int exercicio6() {
    printf("Ler um valor e escrever a mensagem \"E MAIOR QUE 10!\" se o valor lido for maior que 10, caso contrario escrever \"NAO E MAIOR QUE 10!\".\n");
    int valor;

    printf("Digite um valor: ");
    scanf_s("%d", &valor);

    if (valor > 10) {
        printf("E MAIOR QUE 10\n");
    }
    else {
        printf("NAO E MAIOR QUE 10\n");
    }
}

int exercicio7() {
    printf("Ler um valor e escrever se e positivo ou negativo (considere o valor zero como positivo).\n");
    int valor;
    printf("Digite um valor: ");
    scanf_s("%d", &valor);

    if (valor >= 0) {
        printf("Positivo\n");
    }
    else {
        printf("Negativo\n");
    }
}

int exercicio8() {
    printf("Ler as notas da 1a. e 2a. avaliacoes de um aluno. Calcular a media aritmetica simples e escrever uma mensagem que diga se o aluno foi ou nao aprovado (considerar que nota igual ou maior que 6 o aluno e aprovado). Escrever também a media calculada.\n");
    float av1, av2, media;

    printf("Digite sua primeira nota: ");
    scanf_s("%f", &av1);

    printf("Digite sua segunda nota: ");
    scanf_s("%f", &av2);

    media = (av1 + av2) / 2;

    printf("Media: %.2f\n", media);

    if (media >= 6) {
        printf("APROVADO\n");
    }
    else {
        printf("REPROVADO\n");
    }
}

int exercicio9() {
    printf("Faca um programa em C que imprima de 1 a 50 na tela. \n");
    for (int i = 1; i <= 50; i++) {
        printf("%d\n", i);
    }
}

int exercicio10() {
    printf("Elabore um codigo que imprima uma sequencia de 1 ate 100 somente com os numeros pares dessa sequencia.\n");
    for (int i = 1; i <= 100; i++) {
        if (i % 2 == 0) {
            printf("%d\n", i);
        }
    }
}

int main(int argc, char* argv[]) {

    exercicio1();

    exercicio2();

    exercicio3();

    exercicio4();

    exercicio5();

    exercicio6();

    exercicio7();

    exercicio8();

    exercicio9();

    exercicio10();

    return 0;
}

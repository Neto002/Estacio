#include <stdio.h>
#include <stdlib.h>

int exercicio1() {
    printf("Escreva um algoritmo para ler um valor (do teclado) e escrever (na tela) o seu antecessor\n");
    short valor;

	printf("Digite um valor: ");
	scanf("%d", &valor);

	short antecessor = valor - 1;

	printf("Antecessor do numero digitado: %d\n", antecessor);
}

int exercicio2() {
    printf("Escreva um algoritmo para ler as dimensões de um retângulo (base e altura), calcular e escrever a área do retângulo.\n");
    float base;
	float altura;
	float areaRetangulo;

	printf("Digite o valor da base: ");
	scanf("%f", &base);

	printf("Digite o valor da altura: ");
	scanf("%f", &altura);

	areaRetangulo = base * altura;

	printf("A area do retangulo e: %0.2f\n", areaRetangulo);
}

int exercicio3() {
    printf("Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias\n");
    short idadeAnos;
	short idadeMeses;
	int idadeDias;

	printf("Digite sua idade em anos: ");
	scanf("%d", &idadeAnos);

	printf("%d anos e quantos meses: ", idadeAnos);
	scanf("%d", &idadeMeses);

	printf("%d anos, %d meses e quantos dias: ", idadeAnos, idadeMeses);
	scanf("%d", &idadeDias);

	idadeDias += (idadeAnos*365) + (idadeMeses*30);

	printf("A sua idade somente em dias e: %d\n", idadeDias);
}

int exercicio4() {
    printf("Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.\n");
    int totalEleitores;
	int votoBranco;
	int votoNulo;
	int votoValido;

	printf("Digite o total de eleitores do municipio: ");
	scanf("%d", &totalEleitores);

	printf("Digite o total de votos brancos: ");
	scanf("%d", &votoBranco);

	printf("Digite o total de votos nulos: ");
	scanf("%d", &votoNulo);

	printf("Digite o total de votos validos: ");
	scanf("%d", &votoValido);

	float porcentoBranco = (votoBranco/totalEleitores) * 100;
	float porcentoNulo = (votoNulo/totalEleitores) * 100;
	float porcentoValido = (votoValido/totalEleitores) * 100;

	printf("Porcentagens: \nVotos Brancos: %f%%\nVotos Nulos: %f%%\nVotos Validos: %f%%\n", porcentoBranco, porcentoNulo, porcentoValido);
}

int exercicio5() {
    float calculaSalario(float salario, float reajuste) {
        float salarioReajustado = salario + (salario * (reajuste/100));
        return salarioReajustado;
    }
    printf("// Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e escrever o valor do novo salário. Faça os cálculos usando função.\n");
    float salario;
    float percentualReajuste;

    printf("Digite seu salario mensal: ");
    scanf("%f", &salario);

    printf("Digite o percentual de reajuste: ");
    scanf("%f", &percentualReajuste);

    float salarioReajustado = calculaSalario(salario, percentualReajuste);

    printf("Valor do salario reajustado: R$%.2f\n", salarioReajustado);

}

int exercicio6() {
    printf("Ler um valor e escrever a mensagem “É MAIOR QUE 10!” se o valor lido for maior que 10, caso contrário escrever “NÃO É MAIOR QUE 10!”.\n");
    int valor;

    printf("Digite um valor: ");
    scanf("%d", &valor);

    if (valor > 10) {
        printf("E MAIOR QUE 10\n");
    } else {
        printf("NAO E MAIOR QUE 10\n");
    }
}

int exercicio7() {
    printf("Ler um valor e escrever se é positivo ou negativo (considere o valor zero como positivo).\n");
    short valor;
    printf("Digite um valor: ");
    scanf("%d", &valor);

    if (valor >= 0) {
        printf("Positivo\n");
    } else {
        printf("Negativo\n");
    }
}

int exercicio8() {
    printf("Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.\n");
    float av1, av2, media;

    printf("Digite sua primeira nota: ");
    scanf("%f", &av1);

    printf("Digite sua segunda nota: ");
    scanf("%f", &av2);

    media = (av1+av2)/2;

    printf("Media: %.2f\n", media);

    if (media >= 6) {
        printf("APROVADO\n");
    } else {
        printf("REPROVADO\n");
    }
}

int exercicio9() {
    printf("Faça um programa em C que imprima de 1 a 50 na tela. \n");

    int i = 1;
    for (i = 1; i <= 50; i++) {
        printf("%d\n", i);
    }
}

int exercicio10() {
    printf("\n");
}

int main(int argc, char *argv[]) {

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

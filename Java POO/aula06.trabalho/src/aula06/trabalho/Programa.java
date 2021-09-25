package aula06.trabalho;

import java.util.Scanner;

public class Programa {

	public static void main(String[] args) {
		//Instancia��o
		ContaBancaria conta = new ContaBancaria();
		Scanner teclado = new Scanner(System.in);
		
		
		int escolha = 0;
		
		while (escolha != 5) {
			//Menu de op��es
			System.out.println("Qual opera��o deseja realizar?\n1- Consultar Saldo\n2- Consultar Data de Abertura\n3- Dep�sito\n4- Saque\n5- Sair");
			System.out.print("Escolha: ");
			escolha = teclado.nextInt();
			
			//Seletor de opera��o do menu
			switch (escolha) {
				case 1: //Consulta de Saldo
					System.out.println("Saldo: " + conta.getSaldoFormatado());
					break;
				case 2: //Consulta de Data de Abertura da Conta
					System.out.println("Data de Abertura da conta: " + conta.getDataAberturaFormatada());
					break;
				case 3: //Dep�sito
					System.out.println("Digite um valor a ser depositado na conta: ");
					conta.depositar(teclado.nextDouble());
					break;
				case 4: //Saque
					System.out.println("Digite um valor a ser sacado: ");
					conta.sacar(teclado.nextDouble());
					break;
				case 5: //Encerra o programa
					System.out.println("Encerrando..");
					break;
				default:
					System.out.println("Op��o inv�lida");
			}
		}
		
		teclado.close();

	}

}

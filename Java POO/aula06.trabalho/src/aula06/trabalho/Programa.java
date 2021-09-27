/*
 * Aluno: Antonio Gomes Ferreira Neto
 * Matrícula: 202102570735
 */
package aula06.trabalho;

import java.util.Scanner;

public class Programa {

	public static void main(String[] args) {
		//Instanciação
		ContaBancaria conta = new ContaBancaria();
		Scanner teclado = new Scanner(System.in);
		
		int escolha = 0;
		
		while (escolha != 5) {
			//Menu de opções
			System.out.println("Qual operação deseja realizar?\n1- Consultar Saldo\n2- Consultar Data de Abertura\n3- Depósito\n4- Saque\n5- Sair");
			System.out.print("Escolha: ");
			escolha = teclado.nextInt();
			
			//Seletor de operação do menu
			switch (escolha) {
				case 1: //Consulta de Saldo
					System.out.println("------------Consulta de Saldo------------");
					System.out.println("Saldo: " + conta.getSaldoFormatado());
					System.out.println("-----------------------------------------");
					break;
				case 2: //Consulta de Data de Abertura da Conta
					System.out.println("------------Consulta de Data de Abertura------------");
					System.out.println("Data de Abertura da conta: " + conta.getDataAberturaFormatada());
					System.out.println("----------------------------------------------------");
					break;
				case 3: //Depósito
					System.out.println("----------------------Depósito---------------------");
					System.out.println("Digite um valor a ser depositado na conta: ");
					conta.depositar(teclado.nextDouble());
					System.out.println("---------------------------------------------------");
					break;
				case 4: //Saque
					System.out.println("----------------------Saque------------------------");
					System.out.println("Digite um valor a ser sacado: ");
					conta.sacar(teclado.nextDouble());
					System.out.println("---------------------------------------------------");
					break;
				case 5: //Encerra o programa
					System.out.println("Encerrando..");
					break;
				default:
					System.out.println("Opção inválida");
			}
		}
		
		teclado.close();

	}

}

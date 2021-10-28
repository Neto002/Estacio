package trabalho_aula10;

import java.util.Scanner;

//Programa para simular inserções de produtos em um vetor de 10 posições (0 a 9), com tratamento de exceções para situações em que o índice informado não existe.

public class Principal {

	public static void main(String[] args) {

		Produto[] vetor = new Produto[10];
		Scanner scanner = new Scanner(System.in);
		int posicaoProduto = 0;
		
		for (int i = 0; i < 10; i++) {
			vetor[i] = new Produto();
		}
		
		//Coleta de dados para o produto
		
		System.out.println("Nome do produto: ");
		String nomeProduto = scanner.nextLine();
		
		System.out.println("Descrição do produto: ");
		String descricaoProduto = scanner.nextLine();
		
		System.out.println("Preço do produto: ");
		float precoProduto = scanner.nextFloat();
		
		//Verificação do índice informado
		try {
			
			System.out.println("Posição do produto no vetor (0 a 9): ");
			posicaoProduto = scanner.nextInt();
			
			if (posicaoProduto < 0 || posicaoProduto > 9) {
				
				scanner.close();
				throw new ArrayIndexOutOfBoundsException();
				
			}
			
		} catch (ArrayIndexOutOfBoundsException e) { //Tratamento da exceção
			
			System.out.println("Você digitou um valor inválido, por favor digite um valor de 0 a 9:");
			posicaoProduto = scanner.nextInt();
			
			while (posicaoProduto < 0 || posicaoProduto > 9) {
				
				System.out.println("Você digitou um valor inválido, por favor digite um valor de 0 a 9:");
				posicaoProduto = scanner.nextInt();
				
			}
			
		} finally { //Atribuição dos valores informados ao produto
			
			vetor[posicaoProduto].setNome(nomeProduto);
			vetor[posicaoProduto].setDescricao(descricaoProduto);
			vetor[posicaoProduto].setPreco(precoProduto);
			
		}
		
		try {
			
			System.out.println("Posição do vetor que deseja visualizar: ");
			posicaoProduto = scanner.nextInt();
			
			
			if (posicaoProduto < 0 || posicaoProduto > 9) {
				
				scanner.close();
				throw new ArrayIndexOutOfBoundsException();
				
			}
			
		} catch (ArrayIndexOutOfBoundsException e) { //Tratamento da exceção
			
			System.out.println("Você digitou um valor inválido, por favor digite um valor de 0 a 9:");
			posicaoProduto = scanner.nextInt();
			
			while (posicaoProduto < 0 || posicaoProduto > 9) {
				
				System.out.println("Você digitou um valor inválido, por favor digite um valor de 0 a 9:");
				posicaoProduto = scanner.nextInt();
				
			}
			
		} finally { //Exibição dos dados do produto selecionado
			
			System.out.println("Nome: " + vetor[posicaoProduto].getNome() + "\nDescrição: " + vetor[posicaoProduto].getDescricao() + "\nPreço: " + 
		    String.format("R$%.2f", vetor[posicaoProduto].getPreco()));
			
		}
		
		scanner.close();
		
	}
}

package trabNov;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
        Produto[] vetor = new Produto[10];
        Scanner scanner = new Scanner(System.in);
        int i = 0;

        for (int c = 0; c < 10; c++) {
        	vetor[c] = new Produto();
        }
        
        try {
        	System.out.println("posicao: ");
        	i = scanner.nextInt();
			if (i < 0 || i> vetor.length-1) {
				throw new ArrayIndexOutOfBoundsException();
			}
        } catch (ArrayIndexOutOfBoundsException e) {
        	System.out.println("erro. digite 0 e 9:");
        	i = scanner.nextInt();
        } finally {
        	System.out.println("nome:");
        	vetor[i].nome = scanner.next();
        	System.out.println("desc:");
        	vetor[i].descricao = scanner.next();
        	System.out.println("preco;");
        	vetor[i].preco = scanner.nextDouble();
        	System.out.println("Produto cadastrado com sucesso!");
        	System.out.println("Detalhes do produto:\nNome: " + vetor[i].nome + "\nDescrição: " + vetor[i].descricao + "\nPreço: " + vetor[i].preco);
        }
        
    }
	
}

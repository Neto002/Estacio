package aula09;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner teclado = new Scanner(System.in);
		System.out.println("Digite o primeiro n�mero: ");
		int n1 = teclado.nextInt();
		System.out.println("Digite o primeiro n�mero: ");
		int n2 = teclado.nextInt();
		
		try{
			System.out.println(n1/n2);
		} catch(ArithmeticException e) {
			System.out.println("Valor de n2 � igual a 0");
		}
		
	}

}

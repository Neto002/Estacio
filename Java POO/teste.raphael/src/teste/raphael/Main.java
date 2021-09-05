package teste.raphael;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
	
	System.out.println("Bloco de Notas\n");
	Nota[] notas = new Nota[3];
	
	for (int c = 0; c < 3; c++) {
		notas[c] = new Nota();
		Scanner scanner = new Scanner(System.in);
		System.out.println("Digite o seu nome:");
		notas[c].nome = scanner.nextLine();
		System.out.println("Digite a data de criação da nota:");
		notas[c].data = scanner.nextLine();
		System.out.println("Digite a sua nota:");
		notas[c].info = scanner.nextLine();
	}
	
	List<Nota> bloco = new ArrayList<>();
	bloco.add(notas[0]);
	bloco.add(notas[1]);
	bloco.add(notas[2]);
	bloco.add(new Nota());
	bloco.remove(3);
	
	System.out.println(bloco);
	
	}

}

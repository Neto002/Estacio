package aula03.trabalho;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {

	public static void main(String[] args) {
		
		System.out.println("DEMONSTRAÇÃO DE LISTAS - GRUPO 1\n");
		List<Notas> blocoNotas = new ArrayList<>();
		
		System.out.println("Criando as notas...\n");
		
		Notas nota1 = new Notas("Antonio", "03/09/2021", "Informação Nota 1");
		Notas nota2 = new Notas("Brenno", "05/08/2017", "Informação Nota 2");
		Notas nota3 = new Notas("Alice", "01/12/2027", "Informação Nota 3");
		Notas nota4 = new Notas("Beatriz", "26/01/2012", "Informação Nota 4");
		Notas nota5 = new Notas("Arthur", "31/08/2021", "Informação Nota 5");
		
		System.out.println("Nota 1: " + nota1 + "\nNota 2: " + nota2 + "\nNota 3: " + nota3 + "\nNota 4: " + nota4 + "\nNota 5: " + nota5);
		
		System.out.println("\nAdicionando notas ao Bloco de Notas...\n");
		
		blocoNotas.add(nota1);
		blocoNotas.add(nota2);
		blocoNotas.add(nota3);
		blocoNotas.add(nota4);
		blocoNotas.add(nota5);
		
		System.out.println("Notas adicionadas ao Bloco de Notas.\n");
		
		System.out.println("Exibindo o Bloco de Notas:\n");
		System.out.println(blocoNotas);
		
		System.out.println("\nAdicionando uma sexta nota ao Bloco de Notas via programa...\n");
		blocoNotas.add(new Notas("Nota de Exemplo", "03/09/2021", "Nota de exemplo para implementação do programa"));
		
		System.out.println(blocoNotas);
		
		System.out.println("\nRemovendo a terceira nota...\n");
		blocoNotas.remove(2);
		
		System.out.println(blocoNotas);
		
		System.out.println("\nAlterando o nome da nota 1 via programa...\n");
		blocoNotas.get(0).setNome("João");
		
		System.out.println(blocoNotas);
		
		System.out.println("\nOrdenando o Bloco de Notas por ordem alfabética...\n");
		Collections.sort(blocoNotas);
		System.out.println(blocoNotas);
	}

}

package aula01;

import java.util.Scanner;

public class Aula { //Classe Instanciadora

	public static void main(String[] args) {
		
		//Instanciando a classe Aluno
		Aluno alunoA = new Aluno(202102570735L, "Neto");
		
		Scanner teclado = new Scanner(System.in);
		
		System.out.println("Digite seu nome: ");
		String nome = teclado.nextLine();
		
		System.out.println("Digite sua matrícula: ");
		long matricula = teclado.nextLong();
		
		alunoA.setNomeAluno(nome);
		alunoA.setMatriculaAluno(matricula);
		
		//Exibir os dados
		System.out.println(alunoA);
		
	}
	
}

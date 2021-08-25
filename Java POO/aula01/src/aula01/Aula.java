package aula01;

import java.util.Scanner;

import javax.swing.JOptionPane;

@SuppressWarnings("unused")
public class Aula { //Classe Instanciadora

	public static void main(String[] args) {
		
		//Instanciando a classe Aluno
		Aluno alunoA = new Aluno(202102570735L, "Neto");
		
		//Informando dados via teclado com a classe Scanner
		/*Scanner teclado = new Scanner(System.in);
		
		System.out.println("Digite seu nome: ");
		String nome = teclado.nextLine();
		
		System.out.println("Digite sua matrícula: ");
		long matricula = teclado.nextLong();
		
		alunoA.setNomeAluno(nome);
		alunoA.setMatriculaAluno(matricula);
		
		teclado.close();*/
		
		//Exibir os dados
		System.out.println(alunoA);
		
		//Informando dados via teclado com o JOptionPane
		alunoA.setNomeAluno(String.valueOf(JOptionPane.showInputDialog(null, "Digite seu nome: ", "Nome", JOptionPane.INFORMATION_MESSAGE, null, null, null)));
		alunoA.setMatriculaAluno(Long.valueOf(String.valueOf(JOptionPane.showInputDialog(null, "Digite seu nome: ",
								 "Nome", JOptionPane.INFORMATION_MESSAGE, null, null, null))));
		
		JOptionPane.showInternalMessageDialog(null, "Nome do aluno: " + alunoA.getNomeAluno() + 
											  "\nMatrícula do aluno: " + alunoA.getMatriculaAluno(), "Informações", JOptionPane.INFORMATION_MESSAGE, null);
		
		
	}
	
}

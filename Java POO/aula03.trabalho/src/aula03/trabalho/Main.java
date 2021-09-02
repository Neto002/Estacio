package aula03.trabalho;

import java.util.ArrayList;
import java.util.List;

import javax.swing.JOptionPane;

public class Main {

	public static void main(String[] args) {

		/*//Cria��o da Lista
		List<Notas> blocoDeNotas = new ArrayList<>();
		
		//Inclus�o das Notas � Lista
		blocoDeNotas.add(new Notas("Antonio Neto", "01/09/2021", "Hello World"));
		blocoDeNotas.add(new Notas("Jo�o Silva", "05/12/2019", "Oi"));
		
		//Exibi��o da Lista
		System.out.println(blocoDeNotas);*/
		
		List<Notas> blocoNotas = new ArrayList<>();
		
		int quantidadeNotas = Integer.parseInt(JOptionPane.showInputDialog(null, "Quantas notas deseja adicionar?", "Implementa��o de Listas - GRUPO 1", 
				JOptionPane.PLAIN_MESSAGE));
		
		Notas[] notas = new Notas[quantidadeNotas];
		
		for (int c = 0; c < quantidadeNotas; c++) {
			notas[c] = new Notas();
			notas[c].setNome(JOptionPane.showInputDialog(null, "Digite o nome da nota:", "Nome da Nota", JOptionPane.PLAIN_MESSAGE));
			notas[c].setDataCriacao(JOptionPane.showInputDialog(null, "Digite a data de cria��o da nota (dd/mm/aaaa):", "Data da Nota", JOptionPane.PLAIN_MESSAGE));
			notas[c].setInformacao(JOptionPane.showInputDialog(null, "Digite a informa��o da nota:", "Informa��o da Nota", JOptionPane.PLAIN_MESSAGE));
			blocoNotas.add(notas[c]);
		}
		
		JOptionPane.showMessageDialog(null, "Bloco de Notas:\n" + blocoNotas + "\n", "Exibi��o Bloco de Notas - GRUPO 1", JOptionPane.PLAIN_MESSAGE);
		
	}

}

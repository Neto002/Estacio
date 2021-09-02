package aula03.trabalho;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;

import javax.swing.JOptionPane;

public class Main {

	public static void main(String[] args) {
		
		List<Notas> blocoNotas = new ArrayList<>();
		
		blocoNotas.add(new Notas("b"));
		blocoNotas.add(new Notas("z"));
		blocoNotas.add(new Notas("a"));
		
		Collections.sort(blocoNotas);
		System.out.println(blocoNotas);
		
		/*int quantidadeNotas = Integer.parseInt(JOptionPane.showInputDialog(null, "Quantas notas deseja adicionar?", "Implementação de Listas - GRUPO 1", 
				JOptionPane.PLAIN_MESSAGE));
		
		Notas[] notas = new Notas[quantidadeNotas];
		
		for (int c = 0; c < quantidadeNotas; c++) {
			notas[c] = new Notas();
			notas[c].setNome(JOptionPane.showInputDialog(null, "Digite o nome da nota:", "Nome da Nota", JOptionPane.PLAIN_MESSAGE));
			notas[c].setDataCriacao(JOptionPane.showInputDialog(null, "Digite a data de criação da nota (dd/mm/aaaa):", "Data da Nota", JOptionPane.PLAIN_MESSAGE));
			notas[c].setInformacao(JOptionPane.showInputDialog(null, "Digite a informação da nota:", "Informação da Nota", JOptionPane.PLAIN_MESSAGE));
			blocoNotas.add(notas[c]);
		}
		
		JOptionPane.showMessageDialog(null, "Bloco de Notas:\n" + blocoNotas, "Exibição Bloco de Notas - GRUPO 1", JOptionPane.PLAIN_MESSAGE);*/
		
		
	}

}

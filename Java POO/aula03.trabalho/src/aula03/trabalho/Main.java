package aula03.trabalho;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import javax.swing.JOptionPane;

public class Main {

	public static void main(String[] args) {
		
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
		
		Collections.sort(blocoNotas);
		JOptionPane.showMessageDialog(null, "Bloco de Notas:\n" + blocoNotas, "Exibi��o Bloco de Notas - GRUPO 1", JOptionPane.PLAIN_MESSAGE);
		
		
	}

}

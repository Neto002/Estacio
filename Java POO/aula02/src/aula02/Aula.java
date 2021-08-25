package aula02;

import javax.swing.JOptionPane;

public class Aula {

	public static void main(String[] args) {

		Tecnico tecnico = new Tecnico();
		
		tecnico.setMatricula(String.valueOf(JOptionPane.showInputDialog(null, "Digite a matrícula: ", "Informe os dados: ", JOptionPane.INFORMATION_MESSAGE, null, null, null)));
		tecnico.setNome(String.valueOf(JOptionPane.showInputDialog(null, "Digite o nome: ", "Informe os dados: ", JOptionPane.INFORMATION_MESSAGE, null, null, null)));
		tecnico.setTitulo(String.valueOf(JOptionPane.showInputDialog(null, "Digite o titulo: ", "Informe os dados: ", JOptionPane.INFORMATION_MESSAGE, null, null, null)));
		
		JOptionPane.showMessageDialog(null, "Matrícula: " + tecnico.getMatricula() +
											"\nNome: " + tecnico.getNome() +
											"\nTítulo: " + tecnico.getTitulo(), "DADOS DO TÉCNICO", JOptionPane.INFORMATION_MESSAGE, null);
		
	}

}

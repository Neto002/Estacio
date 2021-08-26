package aula02;

import javax.swing.JOptionPane;

public class Aula {

	public static void main(String[] args) {

		Tecnico tecnico = new Tecnico();
		
		tecnico.setMatricula(Long.parseLong(JOptionPane.showInputDialog(null, "Digite a matrícula: ", "Informe os dados: ", JOptionPane.INFORMATION_MESSAGE)));
		tecnico.setNome(JOptionPane.showInputDialog(null, "Digite o nome: ", "Informe os dados: ", JOptionPane.INFORMATION_MESSAGE));
		tecnico.setTitulo(JOptionPane.showInputDialog(null, "Digite o titulo: ", "Informe os dados: ", JOptionPane.INFORMATION_MESSAGE));
		
		mostraTecnico(tecnico.getMatricula(), tecnico.getNome(), tecnico.getTitulo());
		
	}
	
	public static void mostraTecnico(Long m, String n, String t) {
		JOptionPane.showMessageDialog(null, "Matrícula: " + m +
				"\nNome: " + n +
				"\nTítulo: " + t, "DADOS DO TÉCNICO", JOptionPane.INFORMATION_MESSAGE, null);
	}

}

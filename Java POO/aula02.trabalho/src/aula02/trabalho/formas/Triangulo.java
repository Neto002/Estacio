package aula02.trabalho.formas;

import javax.swing.JOptionPane;

public class Triangulo extends Forma2D { //SubClasse de Forma2D
	
	Triangulo() {
		
	}
	
	//Sobreposição de Método
	@Override
	public void area() {
		double area = (this.getDimensao1() * this.getDimensao2()) / 2;
		JOptionPane.showMessageDialog(null, "Área: " + area, "ÁREA DO TRIÂNGULO - GRUPO 1", JOptionPane.PLAIN_MESSAGE);
	}

}

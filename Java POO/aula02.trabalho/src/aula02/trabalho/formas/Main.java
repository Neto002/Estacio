package aula02.trabalho.formas;

import javax.swing.JOptionPane;

public class Main { //Classe Instanciadora

	public static void main(String[] args) {
		
		//Instâncias
		Forma2D forma = new Forma2D();
		Quadrado quadrado = new Quadrado();
		Triangulo triangulo = new Triangulo();
		
		//Input dos valores das dimensões
		double d1 = Double.parseDouble(JOptionPane.showInputDialog(null, "Primeira dimensão:"));
		double d2 = Double.parseDouble(JOptionPane.showInputDialog(null, "Segunda dimensão:"));
		
		//Atribuição dos valores das dimensões
		forma.setDimensao1(d1);
		forma.setDimensao2(d2);
		
		quadrado.setDimensao1(d1);
		quadrado.setDimensao2(d2);
		
		triangulo.setDimensao1(d1);
		triangulo.setDimensao2(d2);
		
		//Exibição dos dados
		forma.mostraDados();
		quadrado.area();
		triangulo.area();
		
	}

}

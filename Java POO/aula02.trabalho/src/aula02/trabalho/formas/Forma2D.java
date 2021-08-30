package aula02.trabalho.formas;

import javax.swing.JOptionPane;

public class Forma2D { //SuperClasse

	private Double dimensao1;
	private Double dimensao2;
	
	Forma2D() {
		
	}
	
	//---------------------------------------Sobrecarga de Métodos-------------------------------------------//
	public void area() {
		double area = this.getDimensao1() * this.getDimensao2();
		JOptionPane.showMessageDialog(null, "Área da forma 2d: " + area, "Área", JOptionPane.PLAIN_MESSAGE);
	}
	
	public void area(double d1, double d2) {
		double area = d1 * d2;
		JOptionPane.showMessageDialog(null, "Área da forma 2d: " + area, "Área", JOptionPane.PLAIN_MESSAGE);
	}
	//-------------------------------------------------------------------------------------------------------//
	
	public void mostraDados() {
		JOptionPane.showMessageDialog(null, "Primeira dimensão: " + this.getDimensao1() + "\nSegunda dimensão: " + 
									  this.getDimensao2(), "DADOS DA SUPERCLASSE - GRUPO 1", JOptionPane.PLAIN_MESSAGE);
	}

	public Double getDimensao1() {
		return dimensao1;
	}

	public void setDimensao1(double dimensao1) {
		this.dimensao1 = dimensao1;
	}

	public Double getDimensao2() {
		return dimensao2;
	}

	public void setDimensao2(double dimensao2) {
		this.dimensao2 = dimensao2;
	}

}

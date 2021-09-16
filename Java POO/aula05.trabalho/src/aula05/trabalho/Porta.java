//Aluno: Antonio Gomes Ferreira Neto
//Matrícula: 202102570735

package aula05.trabalho;

import java.util.Scanner;

public class Porta extends Casa {
	
	private double altura;
	private double largura;
	private String material;

	Porta() {
		
	}
	
	Porta(String cor) {
		this.setCor(cor);
	}
	
	Porta(String cor, double tamanho) {
		this.setCor(cor);
		this.setTamanho(tamanho);
	}
	
	Porta(String cor, double tamanho, double altura) {
		this.setCor(cor);
		this.setTamanho(tamanho);
		this.setAltura(altura);
	}
	
	Porta(String cor, double tamanho, double altura, double largura) {
		this.setCor(cor);
		this.setTamanho(tamanho);
		this.setAltura(altura);
		this.setLargura(largura);
	}
	
	Porta(String cor, double tamanho, double altura, double largura, String material) {
		this.setCor(cor);
		this.setTamanho(tamanho);
		this.setAltura(altura);
		this.setLargura(largura);
		this.setMaterial(material);
	}
	
	@Override
	public void entradaDados() {
		Scanner teclado = new Scanner(System.in);
		
		System.out.println("Digite a cor: ");
		String cor = teclado.nextLine();
		
		System.out.println("Digite o tamanho: ");
		double tamanho = teclado.nextDouble();
		
		System.out.println("Digite o material: ");
		String material = teclado.nextLine();
		
		System.out.println("Digite a altura: ");
		double altura = teclado.nextDouble();
		
		System.out.println("Digite a largura: ");
		double largura = teclado.nextDouble();
		
		this.setCor(cor);
		this.setTamanho(tamanho);
		this.material = material;
		this.setAltura(altura);
		this.setLargura(largura);
		
		teclado.close();
	}
	
	public double getAltura() {
		return altura;
	}

	public void setAltura(double altura) {
		this.altura = altura;
	}

	public double getLargura() {
		return largura;
	}

	public void setLargura(double largura) {
		this.largura = largura;
	}

	public String getMaterial() {
		return material;
	}

	public void setMaterial(String material) {
		this.material = material;
	}
	
	@Override
	public String toString() {
		return "Cor da Porta: " + this.getCor() + "Tamanho: " + this.getTamanho() + "\nMaterial: " + this.getMaterial() + "\nAltura: " + this.getAltura() + "\nLargura: " + this.getLargura();
	}
}

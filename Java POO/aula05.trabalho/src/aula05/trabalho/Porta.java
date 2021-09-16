//Aluno: Antonio Gomes Ferreira Neto
//Matrícula: 202102570735

package aula05.trabalho;

import java.util.Scanner;

public class Porta extends Casa {
	
	private double altura;
	private double largura;
	private String material;

	//Construtores
	Porta() {
		
	}
	
	Porta(String cor) {
		super(cor);
	}
	
	Porta(String cor, double tamanho) {
		super(cor, tamanho);
	}
	
	Porta(String cor, double tamanho, double altura) {
		this(cor, tamanho);
		this.setAltura(altura);
	}
	
	Porta(String cor, double tamanho, double altura, double largura) {
		this(cor, tamanho, altura);
		this.setLargura(largura);
	}
	
	Porta(String cor, double tamanho, double altura, double largura, String material) {
		this(cor, tamanho, altura, largura);
		this.setMaterial(material);
	}
	
	//Sobrescrita do método de entrada de dados
	@Override
	public void entradaDados() {
		@SuppressWarnings("resource")
		Scanner teclado = new Scanner(System.in);
		
		System.out.println("=======Entrada de dados para a Porta=======");
		System.out.println("Digite a cor: ");
		String cor = teclado.nextLine();
		
		System.out.println("Digite o tamanho: ");
		double tamanho = teclado.nextDouble();
		
		System.out.println("Digite o material: ");
		String material = teclado.next();
		
		System.out.println("Digite a altura: ");
		double altura = teclado.nextDouble();
		
		System.out.println("Digite a largura: ");
		double largura = teclado.nextDouble();
		
		
		this.setCor(cor);
		this.setTamanho(tamanho);
		this.setMaterial(material);
		this.setAltura(altura);
		this.setLargura(largura);
		
	}
	
	//Getters e Setters
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
	
	//Sobrescrita do método toString
	@Override
	public String toString() {
		return "Cor da Porta: " + this.getCor() + "\nTamanho: " + this.getTamanho() + "\nMaterial: " + this.getMaterial() + "\nAltura: " + this.getAltura() + "\nLargura: " + this.getLargura();
	}
}

//Aluno: Antonio Gomes Ferreira Neto
//Matrícula: 202102570735

package aula05.trabalho;

import java.util.Scanner;

public class Parede extends Casa {
	
	private String localizacao;
	private double altura;

	//Construtores
	Parede() {
		
	}
	
	Parede(String cor) {
		super(cor);
	}
	
	Parede(String cor, double tamanho) {
		super(cor, tamanho);
	}
	
	Parede(String cor, double tamanho, String localizacao) {
		this(cor, tamanho);
		this.setLocalizacao(localizacao);
	}
	
	Parede(String cor, double tamanho, String localizacao, double altura) {
		this(cor, tamanho, localizacao);
		this.setAltura(altura);
		
	}
	
	//Sobrescrita do método de entrada de dados
	@Override
	public void entradaDados() {
		@SuppressWarnings("resource")
		Scanner teclado = new Scanner(System.in);
		
		System.out.println("=======Entrada de dados para a Parede=======");
		System.out.println("Digite a cor: ");
		String cor = teclado.next();
		
		System.out.println("Digite o tamanho: ");
		double tamanho = teclado.nextDouble();
		
		System.out.println("Digite a localização: ");
		String localizacao = teclado.next();
		
		System.out.println("Digite a altura: ");
		double altura = teclado.nextDouble();
		
		
		this.setCor(cor);
		this.setTamanho(tamanho);
		this.setLocalizacao(localizacao);
		this.setAltura(altura);
		
	}
	
	//Getters e Setters
	public String getLocalizacao() {
		return localizacao;
	}

	public void setLocalizacao(String localizacao) {
		this.localizacao = localizacao;
	}

	public double getAltura() {
		return altura;
	}

	public void setAltura(double altura) {
		this.altura = altura;
	}

	//Sobrescrita do método toString
	@Override
	public String toString() {
		return "Cor da Porta: " + this.getCor() + "\nTamanho: " + this.getTamanho() + "\nLocalização: " + this.getLocalizacao() + "\nAltura: " + this.getAltura();
	}
	
}

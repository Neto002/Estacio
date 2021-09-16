//Aluno: Antonio Gomes Ferreira Neto
//Matrícula: 202102570735

package aula05.trabalho;

import java.util.Scanner;

public class Janela extends Casa {

	private String dimensao;
	private String material;
	
	//Construtores
	Janela() {
		
	}
	
	Janela(String cor) {
		super(cor);
	}
	
	Janela(String cor, double tamanho) {
		super(cor, tamanho);
	}
	
	Janela(String cor, double tamanho, String dimensao) {
		super(cor, tamanho);
		this.setDimensao(dimensao);
	}
	
	Janela(String cor, double tamanho, String dimensao, String material) {
		this(cor, tamanho, dimensao);
		this.setMaterial(material);
	}
	
	//Sobrescrita do método de entrada de dados
	@Override
	public void entradaDados() {
		@SuppressWarnings("resource")
		Scanner teclado = new Scanner(System.in);
		
		System.out.println("=======Entrada de dados para a Janela=======");
		System.out.println("Digite a cor: ");
		String cor = teclado.next();
		
		System.out.println("Digite o tamanho: ");
		double tamanho = teclado.nextDouble();
		
		System.out.println("Digite a dimensão: ");
		String dimensao = teclado.next();
		
		System.out.println("Digite o material: ");
		String material = teclado.next();
		
		
		this.setCor(cor);
		this.setTamanho(tamanho);
		this.setDimensao(dimensao);
		this.setMaterial(material);
		
	}

	//Getters e Setters
	public String getDimensao() {
		return dimensao;
	}

	public void setDimensao(String dimensao) {
		this.dimensao = dimensao;
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
		return "Cor da Janela: " + this.getCor() + "\nTamanho: " + this.getTamanho() + "\nDimensão: " + this.getDimensao() + "\nMaterial: " + this.getMaterial();
	}
	
}

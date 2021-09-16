//Aluno: Antonio Gomes Ferreira Neto
//Matrícula: 202102570735

package aula05.trabalho;

import java.util.Scanner;

public class Janela extends Casa {

	private String dimensao;
	private String material;
	
	Janela() {
		
	}
	
	Janela(String dimensao) {
		this.dimensao = dimensao;
	}
	
	Janela(String dimensao, String material) {
		this.dimensao = dimensao;
		this.material = material;
	}
	
	Janela(String dimensao, String material, String cor) {
		this.dimensao = dimensao;
		this.material = material;
		this.setCor(cor);
	}
	
	Janela(String dimensao, String material, String cor, double tamanho) {
		this.dimensao = dimensao;
		this.material = material;
		this.setCor(cor);
		this.setTamanho(tamanho);
	}
	
	@Override
	public void entradaDados() {
		Scanner teclado = new Scanner(System.in);
		
		System.out.println("Digite a cor: ");
		String cor = teclado.nextLine();
		
		System.out.println("Digite o tamanho: ");
		double tamanho = teclado.nextDouble();
		
		System.out.println("Digite a dimensão: ");
		String dimensao = teclado.nextLine();
		
		System.out.println("Digite o material: ");
		String material = teclado.nextLine();
		
		this.setCor(cor);
		this.setTamanho(tamanho);
		this.setDimensao(dimensao);
		this.setMaterial(material);
		
		teclado.close();
	}

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
	
	@Override
	public String toString() {
		return "Cor da Janela: " + this.getCor() + "Tamanho: " + this.getTamanho() + "\nDimensão: " + this.dimensao + "\nMaterial: " + this.material;
	}
	
}

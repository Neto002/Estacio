//Aluno: Antonio Gomes Ferreira Neto
//Matrícula: 202102570735

package aula05.trabalho;

import java.util.Scanner;

public class Casa {

	private String cor;
	private double tamanho;
	private Janela janela;
	private Porta porta;
	private Parede parede;
	
	//Construtores
	Casa() {
		
	}
	
	Casa(String cor) {
		this.setCor(cor);
	}
	
	Casa(String cor, double tamanho) {
		this(cor);
		this.setTamanho(tamanho);
	}
	
	Casa(String cor, double tamanho, Janela janela) {
		this(cor, tamanho);
		this.setJanela(janela);
	}
	
	Casa(String cor, double tamanho, Janela janela, Porta porta) {
		this(cor, tamanho, janela);
		this.setPorta(porta);
	}
	
	Casa(String cor, double tamanho, Janela janela, Porta porta, Parede parede) {
		this(cor, tamanho, janela, porta);
		this.setParede(parede);
	}
	
	//Método para entrada de dados
	public void entradaDados() {
		@SuppressWarnings("resource")
		Scanner teclado = new Scanner(System.in);
		
		System.out.println("=======Entrada de dados para a Casa=======");
		System.out.println("Digite a cor: ");
		String cor = teclado.next();
		
		System.out.println("Digite o tamanho: ");
		double tamanho = teclado.nextDouble();
		
		
		this.setCor(cor);
		this.setTamanho(tamanho);
		
	}

	//Getters e Setters
	public String getCor() {
		return cor;
	}

	public void setCor(String cor) {
		this.cor = cor;
	}

	public double getTamanho() {
		return tamanho;
	}

	public void setTamanho(double tamanho) {
		this.tamanho = tamanho;
	}

	public Janela getJanela() {
		return janela;
	}

	public void setJanela(Janela janela) {
		this.janela = janela;
	}

	public Porta getPorta() {
		return porta;
	}

	public void setPorta(Porta porta) {
		this.porta = porta;
	}

	public Parede getParede() {
		return parede;
	}

	public void setParede(Parede parede) {
		this.parede = parede;
	}
	
	//Sobrescrita do método toString
	@Override
	public String toString() {
		return "\n====================== Informações da casa ======================\nCor: " + this.getCor() + "\nTamanho: " + this.getTamanho() + 
				"\n--------Janela--------\n" + this.getJanela() + "\n--------Porta--------\n" + this.getPorta() + "\n--------Parede--------\n" + 
				this.getParede() + "\n=================================================================";
	}
	
}

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
	
	Casa() {
		
	}
	
	Casa(String cor) {
		this.setCor(cor);
	}
	
	Casa(String cor, double tamanho) {
		this.setCor(cor);
		this.setTamanho(tamanho);
	}
	
	Casa(String cor, double tamanho, Janela janela) {
		this.setCor(cor);
		this.setTamanho(tamanho);
		this.setJanela(janela);
	}
	
	Casa(String cor, double tamanho, Janela janela, Porta porta) {
		this.setCor(cor);
		this.setTamanho(tamanho);
		this.setJanela(janela);
		this.setPorta(porta);
	}
	
	Casa(String cor, double tamanho, Janela janela, Porta porta, Parede parede) {
		this.setCor(cor);
		this.setTamanho(tamanho);
		this.setJanela(janela);
		this.setPorta(porta);
		this.setParede(parede);
	}
	
	public void entradaDados() {
		Scanner teclado = new Scanner(System.in);
		
		System.out.println("Digite a cor: ");
		String cor = teclado.nextLine();
		
		System.out.println("Digite o tamanho: ");
		double tamanho = teclado.nextDouble();
		
		this.setCor(cor);
		this.setTamanho(tamanho);
		
		teclado.close();
	}

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
	
	@Override
	public String toString() {
		return "Casa\nCor: " + this.getCor() + "\nTamanho: " + this.getTamanho() + "\nJanela: \n" + this.getJanela() + "\nPorta: \n" + this.getPorta() + "\nParede: \n" + this.getParede();
	}
	
}

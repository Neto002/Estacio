package aula03;

public class Cliente {

	private long mat;
	private String nome;
	
	Cliente(long mat, String nome) {
		this.mat = mat;
		this.nome = nome;
	}
	
	public String toString() {
		return "Matrícula: " + this.mat + ", Nome: " + this.nome + ";";
	}
	
}

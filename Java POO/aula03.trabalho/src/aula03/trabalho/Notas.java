package aula03.trabalho;

public class Notas {

	private String nome;
	private String dataCriacao;
	private String informacao;
	
	Notas(String nome, String data, String info) {
		this.setNome(nome);
		this.setDataCriacao(data);
		this.setInformacao(info);
	}
	
	Notas() {
		
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getDataCriacao() {
		return dataCriacao;
	}

	public void setDataCriacao(String dataCriacao) {
		this.dataCriacao = dataCriacao;
	}

	public String getInformacao() {
		return informacao;
	}

	public void setInformacao(String informacao) {
		this.informacao = informacao;
	}

	@Override
	public String toString() {
		return "Nome: " + this.getNome() + ", Data de criação: " + this.getDataCriacao() + ", Informação: " + this.getInformacao();
	}
	
	
	
}

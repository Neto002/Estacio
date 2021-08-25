package aula01;

public class Aluno { //Classe Construtora
	
	private Long matriculaAluno;
	private String nomeAluno;
	
	Aluno() {
		
	}
	
	Aluno(long matricula, String nome) {
		this.setMatriculaAluno(matricula);
		this.setNomeAluno(nome);
	}
	
	public Long getMatriculaAluno() {
		return this.matriculaAluno;
	}
	
	public String getNomeAluno() {
		return this.nomeAluno;
	}
	
	public void setMatriculaAluno(Long m) {
		this.matriculaAluno = m;
	}
	
	public void setNomeAluno(String n) {
		this.nomeAluno = n;
	}
	
	@Override
	public String toString() {
		return "Nome do aluno: " + this.getNomeAluno() + "\nMatrícula: " + this.getMatriculaAluno();
	}
	
}

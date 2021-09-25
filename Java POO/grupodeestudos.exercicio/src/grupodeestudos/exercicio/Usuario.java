package grupodeestudos.exercicio;

public class Usuario {

	protected int matricula;
	protected String nome;
	protected int idade;
	protected String cargo;
	
	
	Usuario() {
		
	}
	
	Usuario(int matricula, String nome, int idade) {
		this.matricula = matricula;
		this.nome = nome;
		this.idade = idade;
		this.cargo = "Usuário comum";
	}
	
	public void status() {
		System.out.println("Nome: " + this.nome + "\nMatrícula: " + this.matricula + "\nIdade: " + this.idade + "\nCargo: " + this.cargo);
	}

	public int getMatricula() {
		return matricula;
	}

	public void setMatricula(int matricula) {
		this.matricula = matricula;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public int getIdade() {
		return idade;
	}

	public void setIdade(int idade) {
		this.idade = idade;
	}
	
	public String getCargo() {
		return this.cargo;
	}
	
	public void setCargo(String cargo) {
		this.cargo = cargo;
	}
	
}

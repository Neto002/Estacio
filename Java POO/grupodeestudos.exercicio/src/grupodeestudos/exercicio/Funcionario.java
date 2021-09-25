package grupodeestudos.exercicio;

public class Funcionario extends Usuario {

	private String setor;
	
	Funcionario() {
		
	}

	public String getSetor() {
		return setor;
	}

	public void setSetor(String setor) {
		this.setor = setor;
	}
	
	@Override
	public void status() {
		System.out.println("Nome: " + this.nome + "\nMatrícula: " + this.matricula + "\nIdade: " + this.idade + "\nCargo: " + this.cargo + "\nSetor: " + this.setor);
	}
	
}

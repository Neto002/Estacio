package av2;


public class Cadastro {

	public static void main(String[] args) {
		Funcionario funcionario = new Funcionario();
		funcionario.nome = "Antonio Gomes Ferreira Neto";
		funcionario.matricula = "202102570735";
		
		System.out.println("Nome: " + funcionario.nome + "\nMatrícula: " + funcionario.matricula);
	}

}

package av2;

public class Programa {

	public static void main(String[] args) {
		
		Aluno aluno = new Aluno();
		
		aluno.nome = "Antonio Gomes Ferreira Neto";
		aluno.matricula = "202102570735";
		
		System.out.println("Nome: " + aluno.nome + "\nMatrícula: " + aluno.matricula);
	}

}

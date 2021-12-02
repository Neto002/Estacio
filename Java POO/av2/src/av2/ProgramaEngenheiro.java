package av2;

public class ProgramaEngenheiro {

	public static void main(String[] args) {
		Engenheiro eg = new Engenheiro(202102570735L, "Antonio Gomes Ferreira Neto", "Engenheiro Civil");
		System.out.println("Nome: " + eg.nome + "\nMatrícula: " + eg.matricula + "\nTitulação: " + eg.titulacao);
	}

}

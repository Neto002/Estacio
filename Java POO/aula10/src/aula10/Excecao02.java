package aula10;

public class Excecao02 {

	public static void main(String[] args) {

		try {
			maiuscula(null);
		} catch (NullPointerException e) {
			System.out.println("Frase nula, atribuindo uma frase padrão...");
			maiuscula("Frase padrão");
		}
		
	}

	private static void maiuscula(String frase) throws NullPointerException {
		String novaFrase = frase.toUpperCase();
		System.out.println("Frase antiga: " + frase + "\nFrase nova: " + novaFrase);
	}
	
}

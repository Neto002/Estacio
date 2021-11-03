package aula11;

public class BancoDados implements Runnable {

	private int i;
	private static int cont = 0;
	
	public BancoDados() {
		cont++;
	}
	
	@Override
	public void run() {
		
		while (i <= 10) {
			System.out.println("Banco de Dados: " + i++);
		}
		
	}
}

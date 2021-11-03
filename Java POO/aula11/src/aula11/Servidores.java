package aula11;

public class Servidores implements Runnable{

	private int i;
	private static int cont = 0;
	
	public Servidores() {
		cont++;
	}
	@Override
	public void run() {
		
		while (i <= 10) {
			System.out.println("Servidores: " + i++);
		}
		
	}
}

package aula11;

public class ProgramaEstoque {

	public static void main(String[] args) {

		Runnable r1 = new Servidores();
		Runnable r2 = new BancoDados();
		Runnable r3 = new RequisicaoWeb();
		new Thread(r1).start();
		new Thread(r2).start();
		new Thread(r3).start();
		
	}

}

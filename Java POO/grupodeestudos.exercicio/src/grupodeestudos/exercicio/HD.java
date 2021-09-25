package grupodeestudos.exercicio;

public class HD extends Computador {
	
	String modelo;
	private int capacidade;
	double preco;
	
	HD(HD hd, Memoria ram, PlacaMae placa) {
		super(hd, ram, placa);
	}
	
	@Override
	public void imprimir() {
		super.imprimir();
		System.out.println("Modelo: " + this.modelo);
	}
	
	public int getCapacidade() {
		return capacidade;
	}
	public void setCapacidade(int capacidade) {
		this.capacidade = capacidade;
	}
}

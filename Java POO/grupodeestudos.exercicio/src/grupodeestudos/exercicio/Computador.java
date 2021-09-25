package grupodeestudos.exercicio;

public class Computador {
	private HD hd;
	Memoria ram;
	PlacaMae placa;
	
	Computador() {
		//hd = new HD();
		ram = new Memoria();
		placa = new PlacaMae();
	}
	
	Computador(HD hd, Memoria ram, PlacaMae placa) {
		this.hd = hd;
		this.ram = ram;
		this.placa = placa;
	}
	
	public void imprimir() {
		System.out.println(this.hd + "\n" + this.ram);
	}

	public HD getHd() {
		return hd;
	}

	public void setHd(HD hd) {
		this.hd = hd;
	}
}

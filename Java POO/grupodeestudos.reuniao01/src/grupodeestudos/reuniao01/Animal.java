package grupodeestudos.reuniao01;

public class Animal {
	protected String corPelo;
	protected double tamanho;
	
	Animal() {
		
	}
	
	Animal(String corPelo, double tamanho) {
		this.corPelo = corPelo;
		this.tamanho = tamanho;
	}

	public String getCorPelo() {
		return corPelo;
	}

	public void setCorPelo(String corPelo) {
		this.corPelo = corPelo;
	}

	public double getTamanho() {
		return tamanho;
	}

	public void setTamanho(double tamanho) {
		this.tamanho = tamanho;
	}
	
	public void emitirSom() {
		System.out.println("Animal não especificado");
	}
}

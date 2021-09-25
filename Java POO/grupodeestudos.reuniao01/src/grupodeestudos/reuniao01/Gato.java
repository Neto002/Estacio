package grupodeestudos.reuniao01;

public class Gato extends Animal {
	//--------------- Sobrecarga de métodos -------------------//
	Gato() {
		
	}
	
	Gato(String corPelo) {
		this.corPelo = corPelo;
	}
	
	Gato(String corPelo, double tamanho) {
		this.corPelo = corPelo;
		this.tamanho = tamanho;
	}
	//-------------------------------------------------------//
	
	//Sobrescrita
	@Override
	public void emitirSom() {
		System.out.println("miau");
	}
}

package grupodeestudos.reuniao01;

public class Cachorro extends Animal {
	
	Cachorro() {
		
	}
	
	Cachorro(String corPelo, double tamanho) {
		this.corPelo = corPelo;
		this.tamanho = tamanho;
	}
	
	@Override
	public void emitirSom() {
		System.out.println("au au");
	}
	
}

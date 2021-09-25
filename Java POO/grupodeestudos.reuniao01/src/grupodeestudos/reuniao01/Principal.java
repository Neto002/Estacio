package grupodeestudos.reuniao01;

public class Principal { //Instanciadora

	public static void main(String[] args) {

		Animal animal = new Animal();
		animal.emitirSom();
		
		Cachorro cachorro = new Cachorro("Preto", 1);
		cachorro.emitirSom();
		
		Gato gato = new Gato("Branco", 0.5);
		gato.emitirSom();
		
	}

}

package teste.raphael;

public class Nota {

	String nome;
	String data;
	String info;
	
	Nota() {

	}
	
	@Override
	public String toString() {
		return "Nome: " + this.nome + ", Data: " + this.data + ", Informa��o: " + this.info;
	}
}

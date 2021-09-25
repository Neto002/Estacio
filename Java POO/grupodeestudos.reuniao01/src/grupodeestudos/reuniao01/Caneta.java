package grupodeestudos.reuniao01;

public class Caneta { //Construtora
	
	private String corTampa;
	private String corTinta;
	private float tamanhoPonta;
	
	//Construtor vazio
	public Caneta() {
		
	}
	
	//Construtor cheio
	public Caneta(String corTampa, String corTinta) {
		this.corTampa = corTampa;
		this.corTinta = corTinta;
	}
	
	public void escrever() {
		System.out.println("a caneta está escrevendo em tinta " + this.corTinta);
	}
	
	public void setCorTampa(String cor) {
		this.corTampa = cor;
	}
	
	public String getCorTampa() {
		return this.corTampa;
	}

	public String getCorTinta() {
		return corTinta;
	}

	public void setCorTinta(String corTinta) {
		this.corTinta = corTinta;
	}

	public float getTamanhoPonta() {
		return tamanhoPonta;
	}

	public void setTamanhoPonta(float tamanhoPonta) {
		this.tamanhoPonta = tamanhoPonta;
	}
	
}

//Antonio Gomes Ferreira Neto
//Matrícula: 202102570735

package av2;

public class Engenheiro extends Pessoa {
	
	String titulacao;
	public Engenheiro(Long matricula, String nome, String titulacao) {
		super(matricula, nome);
		this.titulacao = titulacao;
	}

}

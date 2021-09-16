//Aluno: Antonio Gomes Ferreira Neto
//Matrícula: 202102570735

package aula05.trabalho;

public class Programa {

	public static void main(String[] args) {
		
		Casa casa = new Casa();
		Janela janela = new Janela();
		Porta porta = new Porta();
		Parede parede = new Parede();
		
		casa.entradaDados();
		janela.entradaDados();
		porta.entradaDados();
		
		
		parede.entradaDados();
		
		casa.setJanela(janela);
		casa.setPorta(porta);
		casa.setParede(parede);
		
		System.out.println(casa);
		
	}
	
}

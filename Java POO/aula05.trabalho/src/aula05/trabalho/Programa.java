//Aluno: Antonio Gomes Ferreira Neto
//Matrícula: 202102570735

package aula05.trabalho;

public class Programa {

	public static void main(String[] args) {
		
		//Instanciando os objetos
		Casa casa = new Casa();
		Janela janela = new Janela();
		Porta porta = new Porta();
		Parede parede = new Parede();
		
		
		//Entrada de Dados para os objetos
		casa.entradaDados();
		janela.entradaDados();
		porta.entradaDados();
		parede.entradaDados();
		
		//Adicionando os objetos à Casa
		casa.setJanela(janela);
		casa.setPorta(porta);
		casa.setParede(parede);
		
		//Mostrando os dados dos objetos
		System.out.println(casa);
		
	}
	
}

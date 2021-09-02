package aula03;

import java.util.ArrayList;
import java.util.List;

public class TestaCliente {
	public static void main(String[] args) {

		List<Cliente> listaClientes = new ArrayList<Cliente>();
		
		//Instanciando objetos da classe Cliente
		Cliente cl1 = new Cliente(202102570735l, "Antonio Neto");
		Cliente cl2 = new Cliente(202102580845l, "Bruno");
		
		//Adicionando elementos à lista
		listaClientes.add(cl1);
		listaClientes.add(cl2);
		
		//Exibindo lista
		System.out.println(listaClientes);
		
		//Removendo um elemento da lista
		listaClientes.remove(cl2);
		
		System.out.println(listaClientes);
		
	}
}

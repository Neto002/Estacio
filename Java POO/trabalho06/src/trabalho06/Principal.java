package trabalho06;

public class Principal {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		ContaBancaria contaBancaria = new ContaBancaria();
		
		System.out.println("Testando a exibição da data de abertura formatada e o saldo formatado: ");
		System.out.println("Data de Abertura: " + contaBancaria.getDataAberturaFormatada());
		System.out.println("Saldo: " + contaBancaria.getSaldoFormatado());
		System.out.println("Teste de depósito de R$200,00:");
		contaBancaria.depositar(200);
		System.out.println("Depósito realizado, saldo atualizado: " + contaBancaria.getSaldoFormatado());
		System.out.println("Teste de saque com valor de R$250,00 (maior que o saldo): ");
		contaBancaria.sacar(250);
		System.out.println("Teste de saque com valor de R$190,00 (menor que o saldo):");
		contaBancaria.sacar(190);
		System.out.println("Saque realizado, saldo atualizado: " + contaBancaria.getSaldoFormatado());
		
	}

}

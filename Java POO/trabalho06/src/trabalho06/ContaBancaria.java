package trabalho06;

import java.text.DateFormat;
import java.util.Date;

public class ContaBancaria {

	private double saldo = 0;
	private Date dataAbertura;
	
	public ContaBancaria() {
		this.saldo = 0;
		this.dataAbertura = new Date();
	}

	public double getSaldo() {
		return saldo;
	}

	public void setSaldo(double saldo) {
		this.saldo = saldo;
	}

	public Date getDataAbertura() {
		return dataAbertura;
	}
	
	public String getDataAberturaFormatada() {
		String dataFormatada = DateFormat.getDateInstance(DateFormat.SHORT).format(dataAbertura);
		return dataFormatada;
	}
	
	public String getSaldoFormatado() {
		String saldoFormatado = String.format("R$%.2f", this.saldo);
		return saldoFormatado;
	}
	
	public void depositar(double valorDeposito) {
		if (valorDeposito > 0) {
			this.saldo = this.saldo + valorDeposito;
		}
	}
	
	public void sacar(double valorSaque) {
		if (valorSaque > this.saldo) {
			System.out.println("O valor desejado não está disponível na conta. Saldo: " + this.getSaldoFormatado());
		} else {
			this.saldo = this.saldo - valorSaque;
		}
	}
	
}

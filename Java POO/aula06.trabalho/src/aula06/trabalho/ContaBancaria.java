/*
 * Aluno: Antonio Gomes Ferreira Neto
 * Matrícula: 202102570735
 */
package aula06.trabalho;

import java.text.DateFormat;
import java.text.DecimalFormat;
import java.text.SimpleDateFormat;
import java.util.Scanner;
import java.util.Date;

public class ContaBancaria {
	//Atributos
	private double saldo;
	private final Date dataAbertura;
	
	//Construtor
	ContaBancaria() {
		this.saldo = 0.00;
		this.dataAbertura = new Date(System.currentTimeMillis());
	}
	
	//Método para depósitos
	public void depositar(double deposito) {
		this.setSaldo(this.getSaldo() + deposito);
		System.out.println("Saldo após depósito: " + this.getSaldoFormatado());
	}
	
	//Método para saques
	public void sacar(double saque) {
		while (true) {
			if (saque > this.getSaldo()) {
				Scanner teclado = new Scanner(System.in);
				System.out.println("Não é possível sacar o valor desejado pois não há saldo suficiente para a operação. Saldo disponível: " + 
									this.getSaldoFormatado());
				System.out.println("Por favor, digite um valor válido: ");
				saque = teclado.nextDouble();
			} else {
				this.setSaldo(this.getSaldo() - saque);
				System.out.println("Saque efetivado com sucesso. Saldo disponível: " + this.getSaldoFormatado());
				break;
			}
		}
	}
	
	//Getters e Setters
	public void setSaldo(double saldo) {
		this.saldo = saldo;
	}
	
	public double getSaldo() {
		return this.saldo;
	}
	
	public Date getDataAbertura() {
		return this.dataAbertura;
	}
	
	//Método de Retorno do Saldo formatado
	public String getSaldoFormatado() {
		String saldoFormatado = new DecimalFormat("R$ #,##0.00").format(this.getSaldo());
		return saldoFormatado;
	}
	
	//Método de Retorno da Data de Abertura formatada
	public String getDataAberturaFormatada() {
		SimpleDateFormat dataAberturaFormatada = new SimpleDateFormat("dd/MM/yyyy");
		//return DateFormat.getDateInstance(DateFormat.SHORT).format(dataAbertura); ou
		return dataAberturaFormatada.format(this.dataAbertura);
	}
	
}

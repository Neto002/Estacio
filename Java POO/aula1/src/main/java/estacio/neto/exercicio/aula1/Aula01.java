package estacio.neto.exercicio.aula1;

public class Aula01 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
	}

	public class Sala {
		
		private String disciplina;
		private int turma;
		private String curso;
		private String professor;
		private int quantidadeAlunos;
		
		Sala() {
			
		}
		
		public String getDisciplina() {
			return disciplina;
		}
		public void setDisciplina(String disciplina) {
			this.disciplina = disciplina;
		}
		public int getTurma() {
			return turma;
		}
		public void setTurma(int turma) {
			this.turma = turma;
		}
		public String getCurso() {
			return curso;
		}
		public void setCurso(String curso) {
			this.curso = curso;
		}
		public String getProfessor() {
			return professor;
		}
		public void setProfessor(String professor) {
			this.professor = professor;
		}
		public int getQuantidadeAlunos() {
			return quantidadeAlunos;
		}
		public void setQuantidadeAlunos(int quantidadeAlunos) {
			this.quantidadeAlunos = quantidadeAlunos;
		}
	}
	
	public class Controlador {
		
		private int quantidadeCaminhoes;
		private int quantidadeMotoristas;
		private String localizacaoCaminhoes;
		private String estoque;
		
		Controlador() {
			
		}
		
		public int getQuantidadeCaminhoes() {
			return quantidadeCaminhoes;
		}
		public void setQuantidadeCaminhoes(int quantidadeCaminhoes) {
			this.quantidadeCaminhoes = quantidadeCaminhoes;
		}
		public int getQuantidadeMotoristas() {
			return quantidadeMotoristas;
		}
		public void setQuantidadeMotoristas(int quantidadeMotoristas) {
			this.quantidadeMotoristas = quantidadeMotoristas;
		}
		public String getLocalizacaoCaminhoes() {
			return localizacaoCaminhoes;
		}
		public void setLocalizacaoCaminhoes(String localizacaoCaminhoes) {
			this.localizacaoCaminhoes = localizacaoCaminhoes;
		}
		public String getEstoque() {
			return estoque;
		}
		public void setEstoque(String estoque) {
			this.estoque = estoque;
		}
	}
}

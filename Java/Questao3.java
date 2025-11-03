// Questão 3 - Herança
public class Questao3 {

    // Classe base 
    static class Pessoa {
        protected String nome; // 
    }

    // Classe Aluno herda de Pessoa
    static class Aluno extends Pessoa {
        private String curso;

        public String getCurso() {
            return curso;
        }

        public void setCurso(String curso) {
            this.curso = curso;
        }
    }

    // Classe Professor 
    static class Professor extends Pessoa {
        private String disciplina;

        public String getDisciplina() {
            return disciplina;
        }

        public void setDisciplina(String disciplina) {
            this.disciplina = disciplina;
        }
    }

    public static void main(String[] args) {
        // Criando objeto Aluno
        Aluno aluno = new Aluno();
        aluno.nome = "Jonatha Lopes";
        aluno.setCurso("Análise e Desenvolvimento de Sistemas");

        // Criando objeto Professor
        Professor prof = new Professor();
        prof.nome = "Carlos Mendes";
        prof.setDisciplina("Programação Orientada a Objetos");

        // Exibindo informações
        System.out.println("=== Dados do Aluno ===");
        System.out.println("Nome: " + aluno.nome);
        System.out.println("Curso: " + aluno.getCurso());

        System.out.println("\n=== Dados do Professor ===");
        System.out.println("Nome: " + prof.nome);
        System.out.println("Disciplina: " + prof.getDisciplina());
    }
}

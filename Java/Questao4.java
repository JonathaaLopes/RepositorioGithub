// Questão 4 - Polimorfismo
public class Questao4 {

    // Superclasse Pessoa
    static class Pessoa {
        protected String nome;

        // Método
        public String apresentar() {
            return "Olá, meu nome é " + nome;
        }
    }

    // Classe Aluno
    static class Aluno extends Pessoa {
        private String curso;

        public Aluno(String nome, String curso) {
            this.nome = nome;
            this.curso = curso;
        }

        @Override
        public String apresentar() {
            return "Sou o aluno " + nome + " do curso de " + curso + ".";
        }
    }

    // Classe Professor
    static class Professor extends Pessoa {
        private String disciplina;

        public Professor(String nome, String disciplina) {
            this.nome = nome;
            this.disciplina = disciplina;
        }

        @Override
        public String apresentar() {
            return "Sou o professor " + nome + " e leciono " + disciplina + ".";
        }
    }

    public static void main(String[] args) {
        Pessoa aluno = new Aluno("Jonatha Lopes", "SUPERIOR DE TECNOLOGIA EM SISTEMAS PARA INTERNET");
        Pessoa professor = new Professor("Edmar Senne", "Programação Orientada a Objetos");

        // Chamando o mesmo método, mas com comportamentos diferentes (polimorfismo)
        System.out.println(aluno.apresentar());
        System.out.println(professor.apresentar());
    }
}

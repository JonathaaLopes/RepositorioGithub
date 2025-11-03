// Questão 2 - Encapsulamento
public class Questao2 {

    // Classe Aluno com atributos privados
    static class Aluno {
        private String nome;
        private String matricula;

        // Getter e Setter para nome
        public String getNome() {
            return nome;
        }
        public void setNome(String nome) {
            this.nome = nome;
        }

        // Getter e Setter para matrícula
        public String getMatricula() {
            return matricula;
        }
        public void setMatricula(String matricula) {
            this.matricula = matricula;
        }
    }

    public static void main(String[] args) {
        // Criando o objeto aluno
        Aluno aluno = new Aluno();

        // Usando os setters para inserir os dados
        aluno.setNome("Jonatha Lopes");
        aluno.setMatricula("54512555-5");

        // Alterando o nome (teste do encapsulamento)
        aluno.setNome("Jonatha A. Lopes");

        // Exibindo os dados
        System.out.println("Nome: " + aluno.getNome());
        System.out.println("Matrícula: " + aluno.getMatricula());
    }
}

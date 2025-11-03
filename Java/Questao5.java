// Questão 5 - Interface
public class Questao5 {

    // Interface
    interface Avaliado {
        String avaliarDesempenho();
    }

    // Classe Aluno 
    static class Aluno implements Avaliado {
        private String nome;

        public Aluno(String nome) {
            this.nome = nome;
        }

        @Override
        public String avaliarDesempenho() {
            return "Aluno " + nome + " obteve ótimas notas!";
        }
    }

    public static void main(String[] args) {
        Aluno aluno = new Aluno("Jonatha Lopes");
        System.out.println(aluno.avaliarDesempenho());
    }
}

public class Questao1 {
    
    // Classe Aluno com atributos públicos (serão encapsulados na questão 2)
    static class Aluno {
        public String nome;
        public String matricula;
    }
    
    public static void main(String[] args) {
        // Criando objeto Aluno com meus dados
        Aluno aluno = new Aluno();
        aluno.nome = "Jonatha Lopes";
        aluno.matricula = "54512555-5";
        
        // Exibindo dados no console
        System.out.println("Nome: " + aluno.nome);
        System.out.println("Matrícula: " + aluno.matricula);
    }
}



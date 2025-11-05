# 🧠 Colinha Git + GitHub (Simples e Direta)

## 🧩 Criar repositório no GitHub
1. Vá em [https://github.com/new](https://github.com/new)  
2. Dê um nome (ex: `Exercicio-de-Livros`)  
3. **Não marque nada** (deixe vazio)  
4. Clique em **Create repository**

---

## 📂 Iniciar o projeto no VS Code
Abra o terminal dentro da pasta do seu projeto (Ctrl + `):

```bash
git init
git add .
git commit -m "Primeiro commit"
git branch -M main
```

---

## 🌐 Conectar com o repositório do GitHub
Substitua o link pelo seu repositório:

```bash
git remote add origin https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
```

---

## 🚀 Enviar os arquivos para o GitHub
```bash
git push -u origin main
```

Se pedir login:
- Digite seu **usuário do GitHub**
- Use o **token pessoal de acesso** (não a senha)

---

## 💾 Atualizar o projeto depois
Quando fizer alterações:

```bash
git add .
git commit -m "Descrição das alterações"
git push
```

---

## 🔍 Verificar o que está conectado
```bash
git remote -v
git branch
```

---

## 🧹 Recomeçar do zero (caso precise)
```bash
rm -rf .git
git init
```

---

## 💡 Dica
Para **outros projetos**, repita **o mesmo processo** dentro da nova pasta e use o **link do repositório correspondente** do GitHub.

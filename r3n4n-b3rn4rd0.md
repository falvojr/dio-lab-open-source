# 🗡️ Solo Git Leveling — Painel do Caçador

Você é um caçador que despertou no mundo do **Git & GitHub**.  
Complete missões, ganhe XP, suba de rank e enfrente o Chefão Final: contribuir em Open Source.

---

## 📊 Status do Caçador
- **Rank Atual:** E-Rank 🐣
- **XP Atual:** 0 / 700 XP
- **Missões Concluídas:** 0 / 8
- **Progresso:** ![Progresso](https://progress-bar.dev/0/?scale=700&suffix=%20XP&width=400&color=blue)

---

## 🗺️ Missões

### 🥚 Missão 1 — Despertar (50 XP)
> Instalar Git e configurar nome/e-mail.

**Comandos:**
```bash
git --version
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"

mkdir meu-projeto
cd meu-projeto
git init
echo "# Meu Projeto" > README.md
git add README.md
git commit -m "Primeiro commit"

⚒️ Missão 2 — Forjar a Primeira Arma (70 XP)
Criar seu primeiro repositório local e fazer commit inicial.

Comandos:

bash
Copiar
Editar
mkdir meu-projeto
cd meu-projeto
git init
echo "# Meu Projeto" > README.md
git add README.md
git commit -m "Primeiro commit"
 Feita

🔍 Missão 3 — Ler o Campo de Batalha (60 XP)
Aprender a inspecionar mudanças.

Comandos:

bash
Copiar
Editar
git status
git diff
git log --oneline --graph
 Feita

🌿 Missão 4 — Caminhos Paralelos (80 XP)
Criar e mesclar branches.

Comandos:

bash
Copiar
Editar
git branch nova-skill
git checkout nova-skill
# faça alterações
git commit -m "Nova skill"
git checkout main
git merge nova-skill
 Feita

🌐 Missão 5 — Entrar na Guilda (100 XP)
Conectar repositório local ao GitHub e enviar código.

Comandos:

bash
Copiar
Editar
git remote add origin git@github.com:usuario/repositorio.git
git branch -M main
git push -u origin main
 Feita

📜 Missão 6 — Pedido ao Conselho (120 XP)
Criar Pull Request no GitHub.

Passos:

Criar branch local.

Commitar mudanças.

git push para nova branch.

Abrir PR no GitHub.

 Feita

⏳ Missão 7 — Manipular o Tempo (130 XP)
Rebasear commits e usar stash.

Comandos:

bash
Copiar
Editar
git rebase -i HEAD~3
git stash
git stash pop
 Feita

👑 Missão Final — Chefão Open Source (300 XP)
Contribuir em um projeto público no GitHub.

Passos:

Procurar good first issue.

Fazer fork e clone.

Criar branch → commit → push → PR.

 Feita

📈 Sistema de Ranks
Rank	XP Necessário	Título
E-Rank	0–100	Iniciante
D-Rank	101–200	Aprendiz
C-Rank	201–350	Guerreiro
B-Rank	351–500	Especialista
A-Rank	501–700	Mestre
S-Rank	701+	Lendário
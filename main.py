# Criar um banco de dados SQLite e uma tabela
import sqlite3

#Criar a conexão com o banco de  dados chamado de "escola.db"
conexao = sqlite3.connect("escola.db")

#Criar o objeto chamado de "cursor" que será usado para executar os comandos sql
cursor = conexao.cursor()

# #Criar uma tabela no banco 
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS alunos(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome TEXT NOT NULL,
#     idade INTEGER,
#     curso TEXT
# )        
# """)
# nome = input("Digite o nome do aluno: ").lower()
# idade = int(input("Digite a idade do aluno: "))
# curso = input("Digite o curso do aluno: ").lower()
# #Inserir um dado na tabela
# cursor.execute("""
# INSERT INTO alunos(nome, idade, curso)
# VALUES (?, ?, ?)     
# """,
# (nome, idade, curso)
# )

# #Confirmar as alterações no banco
# conexao.commit()

# #Inserir varios alunos de uma só vez
# alunos = [
#     ("Yago", 28, "Direito"),
#     ("Jessica", 24, "Computacão"),
#     ("Breno", 52, "Computação"),
# ]
# #executemany permite inserir múltiplas linhas  de uma só vez
# cursor.executemany("""
# INSERT INTO alunos(nome, idade, curso) 
# VALUES (?, ?, ?)                
# """,
# (alunos)
# )
# conexao.commit()


# #Atualizar dados no banco
# cursor.execute("""
# UPDATE alunos 
# SET idade = ?,curso = ?
# WHERE id = ?
# """,(25, "Biomedicina", 1)
# )
# conexao.commit()

#Função listar dados do banco
#Consultar os dados no banco
cursor.execute("SELECT * FROM alunos")
#fetchall traz todas as linhas da consulta
for linha in cursor.fetchall():
    print(f"ID: {linha[0]} | NOME: {linha[1]} | IDADE: {linha[2]} | CURSO: {linha[3]}")
print("-"*50)

pesquisar = input("Digite o curso que deseja pesquisar os alunos: ")
cursor.execute("SELECT nome, idade FROM alunos WHERE curso = ?", (pesquisar,))
print(f"Alunos do curso {pesquisar}")
for linha in cursor.fetchall():
    print(f"NOME: {linha[0]} | IDADE: {linha[1]}")

# Criar um banco de dados SQLite e uma tabela
import sqlite3

#Criar a conexão com o banco de  dados chamado de "escola.db"
conexao = sqlite3.connect("escola.db")

#Criar o objeto chamado de "cursor" que será usado para executar os comandos sql
cursor = conexao.cursor()


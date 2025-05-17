import sqlite3 

def conect_bd():
    conexao=sqlite3.connect("titulo.db")
    return conexao

def insere_dados(nome, ano, nota):
    conexao = conect_bd()
    cursor = conexao.cursor()
    cursor.execute(
        """
        INSERT INTO filmes (nome, ano, nota)
        VALUES (?, ?, ?)
        """,(nome, ano, nota)
    )
    conexao.commit()
    conexao.close()

def obter_dados():
    conexao = conect_bd()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM filmes")
    dados = cursor.fetchall()
    cursor.close()
    return dados
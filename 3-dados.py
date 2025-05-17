import sqlite3

conexao = sqlite3.connect("titulo.db")
cursor = conexao.cursor()

#inserindo dados

cursor.execute(
    """
        INSERT INTO filmes (nome,ano,nota)
        VALUES("homem arana",2020,8)
    """
)

conexao.commit()
conexao.close()
print("Dados inseridos com sucesso!")
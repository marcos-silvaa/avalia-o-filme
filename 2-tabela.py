import sqlite3

# Conectando no db
conexao = sqlite3.connect("titulo.db")
cursor = conexao.cursor()

# Criando a tabela

cursor.execute(
    """
        CREATE TABLE filmes(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            ano INTEGER NOT NULL,
            nota REAL NOT NULL
        );
    """
)

# Fechando a conexão 
conexao.close()
print("Tabela foi criada")
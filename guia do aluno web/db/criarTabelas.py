# Lembra que pra usar essa bomba tem que executar no terminal do VSCode aqui
# se não vai dar merda.
# Pra executar: "python criarTabelas.py".
import sqlite3

# Pra ele sempre achar o caminho
import os
bancoDados = os.getcwd()

# Tá achando o banco de dados.
conexao = sqlite3.connect("bancoDados.db")

# Conecto nele.
cursor = conexao.cursor()

# Parte que vai criar as tabelas todas do nosso banco de gagos.
cursor.executescript("""
CREATE TABLE usuario 
( 
    idUsuario INT PRIMARY KEY,  
    nome VARCHAR(100),  
    dataNasc DATE,  
    email VARCHAR(150),  
    senha VARCHAR(100),  
    tipoDeUser INT
); 

CREATE TABLE evento 
( 
    idEvento INT PRIMARY KEY,
    nome VARCHAR(100),
    descricao TEXT,
    data DATE,
    links TEXT,
    tipo INT
); 

CREATE TABLE agendar 
( 
    idUsuario INT,  
    idEvento INT,
    PRIMARY KEY (idUsuario, idEvento),
    FOREIGN KEY (idUsuario) REFERENCES usuario(idUsuario),
    FOREIGN KEY (idEvento) REFERENCES evento(idEvento)
); 

CREATE TABLE cadastra 
( 
    idUsuario INT,  
    idEvento INT,
    PRIMARY KEY (idUsuario, idEvento),
    FOREIGN KEY (idUsuario) REFERENCES usuario(idUsuario),
    FOREIGN KEY (idEvento) REFERENCES evento(idEvento)
); 
""")

# Vai salvar todas as alterações feitas nessa conexão de agora.
conexao.commit()
# Depois de salvar ele fecha a conexão.
conexao.close()

print("💔🥀 SYBAU 💔🥀")

# Manual caso eu esqueça:

# 1 - sqlite3.connect(): conectar no banco

# 2- cursor.execute() ou cursor.executescript(): rodar comandos SQL
# Quando for alterar alguma tabela é só rodar o comando usando essa função
# Ex: cursor.execute("""ALTER TABLE deepWoken ADD COLUMN sybau TEXT""")

# 3 - conexao.commit(): salvar alterações

# 4 - conexao.close(): fechar a conexão
import sqlite3 #importa o sqlite, que permite o acesso à base de dados

def create_users_table(conn):   #função que cria uma tabela na base de dados (caso não exista) de utilizadores. A tabela é composta
                                #por: ID, username, password e email. O ID é chave primária e é criada automaticamente. O username,
                                #a password e o email não podem ser campos que estejam em branco (NOT NULL).
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL,
                    email TEXT NOT NULL
                );""")
    conn.commit()

def add_user(conn, username, password, email): #função que adiciona utilizadores e os valores para os seus respetivos dados
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
              (username, password, email))
    conn.commit()

def get_user_by_username(conn, username):   #função que procura os dados dos utilizadores através do username. E retorna os
                                            #respetivos dados. Caso não haja dados é retornado "NONE"
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    return c.fetchone()

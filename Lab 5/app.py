from flask import Flask, render_template, request, redirect, session #importa o flask e algumas das suas funcionalidades
import sqlite3 #importa o sqlite, que permite o acesso à base de dados
import models #importa o models

app = Flask(__name__) #definição da variável 
app.secret_key = "secret" #cria uma app protegida

@app.route("/register", methods=["GET", "POST"]) #Adiciona os elementos GET e POST ao 'register'
def register():     #função que pertence ao registo (register), nesta página é pedido o user name, a password e o email ao 
                    #utilizador.
    if request.method != "POST":
        return render_template("register.html")
    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]

    conn = sqlite3.connect("media_users.db")    #os dados deste novo utilizador são adicionados à tabela criada no ficheiro
                                                #models, que se encontra na base de dados (por isso ser necessário invocar o sqlite3)

    models.create_users_table(conn)
    models.add_user(conn, username, password, email)
    conn.close()

    return redirect("/login")       #redireciona para a página login

@app.route("/login", methods=["GET", "POST"]) #Adiciona os elementos GET e POST ao 'login'
def login():            #função que pertence ao longin, nesta página é pedido o user name e a password.
    if request.method != "POST":
        return render_template("login.html")
    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect("media_users.db") #é invocado o sqlite3 de forma a recolher os dados do username)
    user = models.get_user_by_username(conn, username)
    conn.close()

    if user is None or user[2] != password:
        return "Incorrect username or password" #caso o resultado seja None, é retornado "Incorrect username or password"
    session["user_id"] = user[0]
    return redirect("/logout")

@app.route("/logout", methods=["GET", "POST"])
def logout():       #função do logout, que depois de terminada reencaminha para a página de login
    if request.method != "POST":
        return render_template("logout.html")
    session.pop("user_id", None)
    return redirect("/login")

if __name__ == "__main__":
    app.run()

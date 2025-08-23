import mysql.connector

def criacaoDB():
    try:
        conexao = mysql.connector.connect(host = "localhost", user = "root", password = "AA11aa22")
        cursor = conexao.cursor()

        #cursor.execute()
        cursor.execute("drop database aplicando")

        for aplicativo in cursor:
            print(aplicativo)

        conexao.commit()

        cursor.close()
        desconectar(conexao)

    except mysql.connector.Error as erro:
        print("Erro, ", erro) 

def desconectar(conexao):
    try:
        conexao.close()
    except Exception as erro:
        print(erro)

criacaoDB()
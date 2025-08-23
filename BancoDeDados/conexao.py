import mysql.connector

def conectar():
    try:
        conexao = mysql.connector.connect(host = "localhost", user = "root", password = "AA11aa22", database = "ledsDB")
        cursor = conexao.cursor()
        cursor.execute("")

        if conexao.is_connected():
            print("Conseguiu")

        else:
            print("Falha")
    
    except mysql.connector.Error as erro:
        print("Erro, ", erro)

def desconectar(conexao):
    try:
        conexao.close()
    except Exception as erro:
        print(erro)

conectar()
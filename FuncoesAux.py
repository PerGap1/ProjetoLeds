import re

#Evita erros na hora de informar a escolha, reduzindo também a redundância de código
def recebeEscolha():
    try:
        print()
        #Recebe a escolha do usuário
        escolha = int(input("1-Perfil do candidato, 2-Perfil do concurso: "))

        if escolha != 1 and escolha != 2:
            escolha = 0
        
    except ValueError:
        escolha = 0

    #Se a escolha tiver sido jogada para 0, a função main irá fechar automaticamente. Senão, ela procede com a escolha do usuário
    return escolha

#Conserta cpf's informados sem a formatação
def formataCPF(cpf : str):
    if not re.match(r'^[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}$', cpf):
        try:
            int(cpf)

            if len(cpf) == 11:
                cpf = cpf[0:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:11]
            else:
                cpf = ""

        except ValueError:          #Tenta transformar o cpf em inteiro para garantir que tenha apenas números
            cpf = ""

    #Se o cpf tiver seu valor anulado, a função main irá pedir o cpf novamente. Senão, ela continua normalmente
    return cpf
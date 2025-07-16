from datetime import date

class Candidato:
    def __init__(self, nome : str, dataNascimento : date, cpf : str, profissoes : list):
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.cpf = cpf

        #Tira espaços em branco
        for index in range(len(profissoes)):
            profissao = profissoes[index]

            if profissao[0] == ' ':
                profissao = profissao[1:]
                profissoes[index] = profissao

        self.profissoes = profissoes
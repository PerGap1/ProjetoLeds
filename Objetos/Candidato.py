from datetime import date

#Classe Candidato, com todos os seus atributos
class Candidato:

    #Construtor
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

    def mostrarDadosPuro(self):
        print(self.nome, self.dataNascimento, self.cpf, self.profissoes)

    def mostrarDados(self):
        print(f"Nome: {self.nome}, data de nascimento: {self.dataNascimento}, cpf: {self.cpf}, lista de profissões: {self.profissoes}")
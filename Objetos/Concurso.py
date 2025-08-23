#Classe Concurso, com todos seus atributos
class Concurso:

    #Construtor
    def __init__(self, orgao : str, edital : str, codigo : str, vagas : list):
        self.orgao = orgao
        self.edital = edital
        self.codigo = codigo
        self.vagas = vagas

    def mostrarDadosPuro(self):
        print(self.orgao, self.edital, self.codigo, self.vagas)

    def mostrarDados(self):
        print(f"Órgão: {self.orgao}, edital: {self.edital}, codigo: {self.codigo}, lista de vagas: {self.vagas}")

    def mostrarVagas(self):
        vagas = str()

        for vaga in self.vagas:
            if vaga != self.vagas[-1]:
                vagas += vaga + ", "
            else:
                vagas += vaga

        return vagas
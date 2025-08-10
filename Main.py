#Importações das outras partes do código
from Logica import LeitorArquivo
from Logica import ListasPerfil
from Logica import ListasBusca
from Logica import FuncoesAux

#Função principal
def main():
    try:
        #Recebe os dados dos arquivos de texto
        listaCandidatos = LeitorArquivo.retornaLista(r"ProjetoLEDS\ArquivosTexto\candidatos.txt")
        listaConcursos = LeitorArquivo.retornaLista(r"ProjetoLEDS\ArquivosTexto\concursos.txt")

        #Garante que as listas são válidas
        if not listaCandidatos or not listaConcursos:
            raise Exception

        #Recebe a entrada do usuário com erros evitados
        escolha = FuncoesAux.recebeEscolha()

        while escolha != 0:
            #O usuário escolheu ver concursos que encaixam com o perfil do candidato
            if escolha == 1:
                perfilCandidato = []
                cpf = FuncoesAux.formataCPF(input("Informe o cpf do candidato: "))

                #Verifica o cpf informado
                if (cpf != ""):

                    #Recebe a lista de concursos que encaixam com o perfil do candidato
                    perfilCandidato = ListasPerfil.perfilCandidato(listaCandidatos, listaConcursos, cpf)

                    #Garante que o candidato existe
                    candidato = ListasBusca.buscaCandidato(listaCandidatos, cpf)

                    #Saídas de dados
                    if candidato:
                        print()
                        print("Perfil do candidato:", candidato.profissoes)
                        print()

                    for concurso in perfilCandidato:
                        concurso.mostrarDados()

                    print(f"Quantidade de concursos: {len(perfilCandidato)}")

                else:
                    print("Cpf inválido")

            #O usuário escolheu ver candidatos que encaixam com o perfil do concurso
            elif escolha == 2:
                perfilConcurso = []
                codigo = input("Informe o código do concurso: ")

                #Verifica o código informado
                if len(codigo) == 11:

                    #Recebe a lista de candidatos que encaixam com o perfil do concurso
                    perfilConcurso = ListasPerfil.perfilConcurso(listaCandidatos, listaConcursos, codigo)

                    #Garante que o concurso existe
                    concurso = ListasBusca.buscaConcurso(listaConcursos, codigo)

                    #Saídas de dados
                    if concurso:
                        print()
                        print("Perfil do concurso:", concurso.vagas)
                        print()

                    for candidato in perfilConcurso:
                        candidato.mostrarDados()

                    print(f"Quantidade de candidatos: {len(perfilConcurso)}")

                else:
                    print("Código inválido")  

            #Recebe novamente a entrada do usuário, com tratamento de erros
            escolha = FuncoesAux.recebeEscolha()

    except NameError:
        print("Erro no arquivo de texto!")

if __name__ == "__main__":
    main()
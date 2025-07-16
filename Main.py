import LeitorArquivo
import ListasPerfil
import FuncoesAux

def main():
    try:
        listaCandidatos = LeitorArquivo.retornaLista("ProjetoLEDS\PseudoBD\candidatos.txt")
        listaConcursos = LeitorArquivo.retornaLista("ProjetoLEDS\PseudoBD\concursos.txt")

        if not listaCandidatos or not listaConcursos:
            raise Exception

        escolha = FuncoesAux.recebeEscolha()

        while escolha != 0:
            if escolha == 1:
                perfilCandidato = []
                cpf = FuncoesAux.formataCPF(input("Informe o cpf do candidato: "))

                #Verifica o cpf informado
                if (cpf != ""):

                    #Recebe a lista de concursos que encaixam com o perfil do candidato
                    perfilCandidato = ListasPerfil.perfilCandidato(listaCandidatos, listaConcursos, cpf)

                    #Garante que o candidato existe
                    candidato = ListasPerfil.buscaCandidato(listaCandidatos, cpf)
                    if candidato:
                        print()
                        print("Perfil do candidato:", candidato.profissoes)
                        print()

                    for concurso in perfilCandidato:
                        print(f"Órgão: {concurso.orgao}, edital: {concurso.edital}, codigo: {concurso.codigo}, lista de vagas: {concurso.vagas}")

                    print(f"Quantidade de concursos: {len(perfilCandidato)}")

                else:
                    print("Cpf inválido")

            elif escolha == 2:
                perfilConcurso = []
                codigo = input("Informe o código do concurso: ")

                #Verifica o código informado
                if len(codigo) == 11:

                    #Recebe a lista de candidatos que encaixam com o perfil do concurso
                    perfilConcurso = ListasPerfil.perfilConcurso(listaCandidatos, listaConcursos, codigo)

                    #Garante que o concurso existe
                    concurso = ListasPerfil.buscaConcurso(listaConcursos, codigo)
                    if concurso:
                        print()
                        print("Perfil do concurso:", concurso.vagas)
                        print()


                    for candidato in perfilConcurso:
                        print(f"Nome: {candidato.nome}, data de nascimento: {candidato.dataNascimento}, cpf: {candidato.cpf}, lista de profissões: {candidato.profissoes}")

                    print(f"Quantidade de candidatos: {len(perfilConcurso)}")

                else:
                    print("Código inválido")  

            escolha = FuncoesAux.recebeEscolha()

    except Exception as e:
        print("Erro no código!")
        print(e)

if __name__ == "__main__":
    main()
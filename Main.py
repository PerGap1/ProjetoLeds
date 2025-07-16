import LeitorArquivo
import ListasPerfil
import re

def main():
    listaCandidatos = LeitorArquivo.retornaLista("ProjetoLEDS\PseudoBD\candidatos.txt")
    listaConcursos = LeitorArquivo.retornaLista("ProjetoLEDS\PseudoBD\concursos.txt")

    escolha = int(input("1-Perfil do candidato, 2-Perfil do concurso: "))

    while escolha == 1 or escolha == 2:     

        if escolha == 1:
            perfilCandidato = []
            cpf = input("Informe o cpf do candidato: ")

            #Verifica o cpf informado
            if re.match(r'^[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}$', cpf):

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

        escolha = int(input("\n1-Perfil do candidato, 2-Perfil do concurso: "))

if __name__ == "__main__":
    main()
#Importações das outras partes do código
from Logica import LeitorArquivo
from Logica import ListasPerfil
from Logica import ListasBusca
from Logica import FuncoesAux

#Função central
def core(escolha, identificador):
    try:
        escolha = int(escolha)

        #Recebe os dados dos arquivos de texto
        listaCandidatos = LeitorArquivo.retornaLista(r"ProjetoLEDS\ArquivosTexto\candidatos.txt")
        listaConcursos = LeitorArquivo.retornaLista(r"ProjetoLEDS\ArquivosTexto\concursos.txt")

        #Garante que as listas são válidas
        if not listaCandidatos or not listaConcursos:
            raise NameError

        #O usuário escolheu ver concursos que encaixam com o perfil do candidato
        if escolha == 1:
            cpf = FuncoesAux.formataCPF(identificador)

            #Verifica o cpf informado
            if (cpf != ""):
                #Recebe a lista de concursos que encaixam com o perfil do candidato
                perfilCandidato = ListasPerfil.perfilCandidato(listaCandidatos, listaConcursos, cpf)

                #Garante que o candidato existe
                candidato = ListasBusca.buscaCandidato(listaCandidatos, cpf)

                return perfilCandidato, candidato

            else:
                print("Cpf inválido")

        #O usuário escolheu ver candidatos que encaixam com o perfil do concurso
        elif escolha == 2:
            codigo = str(identificador)

            #Verifica o código informado
            if len(codigo) == 11:
                #Recebe a lista de candidatos que encaixam com o perfil do concurso
                perfilConcurso = ListasPerfil.perfilConcurso(listaCandidatos, listaConcursos, codigo)

                #Garante que o concurso existe
                concurso = ListasBusca.buscaConcurso(listaConcursos, codigo)

                print(perfilConcurso, concurso)
                return perfilConcurso, concurso
            
            else:
                print("Código inválido")

        else:
            print("Escolha inválida")

    except NameError as e:
        print("Erro no arquivo de texto!", e)
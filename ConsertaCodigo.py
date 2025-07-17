import random
from Logica import LeitorArquivo

# Esse código foi usado para consertar o problema de repetição de códigos de concurso no arquivo de texto passado. O programa recebe a lista com todos
# os concursos, pega o código e vê se está na lista de códigos. Se não estiver, o código original é adicionado a lista, se estiver, o programa gera um
# novo código de 11 dígitos, em que o primeiro nunca pode ser 0, e muda os dados do concurso para ter esse código. Por conta do "while", se por acaso o
# código gerado estiver na lista, o programa gera um novo. Por fim, uma vez que todos os concursos estão atualizados, o programa itera pela lista de
# concursos, e escreve os dados do concurso no formato inicial, em um arquivo de texto provisório. 

# Provavelmente o arquivo no projeto final não funcionará, porque estará em um diretório de arquivos que foram usados apenas em algum momento do programa.

# Esse programa é essencial por conta da característica de singularidade do código do concurso, para que todos os concursos possam ser individualmente 
# analisados. Isso também impede de dar erro na hora de inserir os dados no banco de dados, em que o código do concurso será a chave primária da tabela.

def main():
    listaCodigos = []
    listaConcursos = LeitorArquivo.retornaLista(r"ArquivosTexto\concursos.txt")
    cont = 0

    for concurso in listaConcursos:
        codigo = concurso.codigo

        while codigo in listaCodigos:
            codigo = str()

            for i in range(11):
                if i == 0: 
                    algarismo = random.randint(1, 9)
                else:
                    algarismo = random.randint(0, 9)

                codigo = codigo + str(algarismo)

            concurso.codigo = codigo
            cont += 1

        listaCodigos.append(codigo)

    arquivoFinal = open(r"final.txt", "w", encoding='utf-8')

    for concurso in listaConcursos:
        arquivoFinal.write(concurso.orgao + "," + concurso.edital + "," + concurso.codigo + "," + str(concurso.vagas))
        arquivoFinal.write('\n')

    arquivoFinal.write(str(cont))

    arquivoFinal.close()

if __name__ == "__main__":
    main()
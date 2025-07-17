import random
import Logica.LeitorArquivo as LeitorArquivo

def main():
    listaCodigos = []
    listaConcursos = LeitorArquivo.retornaLista(r"PseudoBD\concursos.txt")

    for concurso in listaConcursos:
        codigo = concurso.codigo

        if codigo in listaCodigos:
            novoCodigo = str()

            for i in range(11):
                if i == 0: 
                    algarismo = random.randint(1, 9)
                else:
                    algarismo = random.randint(0, 9)

                novoCodigo = novoCodigo + algarismo

            concurso.codigo = novoCodigo

        listaCodigos.append(codigo)


    arquivoFinal = open("Descartaveis\final.txt", "w", encoding='utf-8')

    for concurso in listaConcursos:
        arquivoFinal.write(concurso.orgao + "," + concurso.edital + "," + concurso.codigo + "," + concurso.vagas)

if __name__ == "__main__":
    main()

arquivo = open("ProjetoLEDS\PseudoBD\concursos.txt", "r", encoding='utf-8')
arquivo2 = open("ProjetoLEDS\PseudoBD\\resultadoFinal.txt", "w", encoding='utf-8')

linhas = arquivo.readlines()


for i in range(1, 1001):
    arquivo2.write(str(i) + "," + linhas[i - 1])

arquivo.close()
arquivo2.close()
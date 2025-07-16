from Candidato import Candidato
from Concurso import Concurso

#Processa o arquivo por linhas, jogando os dados numa lista e retornando
def retornaLista(caminhoArquivo : str):
    try:                                  
        #Variáveis
        arquivo = open(caminhoArquivo, "r", encoding='utf-8')                         #Abre o arquivo, cuidando com caracteres especiais
        linhas = (arquivo.read()).split('\n')                                         #Recebe todo o conteúdo em um array de linhas
        lista = []

        for linha in linhas:                                                          #Itera pelas linhas
            if linha != "\n" and linha != "":                                         #Evita que o parágrafo do final do arquivo quebre o programa
                var1, var2, var3, var4 = linha.split(',', 3) 

                if "candidato" in caminhoArquivo.lower():                              
                    if var1 != "Nome":                                                #Pula a primeira linha
                        lista.append(Candidato(var1, var2, var3, formataVetor(var4))) 
                elif "concurso" in caminhoArquivo.lower():
                    if var1 != "Órgão":
                        lista.append(Concurso(var1, var2, var3, formataVetor(var4)))  

        arquivo.close()
        return lista
    
    except ValueError:
        print("O arquivo informado está fora de formato válido!")
        return None

#Corrige um erro com o vetor de profissões/vagas e transforma em lista
def formataVetor(vetor : list):                                                   
    if vetor[0] == "\"":
        return vetor[2:-2].split(',')
    else:
        return vetor[1:-1].split(',')
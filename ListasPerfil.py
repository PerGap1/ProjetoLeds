#Esta função permite que nenhuma das capacidades do candidato fique de fora, mas permite que ele não tenha todos os requisitos para o concurso
def perfilCandidato(listaCandidatos : list, listaConcursos : list, cpf : str):
    listaCorrespondencias = []

    #Procura pelo candidato informado
    for candidato in listaCandidatos:

        #Achou o candidato informado
        if candidato.cpf == cpf:                              

            #Itera entre os concursos
            for concurso in listaConcursos:

                #Verifica se todas as profissões (ou capacidades) do candidato estão contidas entre as vagas (ou requisistos) do concurso
                todasCapacidades = True

                for capacidade in candidato.profissoes:
                    if capacidade not in concurso.vagas:
                        todasCapacidades = False
                        break

                #Se todas as capacidades estiverem contidas entre os requisitos e o concurso não estiver na lista, este será adicionado
                if todasCapacidades and concurso not in listaCorrespondencias:
                    listaCorrespondencias.append(concurso) 

    return listaCorrespondencias

#Esta função, ao contrário da anterior, permite que nenhum dos requisitos do concurso fique faltando, 
# mas permite que ela não use de todas as capacidades do candidato
def perfilConcurso(listaCandidatos : list, listaConcursos : list, codigo : str):
    listaCorrespondencias = []

    #Procura pelo concurso informado
    for concurso in listaConcursos:

        #Achou o concurso informado
        if concurso.codigo == codigo:                                

            #Itera entre os candidatos
            for candidato in listaCandidatos:

                #Verifica se todas as vagas (ou requisitos) do concurso estão contidas entre as profissões (ou capacidades) do candidato
                todosRequisitos = True

                for requisito in concurso.vagas:
                    if requisito not in candidato.profissoes:
                        todosRequisitos = False
                        break

                #Se todos os requisitos estiverem contidos entre as capacidades e o candidato não estiver na lista, este será adicionado
                if todosRequisitos and candidato not in listaCorrespondencias:
                    listaCorrespondencias.append(candidato)

    return listaCorrespondencias
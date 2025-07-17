#Função para localizar candidato
def buscaCandidato(listaCandidatos : list, cpf : str):
    for candidato in listaCandidatos:
        if candidato.cpf == cpf:
            return candidato
        
    return None

#Função para localizar concurso
def buscaConcurso(listaConcursos : list, codigo : str):
    for concurso in listaConcursos:
        if concurso.codigo == codigo:
            return concurso
        
    return None
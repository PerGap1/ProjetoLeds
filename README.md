DOCUMENTAÇÃO DA SOLUÇÃO:
Essa explicação serve apenas para o que foi feito no código até o momento.

O desafio proposto é o de fazer um sistema que faça duas consultas diferentes, mas semelhantes: a primeira recebe o cpf de um candidato, e lista os atributos de concursos que tenham correspondência com tal candidato. A segunda, ao contrário, recebe o
código de um concurso, e lista os atributos de candidatos que tenham correspondência com tal concurso.

A forma que eu usei, de maneira geral, considera como correspondência do candidato todos os concursos que usem de todas as profissões dele, mesmo que o concurso ofereça mais vagas do que o que o candidato pode assumir. Também considera como
correspondência do concurso um candidato que tenha todas as profissões ofertadas por ele, mesmo que o candidato possua mais profissões do que as vagas que o concurso ofereça. Devido a esta forma de resolver o problema, optei por mudar a forma de pensar
sobre os termos profissões e vagas de uma maneira diferente: a profissão do candidato foi interpretada como uma capacidade dele, enquanto que a vaga do concurso foi interpretada como um requisito deste. Assim, ao meu ver e de acordo com minha solução,
se torna mais fácil entender o que o código está pretendendo fazer em cada pedaço.

Partindo para a parte do código: a principal ideia do código está no arquivo "ListasPerfil.py". Ela possui duas funções, ambas procuram o objeto (candidato ou concurso) a partir do dado informado (cpf ou código), encontram o objeto, e iteram pelas
listas do objeto oposto (se a função localizou um candidato, a lista iterada é a de concursos, e vice e versa). Para cada objeto da lista, a função itera pelo último atributo do primeiro objeto (capacidades ou requisitos), e verifica se ela está
contida no último atributo do objeto iterado. Se for localizado algum atributo não contido, o objeto iterado não poderá entrar na lista de correspondências. Se isso não acontecer, o objeto será adicionado. Exemplo: a função que procura concursos dentro
do perfil do usuário vai ler o cpf deste, tentar localizar o usuário, e se localizar, vai testar se cada capacidade dele está contida nos requisitos do concurso. Se, em algum momento, for localizada alguma que não está, o concurso não entrará na lista
de correspondências. Senão, o concurso será incluído. No final a lista é retornada para a função "main.py"

As outras partes do código incluem funções que interpretam os arquivos de texto passados pelo desafio, entradas de usuário e saídas de dados, funções de busca para auxiliar nas saídas de dados, e uma classe para concursos e outra para candidatos. 

A documentação do código está em formato de comentários através do próprio código.

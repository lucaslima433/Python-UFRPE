'''Juvenal participou de várias edições da Maratona de Programação e ganhou três
campeonatos seguidos (sozinho). Ele foi aluno revelação do BSI. Isso abriu o olho de um
famoso serviço de busca nordestino chamado “Quêde?”. A empresa contratou Juvenal
antes mesmo de ele poder beber legalmente. Algumas empresas concorrentes do
Quede? acharam isso assédio. Mas já era. Dormiram no ponto.
Quede? está muito preocupada com a crescente taxa de erros de ortografia de seus
usuários. Juvenal pensa que as pessoas não têm mais o menor pudor em assassinar a
língua materna, talvez até esteja na moda (Juvenal tem opiniões sobre tudo!). No entanto,
esses erros tornam mais difíceis as buscas por palavras chaves, que constantemente
contêm erros de algumas letras, devidos a má digitação ou má ortografia. O serviço
funciona com base num dicionário de palavras. O usuário deve inserir uma palavra num
campo de um formulário; o serviço então procura esta palavra no dicionário e retorna
conteúdo que tenha relação com a palavra. Para contornar o problema de ortografia,
designaram Juvenal para fazer um programa que tenta adivinhar qual palavra o usuário
pretendia procurar, independente de haver erros de ortografia nela. Para este problema,
Juvenal definiu a distância entre duas palavras A e B como sendo o número de
operações, descritas abaixo, necessárias para transformar A em B:
1. Retirar uma letra de A.
2. Adicionar uma letra a A, em qualquer posição.
3. Trocar qualquer letra de A por outra letra, na mesma posição.
O serviço de busca definiu que a palavra P fornecida pelo usuário pode se referir a uma
palavra D do dicionário se está a uma distância de no máximo 2 de D.
Exemplos:
• A palavra ‘tu’ pode se referir `a palavra do dicionário ‘tubo’, realizando duas vezes a
operação 2.
• A palavra ‘crto’ pode se referir `a palavra do dicionário ‘corte’, realizando uma vez a
operação 2 e uma vez a operação 3.
• A palavra ‘crto’ pode se referir `a palavra do dicionário ‘curto’, realizando uma vez a
operação 2.
• A palavra ‘hortgrafea’ não pode se referir `a palavra do dicionário ‘ortografia’.
Juvenal deve escrever um programa que, dado um dicionário de palavras, descubra para
cada palavra fornecida pelo usuário a quais palavras do dicionário ela pode se referir, nas
condições descritas acima. A vida de playboy não está deixando Juvenal escrever esse
programa, assim ele pediu sua ajuda para fazê-lo (Juvenal vai ficar te devendo muitos
favores neste semestre).


Entrada
A entrada contém um único conjunto de testes, que deve ser lido do dispositivo de
entrada padrão. A primeira linha contém 2 inteiros N, M, representando respectivamente o
número de palavras contidas no dicionário (1<=N<=1000) e o número de palavras a
serem analisadas (1<=M <=100). Cada uma das N linhas seguintes conterá uma palavra
pertencente ao dicionário. Cada uma das M linhas seguintes conterá uma palavra a ser
analisada, fornecida pelo usuário. Cada palavra pode ter de 1 a 20 letras, contendo
apenas letras de ‘a’ a ‘z’, minúsculas.


Saída
Seu programa deve imprimir, na saída padrão, M linhas, sendo uma linha para cada
palavra fornecido pelo usuário. Cada linha deve conter todas palavras do dicionário `as
quais a palavra fornecida pode se referir. No caso de haver mais de uma palavra em uma
linha da resposta, elas devem ser separadas por um espaço em branco, aparecendo na
ordem que elas foram dadas na entrada, como pode ser visto no exemplo de saída
abaixo. No caso de não haver nenhuma palavra em uma linha da resposta, deixe-a em
branco.'''

def menor(a,b):
    menor = a
    if b < a:
        menor = b
    return menor

def distanciaedicao(palavra1, palavra2):
    n, m = len(palavra1), len(palavra2)
    tab = [[0] * (m + 1) for i in range(n + 1)]

    for i in range(n + 1):
        tab[i][0] = i
    for j in range(m + 1):
        tab[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            tab[i][j] = menor(menor(tab[i - 1][j] + 1, tab[i][j - 1] + 1),tab[i - 1][j - 1] + (0 if palavra1[i - 1] == palavra2[j - 1] else 1))

    return tab[n][m]


N, M = map(int, input().split())

dicionario = []
palavras_erradas = []

for c in range(N):
    dicionario.append(input())

for k in range(M):
    palavras_erradas.append(input())

for palavra in palavras_erradas:
    resultado = []
    for palavra_certa in dicionario:
        distancia = distanciaedicao(palavra, palavra_certa)
        if distancia <= 2:
            resultado.append(palavra_certa)

    print(" ".join(resultado))



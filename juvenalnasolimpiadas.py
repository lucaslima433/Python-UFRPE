'''Juvenal vai disputar as Olimpíadas de inverno na modalidade do Curling masculino. Ele é o único
atleta que também está em competições de programação. Sabendo da polivalência e eficiência de
Juvenal, o comitê olímpico pediu para ele implementar um programa que gere a classificação final
dos países, considerando o número de medalhas recebidas pelos atletas de cada país nessas
olimpíadas. Como Juvenal quer muito a medalha de ouro, ele pediu para você escrever esse sistema
e assim ele poder focar nas vassouras.

Tarefa
Sua tarefa é escrever um programa que, dada a informação dos países que receberam medalhas de
ouro, prata e bronze em cada modalidade, gere a lista de classificação dos países na competição.
Nesta tarefa, os países serão identificados por números inteiros. O melhor colocado deve ser o país
que conseguiu o maior número de medalhas de ouro. Se houver empate entre países no número de
medalhas de ouro, o melhor colocado entre esses é o país que conseguiu o maior número de
medalhas de prata. Se houver empate também no número de medalhas de prata, o melhor colocado
entre esses é o país que recebeu o maior número de medalhas de bronze. Se ainda assim houver
empate entre dois países, o melhor classificado é o que tem o menor nu´mero de identificação.

Entrada
A entrada contém um único conjunto de testes, que deve ser lido do dispositivo de entrada padrão
(normalmente o teclado). A primeira linha da entrada contém dois números inteiros N e M,
separados por um espaço em branco, indicando respectivamente o número de países (1 ≤ N ≤ 100) e
número de modalidades esportivas envolvidas na competição (1≤M ≤100). Os países são
identificados por números inteiros de 1 a N. Cada uma das M linhas seguintes contém três números
inteiros O, P e B, separados por um espaço em branco, representando os países cujos atletas
receberam respectivamente medalhas de ouro (1≤O ≤N), prata (1≤P ≤N) e bronze (1≤B ≤N). Assim,
se uma das M linhas contém os números 3 2 1, significa que nessa modalidade a medalha de outro
foi ganha pelo país 3, a de prata pelo país 2 e a de bronze pelo país 1.

Saída
Seu programa deve imprimir uma linha contendo N números, separados por um espaço em branco,
representando os países na ordem decrescente de classificação (o primeiro nu´mero representa o
país que é o primeiro colocado, o segundo número representa o país que é o segundo colocado, e
assim por diante).'''

def Partition(A, p, r):
    x = A[str(r)]
    i = p - 1
    for j in range(p, r):
        if A[str(j)].ouro > x.ouro:
            i = i + 1
            A[str(i)], A[str(j)] = A[str(j)], A[str(i)]
        elif A[str(j)].ouro == x.ouro:
            if A[str(j)].prata > x.prata:
                i = i + 1
                A[str(i)], A[str(j)] = A[str(j)], A[str(i)]
            elif A[str(j)].prata == x.prata:
                if A[str(j)].bronze > x.bronze:
                    i = i + 1
                    A[str(i)], A[str(j)] = A[str(j)], A[str(i)]
                elif A[str(j)].bronze == x.bronze:
                    if A[str(j)].nome < x.nome:
                        i = i + 1
                        A[str(i)], A[str(j)] = A[str(j)], A[str(i)]

    A[str(i + 1)], A[str(r)] = A[str(r)], A[str(i + 1)]
    return i + 1


def quick_sort(A, p, r):
    if p < r:
        q = Partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


class Pais():
    def __init__(self, nome, ouro=0, prata=0, bronze=0):
        self.nome = int(nome)
        self.ouro = ouro
        self.prata = prata
        self.bronze = bronze
        self.sort = False

    def __repr__(self):
        return str(self.nome)

    def __str__(self):
        return str(self.nome)

    def addOuro(self):
        self.ouro += 1

    def addPrata(self):
        self.prata += 1

    def addBronze(self):
        self.bronze += 1


paises = {}
entrada = input().split()
for i in range(1, int(entrada[0]) + 1):
    paises[str(i)] = Pais(str(i))

for j in range(int(entrada[1])):
    ent = input().split()

    paises[ent[0]].addOuro()
    paises[ent[1]].addPrata()
    paises[ent[2]].addBronze()

quick_sort(paises, 1, len(paises))
classificacoes = ''
for i in range(1, len(paises) + 1):
    if i is not len(paises):
        classificacoes += str(paises[str(i)]) + ' '
    else:
        classificacoes += str(paises[str(i)])
print(classificacoes)

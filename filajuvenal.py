'''Com a proximidade da Copa do Mundo, o fluxo de pessoas nas filas para compra de ingressos
aumentou consideravelmente. Como as filas estão cada vez maiores, pessoas menos pacientes
tendem a desistir da compra de ingressos e acabam deixando as filas, liberando assim vaga para
outras pessoas. Quando uma pessoa deixa a fila, todas as pessoas que estavam atrás dela dão um
passo a frente, sendo assim nunca existe um espaço vago entre duas pessoas. A fila inicialmente
contém N pessoas, cada uma com um identificador diferente. Juvenal sabe o estado inicial dela e os
identificadores em ordem das pessoas que deixaram a fila. Sabendo que após o estado inicial
nenhuma pessoa entrou mais na fila, Juvenal deseja saber o estado final da fila.

Entrada
A primeira linha contém um inteiro N representando a quantidade de pessoas inicialmente na fila. A
segunda linha contém N inteiros representando os identificadores das pessoas na fila. O primeiro
identificador corresponde ao identificador da primeira pessoa na fila. É garantido que duas pessoas
diferentes não possuem o mesmo identificador. A terceira linha contém um inteiro M representando
a quantidade de pessoas que deixaram a fila. A quarta linha contém M inteiros representando os
identificadores das pessoas que deixaram a fila, na ordem em que elas saíram. É garantido que um
mesmo identificador não aparece duas vezes nessa lista.

Saída
Seu programa deve imprimir uma linha contendo N-M inteiros com os identificadores das pessoas
que permaneceram na fila, em ordem de chegada.

Restrições
• 1<=N<=50000
• 1<=M<=50000 e M < N
• Cada identificador está entre 1 e 100000'''

class No:
    def __init__(self, dado=None):
        self._dado = dado
        self._ant = None
        self._prox = None

    def __str__(self):
        return "{}".format(self._dado)

class lista():
    def __init__(self):
        self._inicio = None
        self._fim = None

    def eVazia(self):
        if self._inicio == None:
            return True
        return False

    def InserirNoFim(self, dado=None):
        novono = No(dado)
        if self.eVazia():
            self._inicio = self._fim = novono
        else:
            novono._ant = self._fim
            self._fim._prox = novono
            self._fim = novono


    def buscar(self, x):
        i = self._inicio
        while i != None:
            if x == i._dado:
                break
            else:
                i = i._prox
        return i


    def removerElemento(self, x):
        no_econtrado = self.buscar(x)
        if no_econtrado != None:
            if no_econtrado._ant != None:
                no_econtrado._ant._prox = no_econtrado._prox
            else:
                self._inicio = no_econtrado._prox

            if no_econtrado._prox != None:
                no_econtrado._prox._ant = no_econtrado._ant
            else:
                self._fim = no_econtrado._ant

        return no_econtrado

    def removerDoInicio(self):
        no = self._inicio
        if not self.eVazia():
            if no._prox == None:
                self._fim = None
            else:
                no._prox._ant = None
            self._inicio = no._prox
        return no

    def __str__(self):
        s = ''
        i = self._inicio
        while i != None:
            s += "{} ".format(str(i))
            i = i._prox
        return s

class fila(lista):
    def inserir(self, dado):
        self.InserirNoFim(dado)

    def remover(self):
        return self.removerDoInicio()

N = int(input())
minhafila = fila()
for i in input().split():
    minhafila.inserir(i)
M = int(input())
for j in input().split():
    minhafila.removerElemento(j)

print(minhafila)

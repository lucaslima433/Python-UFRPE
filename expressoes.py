'''Juvenal gosta bastante de teoria da computação e matemática. Como passatempo, ele decidiu
implementar um gerador de expressões matemáticas. O gerador de expressões que ele criou
funciona em duas fases. Na primeira fase é gerada uma cadeia de caracteres que contém apenas os
caracteres `{', `[', `(', `}', `]' e `)'. Na segunda fase, o gerador adiciona os números e operadores na
estrutura criada na primeira fase. Uma cadeia de caracteres é dita bem definida (ou válida) se atende
as seguintes propriedades:

1. Ela é uma cadeia de caracteres vazia (não contém nenhum caractere).
2. Ela é formada por uma cadeia bem definida envolvida por parênteses, colchetes ou chaves.
Portanto, se a cadeia S é bem definida, então as cadeias (S), [S] e {S} também são bem definidas.
3. Ela é formada pela concatenação de duas cadeias bem definidas. Logo, se as cadeias X e Y são
bem definidas, a cadeia XY é bem definida.
Depois que Juvenal gerou algumas expressões matemáticas, ele percebeu que havia algum erro na
primeira fase do gerador. Algumas cadeias não eram bem definidas. Ele quer começar a resolver as
expressões o mais rápido possível, e sabendo que você é um ótimo programador, resolveram pedir
que você escreva um programa que dadas várias cadeias geradas na primeira fase, determine quais
delas são bem definidas e quais não são.


Entrada
A entrada é composta por diversas instâncias. A primeira linha da entrada contém um inteiro T
indicando o número de instâncias. Em seguida temos T linhas, cada uma com uma cadeia A.

Saída
Para cada instância imprima uma linha contendo a letra S se a cadeia é bem definida, ou a letra N
caso contrário.


Restrições
1≤ T ≤20. A cadeia de caracteres A tem entre 1 e 100000 caracteres. A cadeia de caracteres A
contém apenas caracteres `{', `[', `(', `}', `]' e `)'.'''

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
            s += "{}".format(str(i))
            i = i._prox
        return s

class pilha(lista):
    def push(self, dado):
        novono = No(dado)
        if self.eVazia():
            self._inicio = novono
            self._fim = novono
        else:
            novono._prox = self._inicio
            self._inicio._ant = novono
        self._inicio = novono

    def pop(self):
        return self.removerDoInicio()

    def getitem(self):
        return self._inicio._dado


def main(A):
    minhapilha = pilha()
    for item in A:
        if item == '(':
            minhapilha.push(item)
        elif item == '[':
            minhapilha.push(item)
        elif item == '{':
            minhapilha.push(item)

        if not minhapilha.eVazia():
            if item == ')' and minhapilha.getitem() == '(':
                minhapilha.pop()
            elif item == ']' and minhapilha.getitem() == '[':
                minhapilha.pop()
            elif item == '}' and minhapilha.getitem() == '{':
                minhapilha.pop()
        else:
            return 'N'
    if minhapilha.eVazia():
        return 'S'
    else:
        return 'N'

T = int(input())
for x in range(T):
    A = list(input())
    print(main(A))

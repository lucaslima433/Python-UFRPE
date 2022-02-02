'''Juvenal é conhecido pelas ótimas festas que organiza em sua casa de praia em
Natal. Elas são sempre muito badaladas. Mas ele não é bobo e sempre diz que
existe uma condição. Ele aceita fornecer a casa, a comida e a piscina, contanto
que algum dos convidados fique para lavar a louça. Como todos querem as festas
mas ninguém quer ficar pra limpar a bagunça, eles sempre decidem isso em um jogo
de sorte.

O jogo é assim:
Cada convidado começa com um monte de cartas na mão, e existe outro monte na
mesa. A cada rodada, uma carta do monte da mesa é descoberta e cada convidado
faz o mesmo com o seu próprio monte. Caso a carta que um convidado tire seja de
mesmo numero que a carta presente na mesa, o convidado descarta ela de sua mão
(ela não será mais usada!). Caso a carta seja de numero diferente, ela volta
para o final da pilha de cartas do convidado. A carta da mesa sempre volta pro
final do monte da mesa.(Podendo, inclusive, ser reutilizada!). O convidado
sortudo será o primeiro que ficar sem cartas na mão(Torça pra não ser você!).
Caso o jogo não termine em 1000 rodadas, Juvenal será o ganhador.

Formato de Entrada
A entrada inicia com um inteiro F, que indica quantas festas Juvenal realizou.
A próxima linha indica a configuração inicial do deck na mesa, na ordem em que
as cartas deverão aparecer (primeira carta é a primeira que sai). As cartas têm
valores entre 0 e 10^5. As próximas linhas representam os decks de cada
convidado. Cada convidado é representado por um inteiro C, começando de 1 e
contando...
O fim de cada caso é representado pelo numero -1.

Restrições: 0 < F <= 10^5

Formato de Saída
Para cada caso, imprima C o número identificador da pessoa que ganhou (Juvenal
tem o número 0)

Obs: caso haja empate, opte sempre pelo convidado de menor identificador
O baralho é velho, formado pela junção de vários decks incompletos. É possível
encontrar cartas repetidas.
Para todos os convidados terem chance de vencer, é garantido que o deck da mesa
tem qualquer carta que possa aparecer na mão de um convidado.'''

class No:
    def __init__(self, dado=None):
        self.dado = dado
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

    def limpar(self):
        self._inicio = self._fim = None





F_rodadas = int(input())
def main():
    jogadores = []
    mesadeck = fila()
    for x in input().split():
        mesadeck.inserir(int(x))

    while True:
        maofila = fila()
        mao = list(map(int, input().split()))

        if mao[0] == -1:
            break
        else:
            for u in mao:
                maofila.inserir(int(u))
            jogadores.append(maofila)

    for i in range(1000):
        deckjoga = mesadeck.remover()
        for i in range(len(jogadores)):
            jogadorjoga = jogadores[i].remover()

            if jogadores[i].eVazia() == True:
                return i+1
            if jogadorjoga.dado != deckjoga.dado:
                jogadores[i].inserir(jogadorjoga.dado)

        mesadeck.inserir(deckjoga)
    return 0

for x in range(F_rodadas):
    print(main())



'''
Juvenal não confia em ninguém
Juvenal gosta muito de jogar batalha naval, mas não confia nos seus colegas de jogo.
Para verificar se seus amigos estão trapaceando, ele decidiu usar um programa de computador para verificar o resultado do jogo, mas Juvenal ainda não sabe programar e por isso pediu a sua ajuda. O jogo de batalha naval é jogado em um tabuleiro retangular com N linhas e M colunas. Cada posição deste tabuleiro é um quadrado que pode conter água ou uma parte de um navio. Dizemos que dois quadrados são vizinhos se estes possuem um lado em comum. Se duas partes de navio estão em posições vizinhas, então essas duas partes pertencem ao mesmo navio. A regra do jogo proíbe que os quadrados de duas partes de navios distintos tenham um canto em comum (em outras palavras, que quadrados de duas partes de navios distintos compartilhem um vértice).
Cada disparo que um jogador faz deve ser feito em um dos quadrados do tabuleiro do outro jogador. Um jogador informa ao outro a coluna e a linha do quadrado alvo do disparo. Para que um navio seja destruído, o jogador deve acertar todas as partes deste navio. O jogador não pode atirar no mesmo lugar mais de uma vez.
Tarefa
Escreva um programa que, dadas a configuração do tabuleiro e uma sequência de disparos feitos por um jogador, determina o número de navios do outro jogador que foram destruídos.
Entrada
A primeira linha da entrada contém números dois inteiros N e M (1≤N≤100 e M≤100) representando respectivamente o número de linhas e de colunas do tabuleiro. As N seguintes linhas correspondem ao tabuleiro do jogo. Cada uma dessas linhas contém M caracteres. Cada caractere indica o conteúdo da posição correspondente no tabuleiro. Se esse caractere for ‘.’, essa posição contém água; se for ‘#', essa posição contém uma parte de um navio. A próxima linha contém um número K que é o número de disparos feitos pelo jogador (1≤K≤N×M). As próximas K linhas indicam os disparos feitos pelo jogador. Cada linha contém dois inteiros L e C, indicando a linha e a coluna do disparo feito pelo outro jogador (1≤L≤N e 1≤C≤M).
Saída
Seu programa deve imprimir uma única linha contendo um único número inteiro, o número de navios destruídos.
------------------------------------------------------------------------
'''

def tamanhonavios(matriz, i, j, n):
    if matriz [i][j] == '#':
        matriz[i][j] = n
        navios[n] += 1

        if i - 1 >= 0:
                tamanhonavios(matriz, i - 1, j, n)
        if j - 1 >= 0:
                tamanhonavios(matriz, i, j - 1, n)
        if i + 1 < l:
                tamanhonavios(matriz, i + 1, j, n)
        if j + 1 < c:
                tamanhonavios(matriz, i, j + 1, n)


matriz = []
l, c = map(int, input().split())
for i in range(c):
    linha = []
    linha.extend(input())
    matriz.append(linha)

navios = []
numdenavios = 0
for n in range(l):
    for m in range(c):
        if matriz[n][m] == "#":
            navios.append(int('0'))
            tamanhonavios(matriz, n, m, numdenavios)
            numdenavios += 1

numdisparos = int(input())
for x in range(numdisparos):
    i, j = map(int, input().split())
    alvo = matriz[i - 1][j - 1]
    if alvo != '.':
        navios[alvo] -= int(1)


destruidos = 0
destruidos = navios.count(0)
print(destruidos)

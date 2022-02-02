'''Juvenal tem fazendas de caju em Serra do Mel - RN. Os cajueiros são plantados dispostos em linhas
e colunas, formando uma espécie de grade. Na fazenda administrada por Juvenal existem L linhas
de cajueiros, cada uma formada por C colunas. Nesta semana Juvenal deve executar a colheita da
produção de um subconjunto continuo de cajueiros. Esse subconjunto e formado por M linhas e N
colunas de cajueiros. Há uma semana, seus funcionários analisaram cada cajueiro da fazenda e
estimaram a sua produtividade em número de cajus prontos para a colheita. Juvenal agora precisa da
sua ajuda para determinar qual a produtividade máxima estimada (em número de cajus) de uma área
de M x N cajueiros.

Tarefa
Sua tarefa e escrever um programa que, dado um mapa da fazenda contendo o número de cajus
prontos para colheita em cada cajueiro, encontre qual o número máximo de cajus que podem ser
colhidos na fazenda em uma área de M x N cajueiros.

Entrada
A entrada contem um único conjunto de testes, que deve ser lido do dispositivo de entrada padrão
(normalmente o teclado). A primeira linha da entrada contem quatro números inteiros, L, C, M e N.
L e C representam, respectivamente, o número de linhas (1 <= L <= 1000) e de colunas (1 <= C <=
1000) de cajueiros existentes na fazenda. M e N representam, respectivamente, o número de linhas
(1 <= M <= L) e de colunas (1 <= N <= C) de cajueiros a serem colhidos. As L linhas seguintes
contem C inteiros cada, representando número de cajus prontos para colheita no cajueiro localizado
naquela linha e coluna.

Saída
Seu programa deve imprimir, na saída padrão, uma única linha que contem o número máximo
estimado de cajus que podem ser colhidos em uma área continua de M x N. Esse número não será
superior a 1000000'''

def maior(x, y):
    maior = x
    if y > x:
        maior = y
    return maior

L, C, M, N = map(int, input().split())

matriz = []


for x in range(L):
    entrada = list(map(int, input().split()))
    matriz.append(entrada)

matrizPD = [[0]*C for k in range(L)]

for i in range(L):
    for j in range(C):
        if i == 0 and j == 0:
            matrizPD[i][j] = matriz[i][j]
        elif i == 0 and j != 0:
            matrizPD[i][j] = matrizPD[i][j - 1] + matriz[i][j]
        elif j==0 and i!=0:
            matrizPD[i][j] = matrizPD[i - 1][j] + matriz[i][j]
        else:
            matrizPD[i][j] = matrizPD[i][j - 1] + matrizPD[i - 1][j] + matriz[i][j] - matrizPD[i-1][j-1]

caju_colhidos = 0
for i in range(L):
    for j in range(C):
        if i-M < 0 and j-N < 0:
            atual_colhidos = matrizPD[i][j]
            caju_colhidos = maior(atual_colhidos, caju_colhidos)
        elif i-M < 0:
            atual_colhidos = matrizPD[i][j] - matrizPD[i][j - N]
            caju_colhidos = maior(atual_colhidos, caju_colhidos)
        elif j-N < 0:
            atual_colhidos = matrizPD[i][j] - matrizPD[i - M][j]
            caju_colhidos = maior(atual_colhidos, caju_colhidos)
        else:
            atual_colhidos = matrizPD[i][j] - matrizPD[i][j-N] - matrizPD[i-M][j] + matrizPD[i-M][j-N]
            caju_colhidos = maior(atual_colhidos, caju_colhidos)

print(caju_colhidos)



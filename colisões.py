'''
Detectando Colisões
Detecção de colisão é uma das operações mais comuns (e importantes) em jogos eletrônicos. O
objetivo, basicamente, é verificar se dois objetos quaisquer colidiram, ou seja, se a interseção entre
eles é diferente de vazio. Isso pode ser usado para saber se duas naves colidiram, se um monstro
bateu numa parede, se um personagem pegou um item, etc.
Para facilitar as coisas, muitas vezes os objetos são aproximados por figuras geométricas simples
(esferas, paralelepípedos, triângulos etc). Neste problema, os objetos são aproximados por
retângulos num plano 2D.

Escreva um programa que, dados dois retângulos, determine se eles se interceptam ou não.
'''

xa0, ya0, x1a, y1a = list(map(int, input().split()))
xb0, yb0, x1b, y1b = list(map(int, input().split()))


def colide():
    if x1a < xb0 or xa0 > x1b:
        print(0)
    elif y1a < yb0 or ya0 > y1b:
        print(0)
    else:
        print(1)


colide()

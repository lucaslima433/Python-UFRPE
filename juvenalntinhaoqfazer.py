'''
Juvenal estava sem ter o que fazer em uma sexta-feira imprensada e resolveu criar uma função
porém ele não sabe se ela sempre termina, já que é recursiva. A função é a seguinte:

F(n) = {

1, se n = 1

F(n/2), se n for par

F(3*n+1), se n for ímpar

}

Juvenal definiu outra função: G(n) = quantas chamadas recursivas são necessárias para que F(n) atinja o caso base.
Agora, dado dois inteiros A e B, Juvenal quer saber qual o maior valor que a função G assume quando n está no intervalo [A,B].
Formato de Entrada A primeira linha contém T, o número de casos de teste.
Cada caso de teste contém dois números, A e B.'''

def func(n, count):
    if n == 1:
        count += 1
        print(count)
        return count
    elif n % 2 == 0:
        count += 1
        return func(n/2, count)
    elif n % 2 == 1:
        count += 1
        return func(3*n+1, count)


def gfunc():
    recursividade = 0
    t = int(input())
    for j in range(t):
        try:
            maior = 0
            a, b = map(int, input().split())
            for i in range(a, b + 1):
                atual = func(i, recursividade)
                if atual > maior:
                    maior = atual
            print("Caso", str(j + 1) + ":", maior)
        except EOFError or ValueError:
            break


gfunc()

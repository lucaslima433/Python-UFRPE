'''
Quebrando a Banca
Juvenal e seu parceiro Leôncio estavam voltando para casa quando receberam uma
ligação de Tobias, gerente do banco a qual são clientes. Tobias falou que houve
um grande problema no saldo de usuários do banco: foram, acidentalmente,
concatenados (em posições aleatórias) inteiros em cada saldo e não existe um
backup para se descobrir o valor antigo, mas o banco sabe quantos caracteres
foram concatenados em cada saldo.
Para resolver a situação o banco resolveu retirar caracteres do saldo. Juvenal,
que não ia aceitar perder dinheiro, obrigou o banco a deixar o saldo o maior
possível quando se retirassem os caracteres.
Por exemplo, se eu sei que o saldo é 1435 e sabendo que existem 2 caracteres
extras nesse saldo, posso concluir que devo apagar os números 1 e 3 para gerar o
maior saldo possível: 45.
Leôncio conhece (superficialmente) os conceitos de Estruturas de Dados, logo
precisa de sua ajuda para descobrir as maiores sequências possíveis que podem
ser formadas ao se retirar caracteres.
Formato de Entrada
Vão existir vários casos de teste. (use endOfFile)
Cada caso é formado por A e B 1 <= B < A <= 10^5 seguido na linha abaixo por A
caracteres (o primeiro digito nunca vai ser zero) que representam inteiros, B é
a quantidade de dígitos que você deve apagar.
Formato de Saída
Imprima o maior saldo possível que pode existir depois da retirada de
caracteres.
'''

while True:
    try:
        maior = 0
        a, b = map(int, input().split())
        listaInt = input()

        if a == b:
            listaInt = "0"
        else:
            for i in range(b):
                for j in range(len(listaInt)):
                    atual = listaInt[:j] + listaInt[j + 1:]
                    if int(atual) > maior:
                        maior = int(atual)
                listaInt = maior
                maior = 0
        print(int(listaInt))
    except EOFError or ValueError:
        break
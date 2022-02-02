'''A JuveTubo é uma empresa que atua na área de produção de tubos e conexões. A técnica de
produção utilizada na JuveTubo produz sempre canos longos, que são então cortados para satisfazer
a necessidade dos clientes.
Os seus clientes têm aplicações variadas, necessitando de diferentes comprimentos de canos. No
início, quando a empresa era pequena e os clientes eram poucos, todo o processo de planejamento
dos cortes (para maximizar o lucro) era efetuado por um funcionário muito dedicado. Porém, com o
aumento dos pedidos, isto se tornou proibitivo. É aí que você entra: contratado pela JuveTubo, sua
tarefa é escrever um programa que, dada uma relação de comprimentos de cano e seus respectivos
valores de venda, determine o maior valor total que possa ser obtido com o corte de um cano de
comprimento inicial determinado. Comprimentos de cano podem ser repetidos, e podem haver
sobras de cano.

Entrada
A entrada é iniciada por uma linha contendo o inteiro N (1 ≤ N ≤ 1000) que é o número de
tamanhos de canos solicitados e o inteiro T (1 ≤ T ≤ 2000) que é o tamanho do cano produzido pela
JuveTubo.
A seguir virão N linhas, cada uma contendo dois inteiros Ci e Vi(1 ≤ Ci, Vi ≤ 5000, 1 ≤ i ≤ N),
representando, respectivamente, o comprimento do cano i desejado por um cliente e seu valor de
venda.

Saída
Imprima em uma linha o maior valor que pode ser obtido com o corte e a venda o cano original de
tamanho T.'''

def maior(x, y):
    maior = x
    if y > x:
        maior = y
    return maior

N, T = map(int, input().split())
valores = []
tamanhos = []
for i in range(N):
    tamanho, valor = map(int, input().split())
    tamanhos.append(tamanho)
    valores.append(valor)

cortes = [[0]*(T+1) for a in range(N+1)]
for i in range(N + 1):
    for j in range(T + 1):
      if i == 0:
          if j == 0:
            cortes[i][j] = 0

      elif tamanhos[i-1] <= j:
        cortes[i][j] = maior(valores[i-1] + cortes[i-1][j-tamanhos[i-1]],  cortes[i-1][j])

      else:
        cortes[i][j] = cortes[i-1][j]

print(cortes[N][T])

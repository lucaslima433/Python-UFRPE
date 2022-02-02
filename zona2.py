# def dist_edit(a, b):
#     # a = 'pata'
#     # b = 'pato'
#
#     tab = []
#
#     num = 0
#     num2 = 0
#     tab.append([i for i in range(len(b) + 1)])
#
#     for i in range(1, len(a) + 1):
#         tab.append([])
#         for j in range(len(b) + 1):
#             if j == 0:
#                 tab[i].append(i)
#             else:
#                 # tab[i].append(0)
#                 if a[i - 1] == b[j - 1]:
#                     tab[i].append(tab[i - 1][j - 1])
#                 else:
#                     tab[i].append(min(tab[i][j - 1], tab[i - 1][j - 1], tab[i - 1][j]) + 1)
#     return tab[len(a)][len(b)]
#
#
# dic = []
# lista = []
#
# NM = input().split()
# for i in range(int(NM[0])):
#     dic.append(input())
#
# for i in range(int(NM[1])):
#     lista.append(input())
#
# for inpt in lista:
#     saida = []
#     for p_dic in dic:
#         if len(p_dic) >= len(inpt) - 2 and len(p_dic) <= len(inpt) + 2:
#             if len(p_dic) >= len(inpt) - 2 and len(p_dic) <= len(inpt) + 2:
#                 edit_dist = dist_edit(inpt, p_dic)
#                 if edit_dist <= 2:
#                     saida.append(p_dic)
#
#     palavra = ' '
#     print(palavra.join(saida))
#
# ######################################################################################################################################
#
# def minimo(x,y,z):
#     if x < y and x < z:
#         return x
#     elif y < x and y < z:
#         return y
#     else:
#         return z
# def distancia_de_edicao(M,word1,word2):
#     c=0
#     for i in range(1,len(word1)+1):
#         for j in range(1,len(word2)+1):
#             if word1[i-1] == word2[j-1]:
#                 c = 0
#             else:
#                 c = 1
#             M[i][j] = minimo(M[i-1][j-1] + c, M[i-1][j] +1, M[i][j-1] + 1)
#     return M[len(word1)][len(word2)]
#
# def arrumar(M,word1,word2):
#     for i in range(len(word1)+1):
#         M[i][0] = i
#     for j in range(len(word2)+1):
#         M[0][j] = j
#     return M
#
# dic = []
# analisar = []
# n,m = map(int,input().split())
# result=[[] for i in range(m)]
#
# for x in range(n):
#     a = input()
#     dic.append(a)
# for x in range(m):
#     a = input()
#     analisar.append(a)
# #para cada palavra em dic e cada palavra em analisar
#
#
# for x in dic:
#     b=0
#     for y in analisar:
#         M = [[0]*(len(x)+1) for a in range(len(y)+1)]
#         arrumar(M,y,x)
#         a = distancia_de_edicao(M,y,x)
#         if a <= 2:
#             result[b].append(x)
#         b+=1
# for x in result:
#     print(' '.join(x))
#
# ######################################################################################################################################
#
# def menor_custo(a,b,c):
#     menor = a
#     if b < a and b < c:
#         menor = b
#     if c < a and c < b:
#         menor = c
#     return menor
#
# def distancia_edicao(p1, p2):
#     tamanho1 = len(p1)
#     tamanho2 = len(p2)
#     if tamanho1 > tamanho2:
#         p1, p2 = p2, p1
#     distancia = range(tamanho1 + 1)
#     index1, index2 = 0,0
#     for S in p2:
#         distancia2 = [index2+1]
#         for T in p1:
#             if T == S:
#                 distancia2 += [distancia[index1]]
#             else:
#                 distancia2 += [1 + menor_custo((distancia[index1]), (distancia[index1 + 1]), (distancia2[-1]))]
#             index1 += 1
#         index1 = 0
#         index2 += 1
#         distancia = distancia2
#     return distancia[-1]
#
# n, m = [int(c) for c in input().split()]
# dicionario = [input() for x in range(n)]
# p_erradas = [input() for x in range(m)]
#
# n_palavras = len(p_erradas)
# cont = 0
# while cont < n_palavras:
#     lista = []
#     for n in dicionario:
#         if len(n) <= len(p_erradas[cont]) + 2 or len(n) < len(p_erradas[cont]) + 2:
#             if distancia_edicao(p_erradas[cont], n) <= 2:
#                 lista += [n]
#         else:
#             pass
#     p_erradas[cont] = lista
#     print(' '.join(p_erradas[cont]), end="")
#     if p_erradas[cont] != p_erradas[-1]:
#         print("", end='')
#     print('')
#     cont+=1

n, t = map(int, input().split())
valor_total = 0

for i in range(n):
  c, v = list(map(int, input().split()))
  if (t - c) >= 0:
    valor_total += v
    t -= c
print(valor_total)

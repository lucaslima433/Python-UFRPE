'''Normalmente, em urgências de hospitais, os pacientes são atendidos na ordem em que chegam ao à
sala de atendimento. No entanto, há pacientes que têm quadro clínico mais grave e devem ser
atendidos prioritariamente. Como curar pessoas se revelou um mau negócio, pois uma vez curados,
os pacientes não retornavam mais aos hospitais, O Hospital Cura Se Puder Pagar (HCSPP) resolveu
mexer na ordem na qual os pacientes são atendidos. O dono do HCSPP percebeu que se atendesse
pessoas com mais dinheiro primeiro, seu lucro aumentaria. Assim, ele quer implementar um sistema
de prioridades para os atendimentos de acordo com o quanto cada pessoa pode pagar e usar o
quadro clínico como critério de desempate. Uma enfermeira ficará no atendimento fazendo a
triagem: para cada paciente, ela verificará o plano de pagamento do paciente e o grau de gravidade
do seu estado. Os planos de pagamento seguem a seguinte ordem de prioridade: premium >
diamante > ouro > prata > bronze > resto. A gravidade do quadro do paciente é denotado por um
número em [0, 1000], valores menores indicam menor gravidade. A enfermeira irá colocar essas
informações em um sistema e ele organizará a ordem de atendimento dos pacientes.

Tarefa
O HCSPP te contratou para implementar o sistema que organizará a fila de pacientes. Essa fila
deverá ter os pacientes com planos mais caros na frente. Em caso de pacientes com o mesmo plano,
a prioridade deverá ser dado àqueles em situação mais grave. Em caso de empate com o plano e
gravidade, os pacientes serão atendidos em ordem alfabética. Nenhuma biblioteca de funções de
terceiros poderá ser usada.

Entrada
A primeira linha tem o número de pacientes N. As próximas N linhas serão formadas por triplas
compostas pelo nome do paciente, plano de pagamento e gravidade. O nome do paciente é sempre
minúsculo e tem apenas uma palavra.

Saída
Seu programa deverá imprimir os nomes dos pacientes na fila de atendimento do HCSSP.
'''

class Heap:

    def __init__(self, a):
        self.a = a
        self.heap_size = len(a)

    def heapify_max(self, i):
        left = 2*i + 1
        right = 2*i + 2
        if (left < self.heap_size) and (self.a[left] > self.a[i]):
            largest = left
        else:
            largest = i
        if (right < self.heap_size) and (self.a[right] > self.a[largest]):
            largest = right
        if largest != i:
            temp = self.a[i]
            self.a[i] = self.a[largest]
            self.a[largest] = temp
            self.heapify_max(largest)

    def build_max_heap(self):
        self.heap_size = len(self.a)
        for i in range(int((len(self.a))/2), -1, -1):
            self.heapify_max(i)

    def heap_sort(self):
        self.build_max_heap()
        for i in range(len(self.a)-1, 0, -1):
            temp = self.a[0]
            self.a[0] = self.a[i]
            self.a[i] = temp
            self.heap_size -= 1
            self.heapify_max(0)

def ficha(paciente):
    if paciente[1] == "premium":
        paciente[1] = 0
    elif paciente[1] == "diamante":
        paciente[1] = 1
    elif paciente[1] == "ouro":
        paciente[1] = 2
    elif paciente[1] == "prata":
        paciente[1] = 3
    elif paciente[1] == "bronze":
        paciente[1] = 4
    elif paciente[1] == "resto":
        paciente[1] = 5

    paciente.reverse()
    paciente[0], paciente[1] = paciente[1], paciente[0]
    return paciente


numPacientes = int(input())
listaPrioridade = []

for item in range(numPacientes):
    paciente = input().split()
    paciente[2] = int(paciente[2])-1000
    paciente[2] *= -1
    ficha(paciente)
    listaPrioridade.append(paciente)

heap = Heap(listaPrioridade)
heap.heap_sort()

for i in range(numPacientes):
     print(listaPrioridade[i][2])

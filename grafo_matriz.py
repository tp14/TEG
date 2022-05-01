class Graph(): 
   
    def __init__(self, nvertices): 
        self.N = nvertices 
        self.graph = [[0 for column in range(nvertices)]  
                    for row in range(nvertices)] 
        self.V = ['' for v in range(nvertices)]
          
    def nameVertexAdd(self, i, nome):
            self.V[i]=nome    

    def getIndiceVertice(self, nome):
        for n in range(self.N):
            if nome == self.V[n]:
                return n

    def setWeights(self, v1, v2, weight):
        for row in range(self.N):
            if self.V[row] ==  v1:
                for column in range(self.N):
                    if self.V[column] ==  v2:
                        self.graph[row][column]=weight
                
    def verificaAdj(self, v1, v2):
        for row in range(self.N):
            if self.V[row] ==  v1:
                for column in range(self.N):
                    if self.V[column] ==  v2:
                        if self.graph[row][column] != 0:
                            return self.graph[row][column]
        return 'Não são adjacentes'
    
    def grauVertice(self,v1):
        grau = 0
        for row in range(self.N):
            if self.graph[row][g.getIndiceVertice(v1)] != 0:
                grau += 1
        for column in range(self.N):
            if self.graph[g.getIndiceVertice(v1)][column] != 0:
                grau += 1
        return grau

    def numAresta(self):
        arestas = 0
        for row in range(self.N):
            for column in range(self.N):
                if self.graph[row][column] != 0:
                    arestas += 1
        return arestas
    
    def veriCompleto(self):
        completo = True
        for row in range(self.N):
            for column in range(self.N):
                if g.V[row] != g.V[column]:
                    if self.graph[row][column] != self.graph[column][row]:
                        completo = False
                elif self.graph[row][column] != 0:
                 completo = False
        return completo

    def verSubGrafico(self,sub):
        cont = 0
        for row in range(sub.N):
            for column in range(sub.N):
                if sub.graph[row][column] == self.graph[row][column]:
                    cont += 1
        if(cont == sub.N**2):
            return 'Sim'
        return 'Não'
    
    def printGrafo(self):
        print(self.V)
        for column in range(self.N): 
           print(self.graph[column])
  
n = 10
g = Graph(n)

g.nameVertexAdd(0,'A')
g.nameVertexAdd(1,'B')
g.nameVertexAdd(2,'C')
g.nameVertexAdd(3,'D')
g.nameVertexAdd(4,'E')
g.nameVertexAdd(5,'F')
g.nameVertexAdd(6,'G')
g.nameVertexAdd(7,'H')
g.nameVertexAdd(8,'I')
g.nameVertexAdd(9,'J')
g.setWeights('A','C',60)
g.setWeights('C','E',70)
g.setWeights('E','G',70)
g.setWeights('G','I',80)
g.setWeights('B','A',170)
g.setWeights('C','D',180)
g.setWeights('F','E',180)
g.setWeights('G','H',180)
g.setWeights('J','I', 190)
g.setWeights('B','D',70)
g.setWeights('D','B',70)
g.setWeights('D','F',70)
g.setWeights('F','D',70)
g.setWeights('F','H',70)
g.setWeights('H','F',70)
g.setWeights('H','J',70)
g.setWeights('J','H',70)

print('Escolha uma opção:')
print('1- Verificar adjacencia e distancia')
print('2- Grau de um vertice')
print('3- Verificar se um grafo a é subgrafo do grafo b')
print('4- Numero de arestas do grafo')
print('5- Verificar se o grafo é completo')
print('6- Printa um grafo')
print('0 - Sair')
op = int(input())

while (op!=0):
    
    if op == 1:
        print('Digite as letras dos vértice que dejesa verificar:')
        v1 =input()
        v2 = input()
        print(g.verificaAdj(v1,v2))
    if op == 2:
        print('Digite a letra do vértice que dejesa o grau:')
        v1 =input()
        print(g.grauVertice(v1))
    if op == 3:
        print('Numero de vertíces a:')
        na = int(input())
        a = Graph(na)
        for i in range(a.N):
            print('Digite o nome do vértice ',i,' de a:')
            a.V[i] = input()
        op2 = 1
        while (op2!=0):
            print('1- Digite uma nova aresta\n0- Sair')
            op2 = int(input())
            if op2 == 1:
                print('Digite o v1 seguido do v2 e do peso:')
                v1 = input()
                v2 = input()
                weight = int(input())
                a.setWeights(v1,v2,weight)
        print('Numero de vertíces b:')
        nb = int(input())
        b = Graph(nb)
        for i in range(b.N):
            print('Digite o nome do vértice ',i,' de b:')
            b.V[i] = input()
        op2 = 1
        while (op2!=0):
            print('1- Digite uma nova aresta\n0- Sair')
            op2 = int(input())
            if op2 == 1:
                print('Digite o v1 seguido do v2 e do peso:')
                v1 = input()
                v2 = input()
                weight = int(input())
                b.setWeights(v1,v2,weight)
        print(b.verSubGrafico(a))
    
    if op == 4:
        print(g.numAresta())
    if op == 5:
        print(g.veriCompleto())
    if op == 6:
        g.printGrafo()

    print('Escolha uma opção:')
    print('1- Verificar adjacencia e distancia')
    print('2- Grau de um vertice')
    print('3- Verificar se um grafo a é subgrafo do grafo b')
    print('4- Numero de arestas do grafo')
    print('5- Verificar se o grafo é completo')
    print('6- Printa um grafo')
    print('0 - Sair')
    op = int(input())


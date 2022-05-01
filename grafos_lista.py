import queue
import math

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.explored = False
        self.d = math.inf
        self.p = node 

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]
    
    def getAdjacent(self):
        return self.adjacent

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def getNumVertex(self):
        return self.num_vertices

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        #self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def verificaAdj(self):
        print('Digite as letras dos vértice que dejesa verificar:')
        v1 = input()
        v2 = input()
        for v in self:
            for w in v.get_connections():
                vid = v.get_id()
                wid = w.get_id()
                if (vid == v1 and wid == v2):
                    return "São adjacentes, distancia: %i" %(v.get_weight(w))
        return 'Não são adjacentes'

    def verificaAdjBool(self,v1,v2):
        for v in self:
            for w in v.get_connections():
                vid = v.get_id()
                wid = w.get_id()
                if (vid == v1 and wid == v2):
                    return True
        return False

    def grauVertice(self):
        print('Digite a letra do vértice que dejesa o grau:')
        v1 = input()
        grau = 0
        for v in self:
            for w in v.get_connections():
                vid = v.get_id()
                wid = w.get_id()
                if(vid == v1 or wid ==v1):
                    grau +=1
        return grau
    
    def grauDoVertice(self,v):
        grau = 0
        for v in self:
            for w in v.get_connections():
                vid = v.get_id()
                wid = w.get_id()
                if(vid == v.id or wid == v.id):
                    grau +=1
        return grau
                    
    def veriSubGrafo(self):
        a = Graph()
        b = Graph()
        print('Digite o tamanho e os vértices do subgrafo a:')
        tam = int(input())
        for n in range(tam):
            a.add_vertex(input())
        op = 1
        while (op!=0):
            print('1- Digite uma nova aresta\n0- Sair')
            op = int(input())
            if op == 1:
                print('Digite o v1 seguido do v2 e do peso:')
                a.add_edge(input(), input(), int(input())) 
        print('Digite o tamanho e os vértices do subgrafo b:')
        tam = int(input())
        for n in range(tam):
            b.add_vertex(input())
        op = 1
        while (op!=0):
            print('1- Digite uma nova aresta\n0- Sair')
            op = int(input())
            if op == 1:
                print('Digite o v1 seguido do v2 e do peso:')
                b.add_edge(input(), input(), int(input()))
        for v in a:
            for v2 in b:
                vid = v.get_id()
                vid2 = v2.get_id()
                if(vid == vid2):
                    for w in v.get_connections():
                        for w2 in v2.get_connections():
                            wid = w.get_id()
                            wid2 = w2.get_id()
                            pes = v.get_weight(w)
                            pes2 = v2.get_weight(w2)
                            if (wid == wid2 and pes != pes2):
                                return 'Não é um subgrafo'
        return 'É um subgrafo'
         
    def numArestas(self):
        arestas = 0
        for v in self:
            for w in v.get_connections():
                arestas +=1
        return arestas

    def veriCompleto(self):
        for v in self:
            numConexoes = 0
            for w in v.get_connections():
                numConexoes += 1
            if numConexoes != self.num_vertices-1:
                return 'Não é completo'
        return 'É completo'

    def verCiclo(self):
        print('Digite o número de vértices do ciclo:')
        tam = int(input())
        lista = list()  

        print('Vertice inicial:')
        for i in range(tam): 
            lista.append(input())
            print('Proximo vertice:')
        
        if (lista[0] != lista[tam-1]):
            return False
        
        for i in range(tam-2):
            cont = 0
            if (lista[i+1] == lista[0]):
                return False
            for j in range(tam-2):
                if(lista[i+1] == lista[j+1]):
                    cont += 1
            if(cont > 1):
                return False

        for i in range(tam-1):
            adj = 0
            for v in self:
                for w in v.get_connections():
                    vid = v.get_id()
                    wid = w.get_id()
                    if (vid == lista[i] and wid == lista[i+1]):
                        adj += 1
            if (adj==0):
                return False

        return True         
    
    def setAllUnexplored(self):
         for v in self:
            v.explored = False

    def bfs(self,s):
        self.setAllUnexplored() #Marca todos como não explorados
        s.explored = True
        Q = queue.Queue()  #Cria fila FIFO
        Q.put(s)
        while(Q.qsize() != 0):
            print('Q:',end="")
            for i in Q.queue:
                print(i.id,end="")
            print()
            v = Q.get()
            print('v:',v.id)
            for w in v.get_connections():    
                if(w.explored == False):
                    w.explored = True    
                    Q.put(w) #Insere no final da fila         
        Q.empty()  

    def dfs(self,s):
        #self.setAllUnexplored() #Marca todos como não explorados
        P = list()  #Cria pilha
        P.append(s)
        while(len(P) != 0):
            #print('P:',end="")
            #for i in P:
                #print(i.id,end="")
            #print()
            v = P.pop()
            v.explored = True   
            for w in v.get_connections():    
                if(w.explored == False):   
                    P.append(w) #Insere na pilha         
        P.clear() 
      
    def menorDistanciaInexplorado(self):
        menor = math.inf
        for v in self:
            if(v.explored == False and v.d<=menor):
                menor = v.d
                menorV = v
        return menorV

    def dijkstra(self,s):
        self.setAllUnexplored()
        for v in self:
            v.d = math.inf 
            v.p = -1
        s.d = 0
        explorados = list()
        while(len(explorados) != self.num_vertices):
            v = self.menorDistanciaInexplorado()
            explorados.append(v)
            v.explored = True
            for w in v.get_connections():
                if(w.explored == False and v.d + v.get_weight(w) < w.d):
                    w.d = v.d + v.get_weight(w)
                    w.p = v.id
        for v in self:
            print('v:',v.id)
            print(' d:',v.d)
            print(' p:',v.p)

    def reuniao(self):
        menor = math.inf
        for v in g:
            g.dijkstra(v)
            maior = -math.inf
            for v in self:
                if maior < v.d:
                    maior = v.d
            if menor > maior:
                menor = maior
        return menor
    
    def bellmanFord(self, s):
        for v in self:
            v.d = math.inf 
            v.p = -1
        s.d = 0
        for v in self:
            for w in v.get_connections():
                if(v.d != math.inf and v.d + v.get_weight(w) < w.d):
                    w.d = v.d + v.get_weight(w)
                    w.p = v.id
        for v in self:
            print('v:',v.id)
            print(' d:',v.d)
            print(' p:',v.p)

    def floydWarshall(self):
        n = self.num_vertices
        matriz = list()
        matrizResul = list()
        #preencher a matriz
        for v in self:
            for w in self:
                if(v.id == w.id):
                    matriz.append(0)
                    matrizResul.append(0)
                if(v.id != w.id and not self.verificaAdjBool(v.id,w.id)):
                    matriz.append(math.inf)
                    matrizResul.append(math.inf)
                if(self.verificaAdjBool(v.id,w.id)):
                    matriz.append(v.get_weight(w))
                    matrizResul.append(v.get_weight(w))
        print('inicada:',matriz)

        #calculo
        a = n-1
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if(j != i and j != k  and i != k):
                        matrizResul[i+j+(a*i)] = min(matriz[i+j+(a*i)],matriz[i+k+(a*i)]+matriz[k+j+(a*k)])
            matriz.clear
            matriz = matrizResul
            matrizResul.clear
        print('final:', matriz)

    def isConected(self):
        self.setAllUnexplored()
        for v in self:
            if(v.explored == False): 
                for w in v.get_connections():
                    if(self.grauDoVertice(v) > 0):
                        self.dfs(v) 
                        v.explored = True
                    if( self.grauDoVertice(w) > 0):
                        self.dfs(w) 
                        w.explored = True                        
        for v in self:
            print(v.id,v.explored)
            if(v.explored == False):
                print('nao é conectado')
                return False   
        print('é conectado')                   
        return True 

    def isEulerian(self):
        if(self.isConected() == False):
            return 'Não é Euleriano, disconexo'
        impares = 0
        for v in self:
            print(self.grauDoVertice(v))
            print(self.grauDoVertice(v)%2)
            if(self.grauDoVertice(v)%2 != 0):
                impares += 1
        if impares == 0:
            return 'Tem ciclo Euleriano'
        if impares == 2:
            return 'Tem caminho Euleriano'
        if impares > 2:
            return 'Não é Euleriano'

if __name__ == '__main__':

    g = Graph()

    g.add_vertex('0')
    g.add_vertex('1')
    g.add_vertex('2')
    g.add_vertex('3')
    #g.add_vertex('4')

    g.add_edge('0', '1', 10)
    g.add_edge('1', '2', 5)
    g.add_edge('2', '3', 3)
    g.add_edge('3', '0', 2)
    #g.add_edge('2', '4', 6)

    print('Escolha uma opção:')
    print('1- Verificar adjacencia e distancia')
    print('2- Grau de um vertice')
    print('3- Verificar se um grafo a é subgrafo do grafo b')
    print('4- Numero de arestas do grafo')
    print('5- Verificar se o grafo é completo')
    print('6- Printa um grafo')
    print('7- Verifica ciclo no grafo')
    print('8- Fazer busca em largura')
    print('9- Fazer busca em profundidade')
    print('10- Dijkstra')
    print('11- Reuniao')
    print('12- Bellman-Ford')
    print('13- Floyd-Warshall')
    print('14- Teste Euleriano')
    print('0 - Sair')
    op = int(input())

    while (op!=0):
        if op == 1:
            print(g.verificaAdj())  

        if op == 2:
            print(g.grauVertice())

        if op == 3:
            print(g.veriSubGrafo())

        if op == 4:
            print(g.numArestas())

        if op == 5:
            print(g.veriCompleto())

        if op == 6:
            for v in g:
                for w in v.get_connections():
                    vid = v.get_id()
                    wid = w.get_id()
                    print ('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))
            for v in g:
                print ('g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()]))

        if op == 7:
            if (g.verCiclo()):
                print('Sim')
            else: 
                print('Não')

        if op == 8:
            print('Digite o primeiro vertice:')
            s = input()
            for v in g:
                vid = v.get_id()
                if(vid == s):
                    g.bfs(v)

        if op == 9:
            print('Digite o primeiro vertice:')
            s = input()
            for v in g:
                vid = v.get_id()
                if(vid == s):
                    g.dfs(v)
                
        if op == 10:
            print('Digite o primeiro vertice:')
            s = input()
            for v in g:
                vid = v.get_id()
                if(vid == s):
                    g.dijkstra(v)
        
        if op == 11:
            print(g.reuniao())

        if op == 12:
            print('Digite o primeiro vertice:')
            s = input()
            for v in g:
                vid = v.get_id()
                if(vid == s):
                    g.bellmanFord(v)

        if op == 13:
            g.floydWarshall()

        if op == 14:
            print(g.isEulerian())

        print('Escolha uma opção:')
        print('1- Verificar adjacencia e distancia')
        print('2- Grau de um vertice do grafo')
        print('3- Verificar se um grafo a é subgrafo do grafo b')
        print('4- Numero de arestas do grafo')
        print('5- Verificar se o grafo é completo')
        print('6- Printa o grafo')
        print('7- Verifica ciclo no grafo')
        print('8- Fazer busca em largura')
        print('9- Fazer busca em profundidade')
        print('10- Dijkstra')
        print('11- Reuniao')
        print('12- Bellman-Ford')
        print('13- Floyd-Warshall')
        print('14- Teste Euleriano')
        print('0 - Sair')
        op = int(input())

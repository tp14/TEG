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
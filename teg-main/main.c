#include <stdio.h>
#include "matriz.h"

int main() {
    int numero_vertices = 0;

    int ** matriz_adjacencia = criaMatriz(&numero_vertices);
    
    imprime_matriz(matriz_adjacencia, numero_vertices);
    
    imprime_numero_nos(numero_vertices);
    
    imprime_numero_arestas(matriz_adjacencia,numero_vertices);
    
    imprime_arestas(matriz_adjacencia,numero_vertices);
    
    
    return 0;
}


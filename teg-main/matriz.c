#include "matriz.h"
#include <stdio.h>
#include <stdlib.h>

void mostraMenu() {
    printf("\n");
    printf("|____________________________________________|\n");
    printf("|                MENU DE OPÇÕES              |\n");
    printf("|--------------------------------------------|\n");
    printf("| 1 - CARREGAR GRAFO A PARTIR DO ARQUIVO     |\n");
    printf("| 2 - EXIBIR GRAFO                           |\n");
    printf("| 0 - SAIR                                   |\n");
    printf("|--------------------------------------------|\n");
}

/**
 * Cria uma matriz a partir de um arquivo
 * @return a matriz de adjacência correspondente ao grafo representado no arquivo
 */

int ** criaMatriz(int * numero_vertices){
    FILE* f;
    char line[256];

    // TODO: Verificar como informar o local do arquivo
    f = fopen("./matrix.txt", "r");
    if(f == NULL) {
        perror("");
        return NULL;
    }

    int n, from, to;

    // salva referência do número de vértices da main para uso futuro
    fscanf(f, "%i", &n);
    *numero_vertices = n;

    // Cria uma matriz vazia inicializada com zeros para ser populada pelo arquivo
    int ** matriz_adjacencia = malloc(*numero_vertices * sizeof(int *));

    for (int i = 0; i < *numero_vertices; i++) {
        matriz_adjacencia[i] = calloc(*numero_vertices, sizeof(int));
    }

    // Popula o grafo com suas arestas
    while (!feof (f))
    {
        fscanf (f, "%i", &from);
        fscanf(f, "%i", &to);
        matriz_adjacencia[from-1][to-1]++;
        matriz_adjacencia[to-1][from-1]++;
    }

    return matriz_adjacencia;
}


/**
 * Imprime um grafo previamente populado
 * @param matrix matriz de ajdacencia
 * @param n numero de vértices do grafo
 * @return a matriz de adjacência correspondente ao grafo representado no arquivo
 */
void imprime_matriz(int ** matrix, int n) {
    printf("  | ");
    for (int i = 0; i < n; i++) {
        printf("%i ", i+1);
    }
    printf("\n-------------\n");

    for (int i = 0; i < n; i++) {
        printf("%i | ", i+1);
        for (int j = 0; j < n; j++) {
            printf("%i ", matrix[i][j]);
        }
        printf("\n");
    }
}

void imprime_numero_nos(int n){
    printf("Numero de nos: %i\n", n);
}

void imprime_numero_arestas(int ** matrix, int n){
    int cont = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            if(matrix[i][j] != 0){
                cont++;
            }
        }
    }
    printf("Numero de arestas: %i\n", cont);
}

void imprime_arestas(int ** matrix, int n){
    printf("Arestas:\n");
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            if(matrix[i][j] != 0){
                printf("%i-%i\n",i+1,j+1);
            }
        }
    }
}

#ifndef LISTA_H
#define LISTA_H
#include "usuario.h"

typedef struct no
{
	User usuario; 
	struct no *proximo;
} No;

typedef struct Lista 
{
	int tamanho;
	No* cabeca;
	No* cauda;
} lista;

No* criaNo(char nome[20], char codigo_pais[5], char ddd[3],char numero[9]);
void add(lista *lista, char nome[20], char codigo_pais[5], char ddd[3],char numero[9]);
void salvar(lista *lista);
No busca(lista *lista, int index);

#endif /* LISTA_H */
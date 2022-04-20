#include "lista.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "usuario.h"

No* criaNo(char nome[20], char codigo_pais[5], char ddd[3],char numero[9]) 
{
	User *usuario = (User*)malloc(sizeof(User));
	
	strcpy(usuario->nome, nome);
	strcpy(usuario->codigo_pais, codigo_pais);
	strcpy(usuario->ddd, ddd);
	strcpy(usuario->numero, numero);
	
	No *novoNo = (No*)malloc(sizeof(No));
	novoNo->usuario = *usuario;
	novoNo->proximo = NULL;
	return novoNo;
}

void add(lista *lista, char nome[20], char codigo_pais[5], char ddd[3],char numero[9]){
	No *novoNo = criaNo(nome, codigo_pais, ddd, numero);
	lista->cauda->proximo = novoNo;
	lista->cauda = novoNo;
}
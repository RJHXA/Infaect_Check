#include "usuario.h"
#include "lista.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

void usuario()
{
	User usuario;
	
	char nome[20];
	char codigo_pais[5];
	char ddd[3];
	char numero[10];
	int validar = 0, sair = 1;
	
	while(sair == 1){

		lista *Lista = (lista*)malloc(sizeof(lista));
		
		printf("Nome: ");
		scanf("%s", nome);
	
		printf("Codigo do pais: ");
		scanf("%s", codigo_pais);
		
		printf("Codigo DDD: ");
		scanf("%s", ddd); 
	
		printf("Numero celular: ");
		scanf("%s", numero); 

		if (validar == 0){
			No *novoNo = criaNo(nome, codigo_pais, ddd, numero);
			Lista->cabeca = novoNo;
			Lista->cauda = novoNo;

			validar = 1;
		} else {
			add(Lista, nome, codigo_pais, ddd, numero);
		}
    
    printf("Deseja adicionar mais um usuario?\n1- Sim | 2- Nao\n");
    scanf("%d", &sair);

    if(sair == 2)
    {
       sair = 0; 
    }
  }
}
#include <stdio.h>
#include "funcionalidades.h"
#include "usuario.h"

int main() {

   int command = 0;

	printf("Você quer acessar qual partição ?\n 1- Usuario | 2- Funcionalidades\n");
	scanf("%d", &command);

    switch(command)
    {
      case 1:
        usuario();
        break;
      case 2:
        funcionalidades();
        break;
      
      default:
        printf("Comando Inválido!\n");
      break;
    }

    return 0;
}
#include "funcionalidades.h"
#include <stdio.h>
#include <string.h>

void funcionalidades ()
{
	  int analize = 0;
    int validador = 1, parada = 1, opcao, i = 0, tamanho_analise, tamanho_chave, fake = 0;
    FILE *fp;
    char *resultado;
    char linha[100];
    char frase_analisar[10000];

    while(validador != 0)
    {
        int escolha;
        printf("Escolha a Funcionalidade\n1- Ler Arquivo;\n2- Adicionar nova Palavra chave;\n3- Verificar Frase;\n4- Sair\n");
        scanf(" %d", &escolha);
      
        switch (escolha)
        {
            case 1:
                fp = fopen("bd.txt", "rt");
                while(!feof(fp))
                {
                    resultado = fgets(linha, 100, fp);
                    printf("%s", linha);
                }
                printf("\n");
                fclose(fp);
                break;

            case 2:
                while(parada != 0)
                {
                    char palavra_nova[15];
                    fp = fopen("bd.txt", "a");
                    printf("Digite a palavra que deseja adicionar no banco de dados: ");
                    scanf("%s", palavra_nova);
                    fputs("\n", fp);
                    resultado = fputs(palavra_nova, fp);

                    fclose(fp);
                    printf("Deseja adiocionar mais alguma?\n1- Sim | 2- Nao\n");
                    scanf("%d", &opcao);

                    if(opcao == 2)
                    {
                        parada = 0;
                    }
                }
                break;

            case 3:
                printf("Digite a frase que queres analisar: ");
                scanf(" %[^\n]", frase_analisar);

                tamanho_analise = strlen(frase_analisar);

                fp = fopen("bd.txt", "r");
                while(!feof(fp))
                {
                    resultado = fgets(linha, 100, fp);
                    tamanho_chave = strlen(resultado);

                    for(int i = 0; i < tamanho_analise; i++)
                    {
                        if(strncmp(resultado, &frase_analisar[i], tamanho_chave-1) == 0)
                        {
                            fake++;
                        }
                    }
                }

                fclose(fp);

                if(fake > 0)
                {
                    printf("Frase não apresenta confiabilidade. Verifique a Fonte para não compartilhar Fake News!\n");
                }
                fake = 0;
                break;
                
            case 4:
                validador = 0;
                break;

            default:
                printf("Opção Inválida!\n");
                break;
        }
	}
}
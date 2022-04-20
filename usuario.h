#ifndef USUARIO_H
#define USUARIO_H

typedef struct user {
	char nome[20];
	char codigo_pais[5];
	char ddd[3];
	char numero[9];
} User;

void usuario();

#endif /* USUARIO_H */
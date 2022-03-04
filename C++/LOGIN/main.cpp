#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<conio.h>

// #define USUARIO "c"
// #define CLAVE "java"

#define LONGITUD 5
#define MAX_INTENTO 3

#define NUMERO_USUARIOS 5


int main() {
	char usuario[LONGITUD + 1];
	char clave[LONGITUD + 1];
	int intento = 0;
	int ingresa = 0; //
	char caracter;
	int i = 0;
	int j = 0;
	
	/* Declaracion  e inicializacion de arreglos de usuarios y claves */
	char usuarios[NUMERO_USUARIOS][LONGITUD + 1]; // ={"luis", "jorge", "james", "johan", "kevin"};
	char claves[NUMERO_USUARIOS][LONGITUD + 1]; // ={"123", "456", "789", "abc", "efg"};
	
	/* Se llenan los usuarios en el array */
	strcpy(usuarios[0], "luis");
	strcpy(usuarios[1], "jorge");
	strcpy(usuarios[2], "james");
	strcpy(usuarios[3], "johan");
	strcpy(usuarios[4], "kevin");
	
	/* Se llaman las claves en el array */
	strcpy(claves[0], "123");
	strcpy(claves[1], "456");
	strcpy(claves[2], "789");
	strcpy(claves[3], "abc");
	strcpy(claves[4], "efg");
	
	
	do {
		system("cls");
		printf("\n\t\t\tINICIO DE SESION\n");
		printf("\t\t\t------------------\n");
		printf("\n\tUSUARIO: ");
		gets(usuario);
		printf("\tCLAVE: ");
		while(caracter = getch()){
			if(caracter == 13){
				clave[i] = '\0';
				break;
			}else if(caracter == 8){
				if(i > 0){
					i--;
				printf("\b \b");
				}
			}else{
				if(i < LONGITUD){
					printf("*");
					clave[i] = caracter;
					i++;
				}
			}
		}
		
	/* El usuario y clave debe coincidir  con algunos de los que se encuentren en el array */
		for (j - 0; j < NUMERO_USUARIOS; ++j){
			if(strcmp(usuario, usuarios[j]) == 0 && strcmp(clave, claves[j]) == 0){
			ingresa = 1;
			break;
			
			}
		}
		
		if(ingresa == 0){
			printf("\n\tUsuario y/o clave son incorrectos\n");
			intento++;
			getchar();
		}
	
	}while(intento < 3 && ingresa == 0);
	
	if(ingresa == 1){
		printf("\n\tBienvenido al Sistema\n");
	}else{
		printf("\n\tHa sobrepasado el numero maximo de intentos permitidos\n");
	}
	
	return 0;
}

#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL,"");

    int dia;
    printf("Digite um número de 1 a 7: ");
    scanf("%d", &dia);

    switch (dia) {
    case 1:
        printf("O dia é DOMINGO");
        break;
    case 2:
        printf("O dia é SEGUNDA");
        break;
    case 3:
        printf("O dia é TERÇA");
        break;
    case 4:
        printf("O dia é QUARTA");
        break;
    case 5:
        printf("O dia é QUINTA");
        break;
    case 6:
        printf("O dia é SEXTA");
        break;
    case 7:
        printf("O dia é SABADO");
        break;
    default:
        printf("O número não é válido.");
        break;
    }
return 0;
}

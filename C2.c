#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL,"");

    int dia;
    printf("Digite um n�mero de 1 a 7: ");
    scanf("%d", &dia);

    switch (dia) {
    case 1:
        printf("O dia � DOMINGO");
        break;
    case 2:
        printf("O dia � SEGUNDA");
        break;
    case 3:
        printf("O dia � TER�A");
        break;
    case 4:
        printf("O dia � QUARTA");
        break;
    case 5:
        printf("O dia � QUINTA");
        break;
    case 6:
        printf("O dia � SEXTA");
        break;
    case 7:
        printf("O dia � SABADO");
        break;
    default:
        printf("O n�mero n�o � v�lido.");
        break;
    }
return 0;
}

#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL,"");

    float n1, n2, resultado;
    int op;
    printf("Digite o primeiro n�mero: ");
    scanf("%f", &n1);
    printf("Escolha o n�mero da opera��o: \n");
    printf("1. Soma\n");
    printf("2. Subtra��o\n");
    printf("3. Multiplica��o\n");
    printf("4. Divis�o\n");
    scanf("%d", &op);
    printf("Digite o segundo n�mero: ");
    scanf("%f", &n2);

    switch (op) {
    case 1:
        resultado = n1 + n2;
        printf("A soma dos n�meros �: %.2f", resultado);
        break;
    case 2:
        resultado = n1 - n2;
        printf("A subtra��o dos n�meros �: %.2f", resultado);
        break;
    case 3:
        resultado = n1 * n2;
        printf("A multiplica��o dos n�meros �: %.2f", resultado);
        break;
    case 4:
        if (n2 != 0) {
            resultado = n1 / n2;
            printf("A divis�o dos n�meros �: %.2f", resultado);
        } else {
            printf("N�o � poss�vel fazer divis�o por 0!");
        }
        break;
    default:
        printf("Opera��o invalida: ");
        break;
    }

return 0;
}

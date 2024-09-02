#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL,"");

    float n1, n2, resultado;
    int op;
    printf("Digite o primeiro número: ");
    scanf("%f", &n1);
    printf("Escolha o número da operação: \n");
    printf("1. Soma\n");
    printf("2. Subtração\n");
    printf("3. Multiplicação\n");
    printf("4. Divisão\n");
    scanf("%d", &op);
    printf("Digite o segundo número: ");
    scanf("%f", &n2);

    switch (op) {
    case 1:
        resultado = n1 + n2;
        printf("A soma dos números é: %.2f", resultado);
        break;
    case 2:
        resultado = n1 - n2;
        printf("A subtração dos números é: %.2f", resultado);
        break;
    case 3:
        resultado = n1 * n2;
        printf("A multiplicação dos números é: %.2f", resultado);
        break;
    case 4:
        if (n2 != 0) {
            resultado = n1 / n2;
            printf("A divisão dos números é: %.2f", resultado);
        } else {
            printf("Não é possível fazer divisão por 0!");
        }
        break;
    default:
        printf("Operação invalida: ");
        break;
    }

return 0;
}

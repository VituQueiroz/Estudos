#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL,"");
    int n, i, soma = 0;

    printf("Digite o n�mero de valores que deseja somar: ");
    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        int valor;
        printf("Digite o %d� valor: ", i + 1);
        scanf("%d", &valor);
        soma += valor;
    }

    printf("A soma dos valores �: %d\n", soma);

    return 0;
}

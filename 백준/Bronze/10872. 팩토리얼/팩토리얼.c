#include <stdio.h>

int main() {
    int N, result = 1;
    scanf("%d", &N);
    if (N == 0)
        result = 1;
    else {
        for (int i = 1; i <= N; i++) {
            result *= i;
        }
    }
    printf("%d", result);
}
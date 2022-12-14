#include <stdio.h>

int main() {
    int N, M, result = 1;
    scanf("%d", &N);
    scanf("%d", &M);
    printf("%d", (M - 1) + M * (N - 1));
}
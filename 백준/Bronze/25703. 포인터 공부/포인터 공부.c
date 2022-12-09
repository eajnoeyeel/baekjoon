#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);
    printf("int a;\nint *ptr = &a;\n");
    if (N > 1) {
        printf("int **ptr2 = &ptr;\n");
        for (int i = 3; i < N + 1; i++) {
            printf("int ");
            for (int j = 0; j < i; j++) {
                printf("*");
            }
            printf("ptr%d = &ptr%d;\n", i, i - 1);
        }
    }
}
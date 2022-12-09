#include <stdio.h>

int main() {
    int N, temp, count = 0;
    scanf("%d", &N);
    temp = N;
    do {
        int div = temp / 10;
        int mod = temp % 10;
        temp = mod * 10 + (div + mod) % 10;
        count++;
    } while (N != temp);
    printf("%d", count);
}
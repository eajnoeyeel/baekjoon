#include <stdio.h>

int main() {
    int prev = 0, num, temp;
    for (int i = 0; i < 2; i++) {
        scanf("%d", &num);
        int res = 0;
        while (num != 0) {
            res *= 10;
            temp = num % 10;
            res += temp;
            num /= 10;
        }
        if (prev < res)
            prev = res;
    }
    printf("%d", prev);
}
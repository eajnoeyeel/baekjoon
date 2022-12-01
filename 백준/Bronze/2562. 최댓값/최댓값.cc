#include <stdio.h>

int main() {
    int num, res = 0, count = 0;
    for (int i = 0; i < 9; i++) {
        scanf("%d", &num);
        if (res < num) {
            res = num;
            count = i;
        }
    }
    printf("%d\n%d\n", res, count + 1);
}
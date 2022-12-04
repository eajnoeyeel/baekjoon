#include <stdio.h>

int main() {
    int arr[28], res[30];

    for (int i = 0; i < 28; i++) {
        scanf("%d", &arr[i]);
    }

    for (int j = 0; j < 30; j++) {
        res[j] = 31;
    }

    for (int k = 0; k < 28; k++) {
        res[arr[k] - 1] = k;
    }

    for (int l = 0; l < 30; l++) {
        if (res[l] == 31)
            printf("%d\n", l + 1);
    }
}
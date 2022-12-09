#include <stdio.h>

int main() {
    signed int count, result;
    scanf("%d", &count);
    signed int arr[50];
    for (int i = 0; i < count; i++)
        scanf("%d", &arr[i]);

    for (int j = 0; j < count - 1; j++) {
        for (int k = 0; k < count - 1 - j; k++) {
            if (arr[k] > arr[k + 1]) {
                signed int temp = arr[k];
                arr[k] = arr[k + 1];
                arr[k + 1] = temp;
            }
        }
    }

    if (count % 2 == 0)
        result = arr[count / 2 - 1] * arr[count / 2];
    else
        result = arr[count / 2] * arr[count / 2];

    printf("%d", result);
}

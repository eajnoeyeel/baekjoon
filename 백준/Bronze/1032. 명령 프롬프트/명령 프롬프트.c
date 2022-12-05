#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    int N;
    scanf("%d", &N);
    char **files = (char **) malloc(N * sizeof(char *));
    char *result = NULL;

    if (files == NULL) {
        exit(0);
    } else {
        for (int i = 0; i < N; i++) {
            files[i] = (char *) malloc(50 * sizeof(char) + 1);
            scanf("%s", *(files + i));
        }
    }
    if (N == 1)
        printf("%s", *files);
    else {
        result = files[0];
        for (int j = 0; j < strlen(*files); j++) {
            for (int k = 0; k < N - 1; k++) {
                if (files[k][j] == files[k + 1][j])
                    continue;
                else
                    result[j] = '?';
            }
        }
        printf("%s", result);
    }
}


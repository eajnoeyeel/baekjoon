#include <stdio.h>
#include <stdlib.h>

int main() {
    int N;
    scanf("%d", &N);

    int **map = malloc(N * sizeof(int *));
    if (map == NULL) {
        // malloc failed, handle error
        return 1;
    }
    for (int i = 0; i < N; i++) {
        map[i] = malloc(5 * sizeof(int));
        if (map[i] == NULL) {
            // malloc failed, handle error
            return 1;
        }
    }

    // Read in the map array
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < 5; j++) {
            scanf("%d", &map[i][j]);
        }
    }

    int *res = malloc(N * sizeof(int));
    if (res == NULL) {
        // malloc failed, handle error
        return 1;
    }
    for (int i = 0; i < N; i++) {
        res[i] = 0;
    }

    for (int row = 0; row < N; row++) {
        for (int i = 0; i < N; i++) {
            for (int col = 0; col < 5; col++) {
                if (map[row][col] == map[i][col] && row != i) {
                    res[i]++;
                    break;
                }
            }
        }
    }

    int max = 0, idx = 0;
    for (int i = 0; i < N; i++) {
        if (max < res[i]) {
            max = res[i];
            idx = i;
        }
        else if (max == res[i]) {
            if (i < idx)
                idx = i;
        }
    }

    printf("%d", idx + 1);

    for (int i = 0; i < N; i++) {
        free(map[i]);
    }
    free(map);
    free(res);

    return 0;
}

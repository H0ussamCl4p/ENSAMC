#include <stdio.h>
#include <stdlib.h>

int min(int x, int y) {
    return x < y ? x : y;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;

    int *a = (int*) malloc(n * sizeof(int));
    int *b = (int*) malloc(n * sizeof(int));

    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    for (int i = 0; i < n; i++) {
        scanf("%d", &b[i]);
    }

    // find minimum of a[]
    int mn = a[0];
    for (int i = 1; i < n; i++) {
        if (a[i] < mn) mn = a[i];
    }

    long long best = -1;

    // try all possible c from 0 to mn
    for (int c = 0; c <= mn; c++) {
        long long steps = 0;
        int ok = 1;
        for (int i = 0; i < n; i++) {
            int diff = a[i] - c;
            if (b[i] == 0) {
                if (diff != 0) {
                    ok = 0;
                    break;
                }
                // if diff == 0, no steps needed for this i
            } else {
                if (diff < 0 || diff % b[i] != 0) {
                    ok = 0;
                    break;
                }
                steps += diff / b[i];
            }
        }
        if (ok) {
            if (best < 0 || steps < best) {
                best = steps;
            }
        }
    }

    printf("%lld\n", best);

    free(a);
    free(b);
    return 0;
}

#include <stdio.h>

/* #define MAXN 100
#define MAXM 100  // partially accepted */

#define MAXN 1005
#define MAXM 1005  
// accepted , HackerEarth test files can be large. The grid can be up to 1000 × 1000 (sometimes more).


int main() {
    int t, n, m;
    char tab[MAXN][MAXM+1]; // +1 for string terminator when reading rows

    scanf("%d", &t);
    while (t--) {
        scanf("%d %d", &n, &m);

        for (int i = 0; i < n; i++) {
            scanf("%s", tab[i]); // read entire row as string
        }

        int ans = 0;

        // check rows
        for (int i = 0; i < n; i++) {
            int cnt = 0;
            for (int j = 0; j < m; j++) {
                if (tab[i][j] == '#') {
                    cnt++;
                    if (cnt > ans) ans = cnt;
                } else {
                    cnt = 0;
                }
            }
        }

        // check columns
        for (int j = 0; j < m; j++) {
            int cnt = 0;
            for (int i = 0; i < n; i++) {
                if (tab[i][j] == '#') {
                    cnt++;
                    if (cnt > ans) ans = cnt;
                } else {
                    cnt = 0;
                }
            }
        }

        printf("%d\n", ans);
    }

    return 0;
}

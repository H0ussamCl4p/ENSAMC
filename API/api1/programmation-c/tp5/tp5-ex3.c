#include <stdio.h>
#include <ctype.h>

int main() {
    char CH[101];
    int ABC[26] = {0};
    char *PCH = CH;
    int i;
    printf("Entrez une chaine (max 100 caractères) :\n");
    fgets(CH, 101, stdin);
    while (*PCH != '\0') {
        if (isalpha(*PCH)) {
            char c = tolower(*PCH);
            ABC[c - 'a']++;
        }
        PCH++;
    }
    printf("Occurrences des lettres :\n");
    for (i = 0; i < 26; i++) {
        if (ABC[i] > 0) {
            printf("%d fois la lettre '%c'\n", ABC[i], 'A' + i);
        }
    }
    return 0;
}

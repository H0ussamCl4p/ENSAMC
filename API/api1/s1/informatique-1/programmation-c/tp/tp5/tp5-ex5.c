#include <stdio.h>
#include <string.h>
#include <ctype.h>

int estPalindromeMot(const char *chaine) {
    int i = 0, j = strlen(chaine) - 1;
    while (i < j) {
        if (chaine[i] != chaine[j])
            return 0;
        i++;
        j--;
    }
    return 1;
}

int estPalindromePhrase(const char *chaine) {
    int i = 0, j = strlen(chaine) - 1;
    while (i < j) {
        while (i < j && !isalnum(chaine[i])) i++;
        while (i < j && !isalnum(chaine[j])) j--;
        if (tolower(chaine[i]) != tolower(chaine[j]))
            return 0;
        i++;
        j--;
    }
    return 1;
}

int main() {
    char texte[200];
    printf("Entrez une chaine : ");
    fgets(texte, sizeof(texte), stdin);
    texte[strcspn(texte, "\n")] = 0;
    if (estPalindromeMot(texte))
        printf("C'est un mot palindrome.\n");
    else
        printf("Ce n'est pas un mot palindrome.\n");
    if (estPalindromePhrase(texte))
        printf("C'est une phrase palindrome.\n");
    else
        printf("Ce n'est pas une phrase palindrome.\n");
    return 0;
}

#include <stdio.h>
#include <ctype.h>

void crypter(char *message, int ordre) {
    for (int i = 0; message[i] != '\0'; i++) {
        if (isalpha(message[i])) {
            char base = isupper(message[i]) ? 'A' : 'a';
            message[i] = (message[i] - base + ordre) % 26 + base;
        } else if (isdigit(message[i])) {
            message[i] = (message[i] - '0' + ordre) % 10 + '0';
        }
    }
}

void decrypter(char *message, int ordre) {
    for (int i = 0; message[i] != '\0'; i++) {
        if (isalpha(message[i])) {
            char base = isupper(message[i]) ? 'A' : 'a';
            message[i] = (message[i] - base - ordre + 26) % 26 + base;
        } else if (isdigit(message[i])) {
            message[i] = (message[i] - '0' - ordre + 10) % 10 + '0';
        }
    }
}

int main() {
    char message[200];
    int ordre;
    printf("Entrez un message : ");
    fgets(message, sizeof(message), stdin);

    do {
        printf("Entrez l’ordre de cryptage (entre 1 et 9) : ");
        scanf("%d", &ordre);
    } while (ordre < 1 || ordre > 9);
    printf("La cle choisie est : %d \n", ordre);
    crypter(message, ordre);
    printf("Message chiffre : %s", message);
    decrypter(message, ordre);
    printf("Message dechiffre : %s", message);
    return 0;
}

/*
 * Exercice : structures en C
 * Lire n étudiants (nom, prénom, âge, note) dans un tableau de struct puis les afficher.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Students{
    char name[30];
    char lastname[30];
    int age;
    float mark;

};

int main()
{
    int number;

    printf("Hello please enter number of students : \n");
    scanf("%d",&number);

    getchar();

    struct Students student[number];
    for (int i=0;i<number;i++){
        printf("Enter student %d info :\n",i+1);
        printf("name : ");
        fgets(student[i].name, sizeof(student[i].name), stdin);
        printf("lastname : ");
        fgets(student[i].lastname, sizeof(student[i].lastname), stdin);
        student[i].name[strcspn(student[i].name, "\n")] = '\0';
        student[i].lastname[strcspn(student[i].lastname, "\n")] = '\0';
        printf("age : ");
        scanf("%d",&student[i].age);
        printf("mark : ");
        scanf("%f",&student[i].mark);

        getchar();
    }

    printf("\n--- Students Info ---\n");
    for (int i = 0; i < number; i++) {
        printf("Student %d:\n name : %s\n lastname :%s\n Age: %d\n Mark: %.2f\n",
               i + 1, student[i].name, student[i].lastname,
               student[i].age, student[i].mark);
    }
    return 0;
}

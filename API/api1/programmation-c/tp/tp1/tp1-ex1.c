#include <stdio.h>

int main()
{
    int choix;
    float R1,R2,R3,Req;
    printf("Veuillez saisir les valeur de R1 ,R2 et R3\n");
    scanf("%f %f %f",&R1,&R2,&R3);
    printf("Choissez le type de branchement ; 1 pour serie , 2 pour parallele :\n");
    scanf("%d",&choix);
    switch (choix) {
        case 1 :
            Req = R1 + R2 +R3;
            printf("La resitance equivalente est Req = %f",Req) ;
            break ;
        case 2 :
            Req = (R1*R2*R3)/(R1+R2+R3);
            printf("La resitance equivalente est Req = %f",Req) ;
            break ;
        default:
            break;
    }
    return 0;
}

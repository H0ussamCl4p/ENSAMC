#include <stdio.h>
#include <math.h>


int main()
{
    float a,b,c,x,x1,x2,re,img,delta; // re pour reel , img pour imaginaire , a,b et c sont les coefficients d'une equation du second degree
    printf("Veuillez entrer les coefficients a,b et c de l'equation :\n");
    scanf("%f %f %f",&a,&b,&c);
    if (a==0) {
        if ( b!=0) {
            x = - c/b;
            printf("La solution de l'equation est x=%f",x);
        }
        else {
            printf("L'equation admet une infinite de solutions !");
        }
    }
    else {
        if (c==0) {
            x1 = 0;
            x2 = -b/a;
            printf("Il existe deux solutions pour l'equation x1 = %f et x2= %f",x1,x2);
        }
        else {
            delta = b*b-4*a*c;
            if (delta==0) {
                x = -b/(2*a);
                printf("L'equation admet une solution unique : x = %f",x);
            }
            else if (delta > 0) {
                x1 = (-b-sqrt(delta))/(2*a);
                x2 = (-b+sqrt(delta))/(2*a);
                printf("L'equation admet deux solutions  , x1 = %f et x2 = %f",x1,x2);
            }
            else {
                re = -b / (2 * a);
                img = sqrt(-delta) / (2 * a);
                printf("L'equation admet deux solutions complexes :\n");
                printf("x1 = %f - %f i\n", re, img);
                printf("x2 = %f + %f i\n", re, img);
            }
        }
    }
    return 0;
}

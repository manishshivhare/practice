#include<stdio.h>
#include<math.h>


float Foa(float m1, float m2, float r);

float main ()
{
    double m1, m2, r, force, result;
    printf("Enter the mass of obects m1 and m2 in kgs respectively: ");
    scanf("%f%f", &m1, &m2 );
    printf("Enter the distance b/w them in meter : ");
    scanf("%lf", &r);
    printf("the force of attraction between them is %f", result);
}
float Foa(float m1, float m2, float r)
{
    double result;
    result = (9.8 * m1 * m2)/ (pow(r, 2));
    return result;
}
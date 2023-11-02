#include<stdio.h>

float main (){

    float p, y, I, int_amt, tot_amt; 

    printf("Enter the pricipal amount:\n");
    scanf("%f", &p);

    printf("Enter the duration in years amount:\n");
    scanf("%f", &y);

    printf("Enter the intrest rate amount:\n");
    scanf("%f", &I);

    int_amt = p*y*I/100;
    printf("your intrest amount is: %f \n", int_amt );

    tot_amt = int_amt + p;
    printf("total amount is: %f", tot_amt);







}
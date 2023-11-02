#include <stdio.h>
float avg1(float a, float b, float c);

float main()
{
    float a, b, c, res;
    printf("Enter numbers to find its Average: ");
    scanf("%f%f%f", &a, &b, &c);
    printf("The average of given number is %f", res);
}

float avg1(float a, float b, float c)
{
    float res;
    res = (a + b + c) / 3;
}
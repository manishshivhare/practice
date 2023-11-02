#include <stdio.h>

int main()
{
    int i, num, rem,num1;

    printf("Enter the Number: ");
    scanf("%d", &num);

    num1 = num;

    for (i = 1; i < 6; i++)
    {
        rem = num1 % 10 ;
        printf("%d\n", rem);
        num1 /= 10;
    }
}
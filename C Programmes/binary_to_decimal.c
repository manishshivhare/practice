#include <stdio.h>
#include <math.h>

int main()
{
    int num, rem, dec, i = 0;
    printf("ENter the binary number: ");
    scanf("%d", &num);

    while (num != 0)
    {
        rem = num % 2;
        dec += rem * pow(2, i);
        num /= 10;

        ++i;
    }
    printf("%d", dec); 
}
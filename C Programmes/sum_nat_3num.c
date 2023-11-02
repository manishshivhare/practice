#include <stdio.h>

int main()
{
    int i = 1, sum = 0;

    for (i = 0; i <= 10; i++)
    {
        sum = sum + i;
    }

        do{
            sum += i;
            i++;
        }while(i<=10);
    printf("sum of first 10 natural no. %d", sum);
}
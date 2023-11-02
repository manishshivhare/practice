#include<stdio.h>

int main()
{
    int i, n =3, sum = 1;

    for(i=1; i<=n; i++)
    {
        sum *= i;
    }
    printf("%d", sum);
}
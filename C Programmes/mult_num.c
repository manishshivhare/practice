#include <stdio.h>

int main()
{
    int n, i;
    printf("Enter the value: ");
    scanf("%d", &n);

    for (i = 10; i > 0; i--)
    {

        printf("\n%d X %d = %d", n, i, n * i);
    }
}
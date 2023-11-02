#include <stdio.h>
#include <conio.h>

int main()
{
    int order, i, j;
    printf("order of matrix\n");
    scanf("%d", &order);

    for (i = 1; i <= order; i++)
    {
        for (j = 1; j < order; j++)
        {

            printf("*");
        }
        printf("*\n");
        
    }
}
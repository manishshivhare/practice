#include <stdio.h>

int main()
{
    int i, j, c, k, t = 2, value;

    printf("ENter the value of lines: ");
    scanf("%d", &value);
    c = value;
    for (i = 1; i <= value; i++)
    {

        for (j = c; j > 1; j--)
        {
            printf(" ");
        }
        for (k = 1; k < t; k++)
        {
            printf("*");
            printf(" ");
        }
        printf("\n");
        t++;
        c--;
    }
}
#include <stdio.h>

void main()
{

    int i, j, k;

    for (i = 71; i >= 65; i--)
    {
        for (j = 65; j <= i; j++)
        {
            printf("%c", j);
        }

        for (k = 71; k > j - 1; k--)
        {
            printf(" ");
        }
        for (k = i; k < 70; k++)
        {
            printf(" ");
        }
        for (j = j - 1; j >= 65; j--)
        {
            if (j == 71)
            {
                j = 70;
                printf("%c", j);
            }
            else
            {
                printf("%c", j);
            }
            printf("\n");
        }
    }
}
h
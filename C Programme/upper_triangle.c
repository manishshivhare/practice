#include <stdio.h>

int main()
{
    int i, j, c, num;
    c = num;
    

    printf("Enter the value for number of line : ");
    scanf("%d", &num);
    for (i = 1; i <= num; i++)
    {
        printf("\n");

        for (j = c; j >= 1; j--)
        {
            printf("%d", j);
        }
        c--;
    }
}
#include <stdio.h>

int main()
{
    int num, chang, rem, sum ;
    printf("ENter the Postive Number: ");
    scanf("%d", &num);
    chang = num;

    while (chang != 0)
    {
        rem = chang % 10;
        

        if (rem % 2 != 0)
        {
            // printf("%d", rem);
            sum += rem;
        }
        else
        {
            printf("%d else \n", rem);
        }
        chang /= 10;
    }
    printf("%d", sum);
}
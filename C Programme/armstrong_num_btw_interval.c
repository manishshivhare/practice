#include <stdio.h>

int main()
{
    int num, remainder, result = 0, i;
    num = i;

    for (i = 100; i <= 500; i++)
    {

        while (num != 0)
        {
            remainder = num % 10;
            result += (remainder * remainder * remainder);

            num /= 10;
            
            printf("%d\t", i);
        }
        
            // printf("%d\t", result);

        // if (result == i)
        // {
        //     printf("%d/t", result);
        // }
    }
}
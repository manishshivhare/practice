#include <stdio.h>

int main()
{
    int i, result = 0, n, c;
    for (i = 1; i <= 300; i++)
    {
        i = n;
        for (i = 1; i <= n; i++)
        {
            if (n % i == 0)
            {

                c++;
            }
            if (c == 2)
            {
                return result += n;
            }
        }

        printf("%d", result);
    }
}

#include <stdio.h>

int main()
{
    int a, b, x, n, y;
    printf("Value of a, x, b and n respectively: ");
    scanf("%d%d%d%d", &a, &x, &b, &n);

    if (n == 1)
    {
        y = (a * x) % b;
        printf("value of Y = %d", y);
    }
    else if (n == 2)
    {   
        y = a * x * 2 + b * 2;
        printf("value of Y = %d", y);
    }
    else if (n == 3)
    {
        y = a - b * x;
        printf("value of Y = %d", y);
    }
    else if (n == 4)
    {
        y = a + x / b;
        printf("value of Y = %d", y);
    }
    
    return 0;
}
#include <stdio.h>
int factorial(int f);
int main()
{
    int x = 1, n, result = 0,f = 1;
    printf("Enter the value of x and y: ");
    scanf("%d%d", &x, &n);

    while (n != 0)
    {
        result += (1 - (x*1/factorial(f)));
        x++;
        f++;
        n--;

    }
    printf("%d", result);
}

int factorial(int f)
{
    if (f == 1 || f == 0)
    {
        return 1;
    }
    else
    {
        return f * factorial(f - 1);
    }
}
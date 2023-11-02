#include <stdio.h>

int factorial(int X);
int main()
{
    int n, i, result = 0;
    printf("Enter the Value of n: ");
    scanf("%d", &n);

    while (n != 0)
    {
        result += factorial(n);
        n--;
    }

    printf("the sum of factorial of first %d terms %d", n, result);

    return 0;
}

int factorial(int X)
{
    if (X == 1 || X == 0)
    {
        return 1;
    }
    else
    {
        return X * factorial(X - 1);
    }
}

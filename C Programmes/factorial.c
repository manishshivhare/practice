#include <stdio.h>

int factorial(int X);

int main()
{
    int a;
    printf("Write a number to find its factorial: ");
    scanf("%d", &a);
    printf("The factorial of %d is %d", a, factorial(a));
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
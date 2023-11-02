#include <stdio.h>

int sum(int a, int b, int c);

int main()
{

    int c, a, b;
    printf("enter a b and c respectively: ");
    scanf("%d%d%d", &a, &b, &c);
    c = sum(a, b, c);
    printf("equal to %d", c);
    return 0;
}

int sum(int a, int b, int c)
{

    int result;
    result = a + b + c;
    return result;
}
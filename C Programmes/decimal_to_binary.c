#include <stdio.h>

int main()
{
    int num, place = 1, bin = 0, rem;
    printf("Enter the number: ");
    scanf("%d", &num);

    while (num)
    {
        rem = num % 2;
        num /= 2;
        bin = bin + (rem * place);
        place *= 10;
    }
    printf("%d", bin);
}
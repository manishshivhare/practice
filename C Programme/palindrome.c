#include <stdio.h>

int main()
{
    int num, rev, d1, d2, d3, org;
    printf("Enter your three digit No: ");
    scanf("%d", &num);
    org = num;

    if (num < 999)
    {
        d1 = num % 10;
        num = num / 10;
        d2 = num % 10;
        num = num / 10;
        d3 = num % 10;
        num = num / 10;

        rev = d1 * 100 + d2 * 10 + d3;
        printf("%d is your reversed num\n", rev);

        if (rev == org)
        {

            printf("palindrome");
        }
        else
        {
            printf("not a palindrome");
        }
    }

    else
    {
        printf("not a valid number");
    }
    return 0;
}

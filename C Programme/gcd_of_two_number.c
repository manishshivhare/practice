#include <stdio.h>

int gcd(int a, int b);

void main()
{
    int gcd_num, num1, num2;

    printf("Enter two numbers: ");
    scanf("%d%d", &num1, &num2);

    gcd_num = gcd(num1, num2);

    printf("The GCD of given number = %d", gcd_num );
}
int gcd(int a, int b)
{
    int  lcm, mul, gcd1;
    

    lcm = (a > b) ? a : b;

    while (1)
    {
        if (lcm % a == 0 && lcm % b == 0)
        {
            break;
        }
        ++lcm;
    }

    mul = (a * b);
    gcd1 = (mul / lcm);
    return gcd1;
    
}
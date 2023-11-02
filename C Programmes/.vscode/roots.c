#include <stdio.h>
#include <math.h>
// #include <conio.h>

int main()
{

        float c1, c2, c3, discriminant, root1, root2, realPart, imagPart;

    printf("cofficient of a: ");
    scanf("%f", &c1);
    printf("cofficient of b: ");
    scanf("%f", &c2);
    printf("constant: ");
    scanf("%f", &c3);

    discriminant = pow(c2, 2) - 4 * c1 * c3;

    if (discriminant > 0)
    {
        root1 = (-c2 + sqrt(discriminant)) / (2 * c1);
        root2 = (-c2 - sqrt(discriminant)) / (2 * c1);
        printf("\nroot1 = %f and root2 = %f", root1, root2);
    }

    else if (discriminant == 0)
    {
        root1 = -c2 / (2 * c1);
        root2 = -c2 / (2 * c1);
        printf("\nroot1 = root2 = %f;", root1);
    }

    else
    {
        realPart = -c2 / (2 * c1);
        imagPart = (sqrt(-discriminant) / (2 * c1));
        printf("root1 = %f+%fi and root2 = %f-%fi", realPart, imagPart, realPart, imagPart);
    }

    return 0;
}

#include <stdio.h>
    #include <math.h>

float main()
{

    float a, b, c, s, area;
    printf("Enter the sides of triangle:\n");
    scanf("%f%f%f", &a, &b, &c);

    s = (a + b + c) / 2;
    area = sqrt(s * (s - a) * (s - b) * (s - c));
    printf("area of triangle is: %f", area);

    return 0;
}

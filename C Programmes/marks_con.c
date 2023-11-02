#include <stdio.h>

int main()
{
    int phy, chem, maths, sum1, sum2;

    printf("marks obtained in PCM respectively: ");
    scanf("%d%d%d", &phy, &chem, &maths);

    sum1 = phy + maths;
    sum2 = sum1 + chem;

    if (phy > 40 && chem > 50 && maths > 60)
    {
        printf("Student is eligible for this course");
    }
    else if (sum1 > 150 && sum2 > 200)
    {
        printf("yes");
    }
    else
    {
        printf("Student is not eligible for this course");
    }

    return 0;
}